# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    match_counter = 0
    for c in secretWord:
        if c in lettersGuessed:
            match_counter += 1
    if match_counter == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed_so_far = ''
    for c in secretWord:
        if c in lettersGuessed:
            guessed_so_far += c
        else:
            guessed_so_far += ' _ '
    return guessed_so_far

def compare_guess_to_word(secretWord, guess, lettersGuessed):
    guesses_made = 0
    for c in secretWord:
        if guess in secretWord:
            print lettersGuessed
            print 'Good guess : '+getGuessedWord(secretWord, lettersGuessed)
            return guesses_made
        else:
            print lettersGuessed
            print 'Oops! That letter is not in my word : '+getGuessedWord(secretWord, lettersGuessed)
            guesses_made += 1
            return guesses_made

def compare_guess_to_guessed_list(secretWord, guess, lettersGuessed):
    for l in lettersGuessed:
        if guess in lettersGuessed:
            print "You've already guessed that letter : "+getGuessedWord(secretWord, lettersGuessed)
            return True
#        else:
#            lettersGuessed.append(guess)
#            return False
            
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lowercase_letters = string.ascii_lowercase
    letters_left = ''
    for l in lowercase_letters:
        if l not in lettersGuessed:
            letters_left += l
    return letters_left

def set_end_game_check(count):
    return count

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is %d letters long' % len(secretWord)
    
    print '-----------------------'
    
    max_guess_count = 8
    letters_guessed = []
    
    while max_guess_count > 0:
        print 'You have %d guesses left' % max_guess_count
        print 'Available Letters : '+getAvailableLetters(letters_guessed)
        guess = raw_input('Please guess a letter : ').lower()
        check_list = compare_guess_to_guessed_list(secretWord, guess, letters_guessed)
        letters_guessed.append(guess)
        if check_list != True:
            count_now = compare_guess_to_word(secretWord, guess, letters_guessed)
            max_guess_count -= count_now
            
        print '-----------------------'
        end_game = isWordGuessed(secretWord, letters_guessed)
        if end_game == True:
            print 'Congratulations, you won!'
            break
        set_end_game_check(max_guess_count)
    
    end_game = set_end_game_check(max_guess_count)
    if end_game == 0:    
        print 'Sorry, you ran out of guesses. The word was else.'
    letters_guessed[:] = []


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'hello'#chooseWord(wordlist).lower()
hangman(secretWord)