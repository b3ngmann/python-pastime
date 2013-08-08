from ps4a import *
import time



#my helper functions
def form_valid_word(word, hand):
    w = ''
    for l in word:
        if l in hand.keys() and hand[l] >= word.count(l):
            w += l
        else:
            return None
    if w == word:
        return w

def adjusted_freq_return(chr):
    freq = str(getFrequencyDict(chr).values())
    return freq.strip('[]')

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq    

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

def getWordScore(word, n):
    score = 0
    if len(word) == n:
        score = (n * get_word_value(word)) + 50
    else:
        score = (len(word) * get_word_value(word))
    return score

def improved_display_hand(hand):
    display_hand = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            display_hand += letter + ' '              
    return display_hand
    print

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)

    # Create a new variable to store the best word seen so far (initially None)  

    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.
    
    
    def scan_for_word(hand, wordList, n):
        
        max_score = 0
        best_comp_play = ''
        
        for w in wordList:
            valid_word = form_valid_word(w, hand)
            if valid_word != None:
                valid_word_score = getWordScore(valid_word, n)
                if valid_word_score > max_score:
                    max_score = valid_word_score
                    best_comp_play = valid_word
        return best_comp_play
    
    comp_word = scan_for_word(hand, wordList, n)
    
    if comp_word == '':
        return None
    else:
        return comp_word
        
#print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, loadWords(), 12)      
#print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, loadWords(), 6)
#print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, loadWords(), 12)
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0
    user_input = ''
    while len(hand) > 0:
        display_hand = improved_display_hand(hand).rstrip()
        if len(display_hand) > 0:
            print 'Current Hand : ' + display_hand
            comp_play = compChooseWord(hand, wordList, n) 
            if comp_play != None:
                valid_word = isValidWord(comp_play, hand, wordList)
                if valid_word == True:
                    cur_word_score = getWordScore(comp_play, n)
                    total += cur_word_score
                    hand = updateHand(hand, comp_play)
                    print '"%s" earned %d. Total: %d points' % (comp_play, cur_word_score, total)
#                else:
#                    print 'Invalid word, please try again.'
            else:
                print 'Computer Unable to play! Computer Total score: %d points.' % total
                break
        else:
            print
            print 'Run out of letters. Total score: %d points.' % total
            break

#print compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, loadWords(), 12)
  
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    def set_replay_hand(hand):
        return hand
    
    replay_hand = ''
    
    while True:
        user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if user_input == 'n':
            while True:
                select_player = raw_input('Enter u to have yourself play, c to have the computer play: ')
                
                if select_player == 'u':
                    hand = dealHand(HAND_SIZE)
                    replay_hand = set_replay_hand(hand)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif select_player == 'c':
                    comp_hand = dealHand(HAND_SIZE)
                    replay_hand = set_replay_hand(comp_hand)
                    compPlayHand(comp_hand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command'
        
        
        elif user_input == 'r':
            while True:
                if len(replay_hand) > 0:
                    select_player = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    if select_player == 'u':                
                        playHand(replay_hand, wordList, HAND_SIZE)
                        break
                    elif select_player == 'c':
                        compPlayHand(replay_hand, wordList, HAND_SIZE)
                        break
                else:
                    print 'You have not played a hand yet. Please play a new hand first!' 
                    break

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


