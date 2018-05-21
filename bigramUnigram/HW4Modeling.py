# Von Jhiro Mandocdoc
# A09999946
# 5/09/17

################### HW4.4 Language Modeling ###################
import math
import matplotlib.pyplot as plt

vocab = [line.rstrip('\n') for line in open('vocab.txt')]
unigram = [line.rstrip('\n') for line in open('unigram.txt')]
bigram = [line.rstrip('\n') for line in open('bigram.txt')]

# Important variables
uniSum = 0      # Unigram sum of all words
vocabList = []  # List to hold vocab words and line number

# Local variables
i = 1           # Count for the words and corresponding line number
dummyList = []  # Stores all valid word/line number pairs    

# Iterate through vocab to get words and line number
for word in vocab:
    vocabList.append([word, i])
    i += 1

# Get sum of all word counts
for num in unigram:
    uniSum += int(num)

################### PART A ###################

# Find all words that start with 'M'
for pair in vocabList:
    if 'M' in pair[0][0]:
        dummyList.append(pair)

# From the list with valid words, get ML estimate unigram dist
for pair in dummyList:
    # Reset i on each iteration of pair
    i = 1
    for line in unigram:
        if i == pair[1]:
            print(pair[0], line)
            print(int(line) / uniSum)
        i += 1

################### PART B ###################

# Reset local variables
oneTotal = 0    # Count for bigram probabilties of words following 'ONE'
i = 1           # Count for the words and corresponding line number
dummyList = []  # Stores all valid word/line number pairs    
followList = [] # Stores line numbers and count of words that follow 'ONE'
trackList = []  # Stores list of word and probability

# Function to sort by number of occurrences
def getWordCount(wordList):
    return float(wordList[1])

# Find index of string 'ONE' and put into dummyList
for pair in vocabList:
    if 'ONE' == pair[0]:
        dummyList.append(pair)

# Search bigram for top 10 words that follow 'ONE'
for pair in dummyList:
    for line in bigram:
        lineSplit = line.split()
        if pair[1] == int(lineSplit[0]):
            followList.append([lineSplit[1], lineSplit[2]])
            oneTotal += int(lineSplit[2])    # Update oneTotal

# Replace the line number of word with the actual word from vocab list
for word in vocabList:
    for pair in followList:
        if int(pair[0]) == int(word[1]):
            bigramProb = int(pair[1]) / int(oneTotal)
            trackList.append([word[0], bigramProb])

# Sort by bigram probabilities
sortedList = sorted(trackList, key = getWordCount, reverse = True)
mostFreqList = [sortedList[0], sortedList[1], sortedList[2], sortedList[3],
        sortedList[4], sortedList[5], sortedList[6], sortedList[7],
        sortedList[8], sortedList[9]]

print("Most frequent words are: ", mostFreqList ,'\n')

################### PART C ###################

# Reset local variables
uniProb = 1     # Probability for unigrams for the sentence given
biProb = 1      # Probability for bigrams for the sentence given
biTotal = 0     # Total count that word is followed by another word
i = 1           # Count for the words and corresponding line number
dummyList = []  # Stores all valid word/line number pairs    
indexList = []  # Stores line number of the word for text files

# Create a list of all indexes that will be used for line number
for word in vocabList:
    if 'THE' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'MARKET' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'FELL' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'BY' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'ONE' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'HUNDRED' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'POINTS' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'LAST' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'WEEK' == word[0]:
        indexList.append(word[1])

print("Index List: ", indexList)

# Multiply all probabilities together
for index in indexList:
    i = 1
    for count in unigram:
        if i == index:
            uniProb = uniProb * (int(count) / uniSum)
        i += 1

natLog = math.log(uniProb)
print(natLog)

# Create list that now include <s>
biIndexList = [2] + indexList
biCheck = len(biIndexList)      # Will check if all numbers were checked
i = 1

while(len(biIndexList) != 1):
    biTotal = 0

    # Calculate total times word is followed
    for line in bigram:
        lineSplit = line.split()
        if int(lineSplit[0]) == int(biIndexList[0]):
            biTotal += float(lineSplit[2])

    # Calculate probabilities
    for line in bigram:
        lineSplit = line.split()
        if int(lineSplit[0]) == int(biIndexList[0]):
            if int(lineSplit[1]) == int(biIndexList[1]):
                print(lineSplit[0], lineSplit[1])
                i += 1
                biProb = float(biProb) * (float(lineSplit[2]) / float(biTotal))

    biIndexList.pop(0)
    print(biIndexList)

if i != biCheck:
    biProb = 0
    print("biProb is undefined\n")
else:
    natLog = math.log(biProb)
    print(natLog, '\n')

################### PART D ###################

# Reset local variables
uniProb = 1     # Probability for unigrams for the sentence given
biProb = 1      # Probability for bigrams for the sentence given
biTotal = 0     # Total count that word is followed by another word
i = 1           # Count for the words and corresponding line number
dummyList = []  # Stores all valid word/line number pairs    
indexList = []  # Stores line number of the word for text files

# Part E variables
# Create a list to hold all probabilities using Pm formula
uniProbList = []
biProbList = []

# Create a list of all indexes that will be used for line number
for word in vocabList:
    if 'THE' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'FOURTEEN' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'OFFICIALS' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'SOLD' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'FIRE' == word[0]:
        indexList.append(word[1])
for word in vocabList:
    if 'INSURANCE' == word[0]:
        indexList.append(word[1])

print("Index List: ", indexList)

# Multiply all probabilities together
for index in indexList:
    i = 1
    for count in unigram:
        if i == index:
            prob = int(count) / uniSum
            uniProb = uniProb * float(prob)
            uniProbList.append([index, float(prob)])
        i += 1

natLog = math.log(uniProb)
print(natLog)

# Create list that now include <s>
biIndexList = [2] + indexList

biCheck = len(biIndexList)   # Will check if all numbers were checked
i = 1

while(len(biIndexList) != 1):

    # Calculate total times word is followed
    for line in bigram:
        lineSplit = line.split()
        if int(lineSplit[0]) == int(biIndexList[0]):
            biTotal += int(lineSplit[2])

    # Calculate probabilities
    for line in bigram:
        lineSplit = line.split()
        if int(lineSplit[0]) == int(biIndexList[0]):
            if int(lineSplit[1]) == int(biIndexList[1]):
                print(lineSplit[0], lineSplit[1])
                i += 1
                prob = float(lineSplit[2]) / float(biTotal)
                biProb = float(biProb) * float(prob)
                biProbList.append([[lineSplit[0], lineSplit[1]], float(prob)])

    biIndexList.pop(0)
    print(biIndexList)

if i != biCheck:
    biProb = 0
    print("biProb is undefined\n")
else:
    natLog = math.log(biProb)
    print(natLog, '\n')

################### PART E ###################

lambdaList = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 
        0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20,
        0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30,
        0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.40,
        0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.50,
        0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.60,
        0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70,
        0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80,
        0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90,
        0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]

# Recreate the index list for bigrams
biIndexList = [2] + indexList

# Add the missing pairs with probabilities 0
biProbList.append([[148, 134], 0])
biProbList.append([[500, 444], 0])

# Probability list for Pm
probList = []

# Get the probability of Pm for each word | word
for lam in lambdaList:
    for biLine in biProbList:
        for uniLine in uniProbList:
            if int(biLine[0][1]) == int(uniLine[0]):
                pm1 = (float(1) - float(lam)) * float(uniLine[1])
                pm2 = float(lam) * float(biLine[1])
                pm = float(pm1) + float(pm2)
                probList.append([float(lam), float(pm)])

# Separate based on lambda given
finalList = []
for lam in lambdaList:
    total = 1
    num = 0
    for probLine in probList:
        if float(lam) == float(probLine[0]):
            total = float(total) * float(probLine[1])
            num += 1
         if num == 5:
            logTotal = math.log(float(total))
            finalList.append([float(lam), float(logTotal)])

def getWordCount2(wordList):
    return float(wordList[1])

sortedList = sorted(finalList, key = getWordCount2, reverse = True)
print(sortedList[0])

# Grab only the values resulting from the lambda
displayList = []
for line in finalList:
    displayList.append(line[1])

plt.plot(lambdaList, displayList)
plt.show()
