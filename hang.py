import random
import string
import re
import os.path

WORDLIST_FILENAME = "dicao.txt"
TOTAL_GUESSES = 8

def loadWords():
    print "Loading word list from file..."
    if os.path.isfile(WORDLIST_FILENAME):
        inFile = open(WORDLIST_FILENAME, 'r', 0)
        line = inFile.readline()
        wordlist = string.split(line)
        print '  ', len(wordlist), "words loaded."
        return random.choice(wordlist)
    else:
        print 'Oops! File', WORDLIST_FILENAME, 'not found.'
        raise SystemExit(0)

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

def isValidInput(letter):
    if re.match('^[a-z]$', letter):
        return True
    else:
        return False

def guessesAreOver(guessesLeft):
    if guessesLeft > 0:
        return False
    else:
        return True

def hangman(secretWord):
    guessesLeft = TOTAL_GUESSES
    print guessesLeft
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    print '-------------'

    while not isWordGuessed(secretWord, lettersGuessed) and not guessesAreOver(guessesLeft):
        print 'You have', guessesLeft, 'guesses left.'
        print 'Available letters:', getAvailableLetters(lettersGuessed)

        letter = raw_input('Please guess a letter: ').lower()
        if isValidInput(letter):
            if letter in secretWord:
                lettersGuessed.append(letter)
                print 'Good Guess: ', getGuessedWord(secretWord, lettersGuessed)

            elif letter in lettersGuessed:
                print 'Oops! You have already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed)

            else:
                guessesLeft -=1
                lettersGuessed.append(letter)
                print 'Oops! That letter is not in my word: ',  getGuessedWord(secretWord, lettersGuessed)

        else:
            print 'Oops! Only one letter [a-z] allowed! My word: ',  getGuessedWord(secretWord, lettersGuessed)

        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'

        else:
            print 'Sorry, you ran out of guesses. The word was:', secretWord

secretWord = loadWords().lower()
hangman(secretWord)
