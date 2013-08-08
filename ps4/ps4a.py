# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# my add-on helper code
def adjusted_freq_return(chr):
    freq = str(getFrequencyDict(chr).values())
    return freq.strip('[]')
    

def get_letter_value(l):
    if SCRABBLE_LETTER_VALUES.get(l) != None: 
        return SCRABBLE_LETTER_VALUES[l]
    else:
        return 0

def get_word_value(word):
    total = 0
    for chr in word:
        freq = int(adjusted_freq_return(chr))
        letter_val_int = int(get_letter_value(chr))
        total += freq * letter_val_int
    return total

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    if len(word) == n:
        score = (n * get_word_value(word)) + 50
    else:
        score = (len(word) * get_word_value(word))
    return score

#print getWordScore('apple', 7)
               
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_dict = hand.copy()
    num = 1
    for l in word:
        if l in hand.keys():
            updated_dict[l] -= num 
    return updated_dict

#d = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}#{'a':1, 'u':2, 'p':3}
#print updateHand(d,'quail')
#print displayHand(updateHand(d,'quail'))
#print
#handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#print updateHand(handOrig, 'hello')


def check_letters(word, hand):
    w = ''
    for l in word:
        if l in hand.keys() and hand[l] >= word.count(l):
            w += l
        else:
            return False
    if w == word:
        return True
    else:
        return False

def check_in_wordList(word, wordList):
    if word in wordList:
        return True
    else:
        return False
#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if len(word) > 0:
        if check_letters(word,hand) == True and check_in_wordList(word,wordList) == True:
            return True
        else:
            return False
    
    
#    for l in word:
#        if len(word) != 0:
#            if l in hand.keys():
#                if hand[l] >= word.count(l):       
#                    if word in wordList:
#                        return True
            
#hand = {'a': 1, 'c': 2, 'u': 2, 't': 2, 'y': 1, 'h': 1, 'z': 1, 'o': 2}#{'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
#word = "chayote"
#print check_letters(word, hand)
#print check_in_wordList(word, loadWords())
#print isValidWord(word, hand, loadWords())
#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    num_char = 0
    for letter in hand.keys():
        for j in range(hand[letter]):
            num_char += 1
    return num_char

#print calculateHandlen(hand)

def improved_display_hand(hand):
    display_hand = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            display_hand += letter + ' '              
    return display_hand
    print

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    total = 0
    user_input = ''
    while len(hand) > 0:
        display_hand = improved_display_hand(hand).rstrip()
        if len(display_hand) > 0:
            print 'Current Hand : ' + display_hand
            user_input = raw_input('Enter word, or a "." to indicate that you are finished : ')
            if user_input != '.':
                valid_word = isValidWord(user_input, hand, wordList)
                if valid_word == True:
                    cur_word_score = getWordScore(user_input, n)
                    total += cur_word_score
                    hand = updateHand(hand, user_input)
                    print '"%s" earned %d. Total: %d points' % (user_input, cur_word_score, total)
                else:
                    print 'Invalid word, please try again.'
            else:
                print 'Goodbye! Total score: %d points.' % total
                break
        else:
            print
            print 'Run out of letters. Total score: %d points.' % total
            break

#hand = {'b': 1, 'e': 2, 'f': 1, 'h': 1, 'k': 1, 'p': 1, 't': 2, 'y': 1}#{'h': 1, 's': 1, 'e': 1, 'o': 1}#{'a': 1, 'c': 2, 'u': 2, 't': 2, 'y': 1, 'h': 1, 'z': 1, 'o': 2}        
#playHand(hand, loadWords(), len(hand))
#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    
    def set_replay_hand(hand):
        return hand
    
    replay_hand = ''
    
    while True:
        user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if user_input == 'n':
            hand = dealHand(HAND_SIZE)
            replay_hand = set_replay_hand(hand)
            playHand(hand, wordList, HAND_SIZE)
        elif user_input == 'r':
            if len(replay_hand):
                playHand(replay_hand, wordList, len(hand))
            else:
                print 'You have not played a hand yet. Please play a new hand first!' 
        elif user_input == 'e':
            break
        else:
            print 'Invalid command'


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
