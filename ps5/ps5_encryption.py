# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    #return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dict_shift = {}
    lower_flip_count = 0
    upper_flip_count = 0
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    letters       = string.ascii_letters
    
    for i in range(len(letters)):
        if letters[i] in lower_letters:
            if lower_letters[-1] not in dict_shift.values():
                dict_shift[letters[i]] = lower_letters[lower_letters.find(letters[i]) + shift]
            else:
                dict_shift[letters[i]] = lower_letters[lower_flip_count]
                lower_flip_count += 1
        else:
            if upper_letters[-1] not in dict_shift.values():
                dict_shift[letters[i]] = upper_letters[upper_letters.find(letters[i]) + shift]
            else:
                dict_shift[letters[i]] = upper_letters[upper_flip_count]
                upper_flip_count += 1
    return dict_shift

print buildCoder(9)

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    coded_text = ''
    for l in text:
        if l not in string.ascii_letters:
            coded_text += l
        else:
            coded_text += coder[l]
    return coded_text

#print applyCoder("Hello, world!", buildCoder(3))
#print applyCoder("Khoor, zruog!", buildCoder(23))

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    coder = buildCoder(shift)
    return applyCoder(text, coder)

#print applyShift('Bpqa qa i bmab.', 18)
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    code_shift = 0
    count_valid_words = 0
    list_valid_words_count = []
    
    for i in range(0, 26):
        shifted_text = applyShift(text, i)
        shifted_text_words = shifted_text.split()
        for word in shifted_text_words:
            if isWord(wordList, word) == True:
                count_valid_words += 1
            else:
                code_shift += 1
        list_valid_words_count.append(count_valid_words)
    best_shift = max(list_valid_words_count)
    return list_valid_words_count.index(best_shift)
#    max_valid_word_count = 0
#    num_valid_words = 0
#    best_shift = 0
#    for i in range(0, 26):
#        shifted_text = applyShift(text, i)
#        shifted_text_words = shifted_text.split()
#        if shifted_text_words in wordList:
#            num_valid_words += 1
#    if num_valid_words > max_valid_word_count:
#        best_shift = 
#    return best_shift
'''
initial
'''
#code_shift = 0
#    count_valid_words = 0
#    
#    while True:
#        shifted_text = applyShift(text, code_shift)
#        shifted_text_words = shifted_text.split()
#        for word in shifted_text_words:
#            if isWord(wordList, word) == True:
#                count_valid_words += 1
#            else:
#                code_shift += 1
#        if count_valid_words == len(shifted_text_words):
#            return code_shift
#            break
    

print findBestShift(loadWords(), 'Aol xbpg pz... ohyk!')
#print applyShift('Aol xbpg pz... ohyk!', y)    

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    text = getStoryString()
    coder_shift = findBestShift(wordList, text)
    applyShift(text, coder_shift)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
