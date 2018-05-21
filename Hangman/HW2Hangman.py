import string

################# HOMEWORK 2.3 HANGMAN ####################

# Get all the words with their values from the given file
words = [line.rstrip('\n') for line in open('hw1_word_counts_05.txt')]

# Alphabet of all uppercase letters
ALPHABET = string.ascii_lowercase.upper()

# Local variables
totalWords = 0      # Total number of words in journal
totalFit = 0        # Total number of words that fit evidence
wordList = []       # List to hold words as [word, count]
probList = []       # List to contain probabilities of each word as [word, prob]
chanceList = []     # List of all the words that fit the evidence given
usedLetter = []     # List of all letters that are guessed correctly or not
letterList = {}     # Dictionary of all letter probabilities
finalList = []      # List that contains letter's with their probability

# Add all word counts to get total number of words in the journal
for word in words:
    wordCount = word.split()
    wordList.append([wordCount[0], wordCount[1]])
    totalWords += int(wordCount[1])

# Get probabilities of each word
for word in words:
    wordCount = word.split()
    probList.append([wordCount[0], int(wordCount[1])/totalWords])

                    #####################################
########## Part (a) Calculate most and least frequent 5-letter words ##########
                    #####################################
# Most frequent : THREE, SEVEN, EIGHT, WOULD, ABOUT

def getWordCount(wordList):
    return int(wordList[1])

sortedList = sorted(wordList, key = getWordCount, reverse = True)
MosFreqList = [sortedList[0], sortedList[1], sortedList[2], sortedList[3], sortedList[4], 
        sortedList[5], sortedList[6], sortedList[7], sortedList[8], sortedList[9]]
print('Most frequent words: ', MosFreqList, '\n')

# Least frequent : BOSAK, CAIXA, MAPCO, OTTIS, TROUP

sortedList = sorted(wordList, key = getWordCount)
LesFreqList = [sortedList[0], sortedList[1], sortedList[2], sortedList[3], sortedList[4],
        sortedList[5], sortedList[6], sortedList[7], sortedList[8], sortedList[9]]
print('Least frequent words: ', LesFreqList, '\n')

                    #####################################
#################### Part (b) Calculations for table ####################
                    #####################################
# Use this function as a key to sort the finalList
def getFloat(list):
    return float(list[1])

# Testing first given case 0.6366
usedLetter = ['E', 'O']

# Calculate all words that fit evidence
for word in wordList:
    if 'E' in word[0] or 'O' in word[0] or ('E' and 'O' in word[0]):
        continue
    else:
        # Get total of all words that fit evidence
        totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    if 'E' in word[0] or 'O' in word[0] or ('E' and 'O' in word[0]):
        continue
    else:
        chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0

    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))

# Testing second given case
# Reset all the lists back to empty
totalFit = 0
chanceList = []
letterList = {}
finalList = []

usedLetter = ['D', 'I']

# Calculate all words that fit evidence
for word in wordList:
    if 'D' in word[0][0] and 'D' not in word[0][1] and 'D' not in word[0][2]:
        if 'D' not in word[0][4] and 'I' in word[0][3] and 'I' not in word[0][1]:
            if 'I' not in word[0][2] and 'I' not in word[0][4]:    
                totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    if 'D' in word[0][0] and 'D' not in word[0][1] and 'D' not in word[0][2]:
        if 'D' not in word[0][4] and 'I' in word[0][3] and 'I' not in word[0][1]:
            if 'I' not in word[0][2] and 'I' not in word[0][4]:    
                chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0
    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))

# Testing third given case
# Reset all the lists back to empty
totalFit = 0
chanceList = []
letterList = {}
finalList = []

usedLetter = ['D', 'I', 'A']

# Calculate all words that fit evidence
for word in wordList:
    if 'D' in word[0][0] and 'D' not in word[0][1] and 'D' not in word[0][2]:
        if 'D' not in word[0][4] and 'I' in word[0][3] and 'I' not in word[0][1]:
            if 'I' not in word[0][2] and 'I' not in word[0][4] and 'A' not in word[0]:    
                totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    if 'D' in word[0][0] and 'D' not in word[0][1] and 'D' not in word[0][2]:
        if 'D' not in word[0][4] and 'I' in word[0][3] and 'I' not in word[0][1]:
            if 'I' not in word[0][2] and 'I' not in word[0][4] and 'A' not in word[0]:    
                chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0
    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))

          ###################
        ### Part b number 1 ###
          ###################
# Reset all the lists back to empty
totalFit = 0
chanceList = []
letterList = {}
finalList = []

usedLetter = []

# Calculate all words that fit evidence
for word in wordList:
    totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0
    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))

          ###################
        ### Part b number 2 ###
          ###################
# Reset all the lists back to empty
totalFit = 0
chanceList = []
letterList = {}
finalList = []

usedLetter = ['E', 'T']

# Calculate all words that fit evidence
for word in wordList:
    if 'E' in word[0] or 'T' in word[0] or ('E' and 'T' in word[0]):
        continue
    else:
        # Get total of all words that fit evidence
        totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    if 'E' in word[0] or 'T' in word[0] or ('E' and 'T' in word[0]):
        continue
    else:
        chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0

    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))

          ###################
        ### Part b number 3 ###
          ###################

# Reset all the lists back to empty
totalFit = 0
chanceList = []
letterList = {}
finalList = []

usedLetter = ['A', 'R']

# Calculate all words that fit evidence
for word in wordList:
    if 'A' in word[0][0] and 'A' not in word[0][1] and 'A' not in word[0][2]:
        if 'A' not in word[0][3] and 'R' in word[0][4] and 'R' not in word[0][1]:
            if 'R' not in word[0][2] and 'R' not in word[0][3]:    
                totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    if 'A' in word[0][0] and 'A' not in word[0][1] and 'A' not in word[0][2]:
        if 'A' not in word[0][3] and 'R' in word[0][4] and 'R' not in word[0][1]:
            if 'R' not in word[0][2] and 'R' not in word[0][3]:    
                chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0
    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))

          ###################
        ### Part b number 4 ###
          ###################

# Reset all the lists back to empty
totalFit = 0
chanceList = []
letterList = {}
finalList = []

usedLetter = ['A', 'R', 'E']

# Calculate all words that fit evidence
for word in wordList:
    if 'A' in word[0][0] and 'A' not in word[0][1] and 'A' not in word[0][2]:
        if 'A' not in word[0][3] and 'R' in word[0][4] and 'R' not in word[0][1]:
            if 'R' not in word[0][2] and 'R' not in word[0][3] and 'E' not in word[0]:    
                totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    if 'A' in word[0][0] and 'A' not in word[0][1] and 'A' not in word[0][2]:
        if 'A' not in word[0][3] and 'R' in word[0][4] and 'R' not in word[0][1]:
            if 'R' not in word[0][2] and 'R' not in word[0][3] and 'E' not in word[0]:    
                chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0
    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))


          ###################
        ### Part b number 5 ###
          ###################

# Reset all the lists back to empty
totalFit = 0
chanceList = []
letterList = {}
finalList = []

usedLetter = ['H', 'I', 'M', 'N', 'T']

# Calculate all words that fit evidence
for word in wordList:
    if 'H' not in word[0][0] and 'H' not in word[0][1] and 'H' in word[0][2]:
        if 'H' not in word[0][3] and'H' not in word[0][4] and 'I' not in word[0]:
            if 'M' not in word[0] and 'N' not in word[0] and 'T' not in word[0]:
                totalFit += int(word[1])

# Calculate P(W = w|E) using the totalFit as denominator
for word in wordList:
    if 'H' not in word[0][0] and 'H' not in word[0][1] and 'H' in word[0][2]:
        if 'H' not in word[0][3] and'H' not in word[0][4] and 'I' not in word[0]:
            if 'M' not in word[0] and 'N' not in word[0] and 'T' not in word[0]:
                chanceList.append([word[0], int(word[1])/totalFit])

for letter in ALPHABET:
    # Initialize dictionary to 0 for each letter
    letterList[letter] = 0
    # Make sure letter is not already used
    if letter not in usedLetter:
        # Summation on P(W = w|E) with the given letter
        for word in chanceList:
            if letter in word[0]:
                letterList[letter] += word[1]

    # Create a list to be able to sort with the letter and it's occurrence
    finalList.append([letter, letterList[letter]])

print(sorted(finalList, key = getFloat))

