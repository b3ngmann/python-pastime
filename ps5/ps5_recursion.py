# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0 or len(aStr) == 1:
        return aStr
    else:
        return aStr[-1] + reverseString(aStr[:-1]) 

print reverseString('abc')    
#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    elif len(x) == 1:
        return x in word
    elif x[0] in word:
        return x_ian(x[1:], word[word.find(x[0])+1:])
    else:
        return False 

print x_ian('eric', 'meritocracy')
print x_ian('eric', 'cerium')
print x_ian('sarina', 'czarina')
print x_ian('alvin', 'palavering')
print x_ian('john', 'mahjong')
print x_ian('eric', 'algebraic')
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    #words = text.split()
    if len(text) < lineLength:
        return text
    else:
        if text[lineLength] == ' ':
            return text[:lineLength + 1] + '\n' + insertNewlines(text[lineLength + 1:].lstrip(), lineLength)
        else:
            if text.find(' ', lineLength - 1) != -1:
                return text[:text.find(' ', lineLength - 1)] + '\n' + insertNewlines(text[text.find(' ', lineLength-1):].lstrip(), lineLength)
            else:
                return text[:] #+ '\n' + insertNewlines(text[:].lstrip(), lineLength)

print insertNewlines('Random text to wrap again.', 5)
print
print insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
print 
print insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20)