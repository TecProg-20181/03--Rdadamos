import random
import string
import re

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
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
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'

    return guessed

def getAvailableLetters(lettersGuessed):
    available = string.ascii_lowercase
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')

    return available

def checkValidInput(letter):
    if re.match('^[a-z]$', letter):
        return True
    else:
        return False

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    print '-------------'

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have', guesses, 'guesses left.'
        print 'Available letters:', getAvailableLetters(lettersGuessed)

        letter = raw_input('Please guess a letter: ').lower()
        if letter in lettersGuessed:
            print 'Oops! You have already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed)

        elif letter in secretWord:
            lettersGuessed.append(letter)
            print 'Good Guess: ', getGuessedWord(secretWord, lettersGuessed)

        elif not checkValidInput(letter):
            print 'Oops! Only one letter [a-z] allowed! My word: ',  getGuessedWord(secretWord, lettersGuessed)

        else:
            guesses -=1
            lettersGuessed.append(letter)
            print 'Oops! That letter is not in my word: ',  getGuessedWord(secretWord, lettersGuessed)


        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'

        else:
            print 'Sorry, you ran out of guesses. The word was:', secretWord


secretWord = loadWords().lower()
hangman(secretWord)
