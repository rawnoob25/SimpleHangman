

# Problem Set 2, hangman.py
#THIS VERSION SEEMS STABLE. 
#One issue is that when you press the asterisk, included among
#those words that appear could be those that contain letters
#that you've already guessed that aren't present in the word.
#e.g. word is "apple" and display is "a_ _ l _", and you've already
#guessed the character, "g", but "agile" nevertheless appears
#among the possibilities.
# Time spent:
#7 hours
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #this function is pythonified
    for letter in secret_word:
        if not (letter in letters_guessed):
            return False
    return True
    
      

def test_is_word_guessed():
    val=is_word_guessed("hello",['e','l','l','o'])
    print(val)
    secret_word='apple'
    letters_guessed=['e','i','k','p','r','s']
    print(is_word_guessed(secret_word,letters_guessed))
    val=is_word_guessed("hello",['e','l','l','o','h'])
    print(val)
    val=is_word_guessed("wright",['f','o','o','t','w','r','h','g'])
    print(val)
    val=is_word_guessed("wright",['f','o','i','o','t','w','r','h','g'])
    print(val)
    
#test_is_word_guessed()

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    #try to pythonify this function
    out=""
    for letter in secret_word:
        if letter in letters_guessed:
          out+=(letter)
        else:
            out+="_ "
    return out

def test_get_guessed_word():
    print(get_guessed_word("apple",['e','i','k','p','r','s']))

#test_get_guessed_word()

def anotherIsWordGuessed(secret_word,letters_guessed):
    for i in range(len(secret_word)):
        j=0
        while j<len(letters_guessed):
            if secret_word[i]==letters_guessed[j]:
                print("found "+secret_word[i]+" at position "+str(j)+" in letters_guessed")
                break
            j+=1
        if j==len(letters_guessed):
            return False
    return True
        
#def test_anotherIsWordGuessed():
#     val=anotherIsWordGuessed("hello",['o','e','l'])
#     print(val)

#test_anotherIsWordGuessed()



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    out=""
    lowercaseLetters=string.ascii_lowercase
    for lett in lowercaseLetters:
        if not (lett in letters_guessed):
            out+=lett
    return out

def test_get_available_letters():
    guessed=list("eikprs")
    print(get_available_letters(guessed))

#test_get_available_letters()
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings=3
    dispWelcomeScreen(secret_word,warnings)
    guessesLeft=6
    letters_guessed=[]
    while guessesLeft>0 and not(is_word_guessed(secret_word,letters_guessed)):
        position=processMove(secret_word,letters_guessed,warnings,guessesLeft)
        letters_guessed=position[0]
        warnings=position[1]
        guessesLeft=position[2]

    if guessesLeft<=0:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")
    else:
        n=num_unique_letters(secret_word)
        print("Congratulations, you won!")
        print("Your total score for this game is: "+str(n*guessesLeft))

def num_unique_letters(word):
    letterDictionary={}
    for lett in word:
        if not (lett in letterDictionary):
            letterDictionary[lett]=1
    return len(letterDictionary)

def test_num_unique_letters():
    print(num_unique_letters("dolphin"))


 
def processMove(secret_word,letters_guessed,warnings,guessesLeft):
    print("You have "+str(guessesLeft)+" guesses left.")
    print("Available letters:"+get_available_letters(letters_guessed))
    theGuess=input("Please guess a letter:")[0]
    if not (theGuess.isalpha()):
        if warnings>0:
            warnings-=1
            print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
        else:
            guessesLeft-=1
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word,letters_guessed))
        print("-"*12)
        return (letters_guessed,warnings,guessesLeft)
    else:
        theGuess=theGuess.lower()
    
    if theGuess in letters_guessed:
        if warnings>0:
            warnings-=1
            print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
        else:
            guessesLeft-=1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word,letters_guessed))
    else: #guess was an alphabetic character (letter) and was not present in letters_guessed
        letters_guessed+=theGuess
        if theGuess in secret_word:
            print("Good guess: "+get_guessed_word(secret_word,letters_guessed))
        else: #guessed letter NOT present in secret word; consider vowel and consonant branches separately
            if theGuess in list("aeiou"):
                guessesLeft-=2
                print("Oops! That letter is not in my word: "+get_guessed_word(secret_word,letters_guessed))
            else:
                guessesLeft-=1
                print("Oops! That letter is not in my word: "+get_guessed_word(secret_word,letters_guessed))
    print("-"*12)
    return (letters_guessed,warnings,guessesLeft)

def dispWelcomeScreen(secret_word,warnings):
    load_words()
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    print("You have "+str(warnings)+" warnings left.")
    print("-"*12)

#hangman("else")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word=my_word.replace(" ","")
    if len(my_word)!=len(other_word):
        return False
    n=len(my_word)
    i=0
    while(i<n):
        if not (my_word[i]=="_"):
            if my_word[i]!=other_word[i]:
                return False
        else: #my_word[i] is the blank character
            if other_word[i] in my_word:
                return False
        i+=1
    return True
            
def test_match_with_gaps():
    print(match_with_gaps("a_ _ l_", "atoll"))

#test_match_with_gaps()

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    out=""
    for word in wordlist:
       if match_with_gaps(my_word,word):
           out+=(word+" ")
    print(out)
#    for word in wordlist:
#         if match_with_gaps(my_word,word):
#             print(word)
    
def test_show_possible_matches():
    show_possible_matches("a_ _ l_")

#test_show_possible_matches()

def processMoveWithHints(secret_word,letters_guessed,warnings,guessesLeft):
    print("You have "+str(guessesLeft)+" guesses left.")
    print("Available letters:"+get_available_letters(letters_guessed))
    theGuess=input("Please guess a letter:")[0]
    if not (theGuess.isalpha()):
        if(theGuess=="*"):
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        else:
            if warnings>0:
                warnings-=1
                print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
            else:
                guessesLeft-=1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word,letters_guessed))
        print("-"*12)
        return (letters_guessed,warnings,guessesLeft)
    else:
        theGuess=theGuess.lower()
    
    if theGuess in letters_guessed:
        if warnings>0:
            warnings-=1
            print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
        else:
            guessesLeft-=1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word,letters_guessed))
    else: #guess was an alphabetic character (letter) and was not present in letters_guessed
        letters_guessed+=theGuess
        if theGuess in secret_word:
            print("Good guess: "+get_guessed_word(secret_word,letters_guessed))
        else: #guessed letter NOT present in secret word; consider vowel and consonant branches separately
            if theGuess in list("aeiou"):
                guessesLeft-=2
                print("Oops! That letter is not in my word: "+get_guessed_word(secret_word,letters_guessed))
            else:
                guessesLeft-=1
                print("Oops! That letter is not in my word: "+get_guessed_word(secret_word,letters_guessed))
    print("-"*12)
    return (letters_guessed,warnings,guessesLeft)
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings=3
    dispWelcomeScreen(secret_word,warnings)
    guessesLeft=6
    letters_guessed=[]
    while guessesLeft>0 and not(is_word_guessed(secret_word,letters_guessed)):
        position=processMoveWithHints(secret_word,letters_guessed,warnings,guessesLeft)
        letters_guessed=position[0]
        warnings=position[1]
        guessesLeft=position[2]

    if guessesLeft<=0:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")
    else:
        n=num_unique_letters(secret_word)
        print("Congratulations, you won!")
        print("Your total score for this game is: "+str(n*guessesLeft))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #wordlist=load_words()
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    #hangman_with_hints("apple")