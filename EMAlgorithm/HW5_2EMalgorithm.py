# Von Jhiro Mandocdoc
# A09999946
# 5/23/17

############# HW5.2 EM algorithm for noisy-OR #############
import math

# Open given files and set to a variable
noisyOrX    = [line.rstrip('\n') for line in open('hw5_noisyOr_x.txt')]
noisyOrY    = [line.rstrip('\n') for line in open('hw5_noisyOr_y.txt')]
noisyOrZip  = zip(noisyOrY, noisyOrX)
noisyOr     = list(noisyOrZip)

# Variables for totals
totData         = 267
totInput        = 23
totMistake      = 0
totSum          = 0
mistakeCheck    = 0.5

# Create list to hold probabilities (size 23)
probList = [1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 
        1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23, 1/23,
        1/23, 1/23, 1/23]

newProbList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0]

# Create list to hold Xi = 1 columns (size 23)
columnXList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0]

############ Start of functions ############

# Calculates P(Y=yt|X)
def probY(Y, X):
    global totMistake
    xList = X.split()

    # Case for Y = 1
    if int(Y) == 1:
        product = 1
        i = 0
        while (i < 23):
            productX = (1 - probList[i]) ** int(xList[i])
            product = product * productX
            i += 1

        answer = 1 - product
        if ((float(answer) <= mistakeCheck)):
            totMistake += 1

    # Case for Y = 0
    else:
        product = 1
        i = 0
        while(i < 23):
            productX = (1 - probList[i]) ** int(xList[i])
            product = product * productX
            i += 1

        answer = product
        if ((float(1 - answer) >= mistakeCheck)):
            totMistake += 1
    return answer

# Calculates denominator for EM update, similar to P(Y=yt|X)
def probCalc(Y, X):
    xList = X.split()

    product = 1
    i = 0
    while (i < 23):
        productX = (1 - probList[i]) ** int(xList[i])
        product = product * productX
        i += 1
    answer = 1 - product

    return answer

# Calculates EM update
def probUpdate(Y, X, number):
    xList = X.split()

    numerator   = int(Y) * int(xList[number]) * probList[number]
    denominator = probCalc(Y, X)
    answer = numerator / denominator

    return answer

############ End of functions ############

# Get the log likelihood 0th iteration
for pair in noisyOr:
    xiCount = pair[1].split()
    i = 0

    while(i < 23):
        # Check if Xi = 1, then increment if so
        if(int(xiCount[i]) == 1):
            columnXList[i] += 1
        i += 1

    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

denom   = 1 / totData
logLike = denom * totSum

print(logLike)
print(totMistake)

# EM Update
updateSum = 0
i = 0
while (i < 23):
    for pair in noisyOr:
        updateSum += probUpdate(pair[0], pair[1], i)
    newProbList[i] = updateSum * (1 / columnXList[i])
    updateSum = 0
    i += 1

i = 0
while(i < 23):
    probList[i] = newProbList[i]
    i += 1

# Get the log likelihood 1st iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

# EM Update
updateSum = 0
i = 0
while (i < 23):
    for pair in noisyOr:
        updateSum += probUpdate(pair[0], pair[1], i)
    newProbList[i] = updateSum * (1 / columnXList[i])
    updateSum = 0
    i += 1

i = 0
while(i < 23):
    probList[i] = newProbList[i]
    i += 1

# Get the log likelihood 2nd iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 2):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 4th iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 4):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 8th iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 8):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 16th iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 16):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 32nd iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 32):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 64th iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 64):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 128th iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 128):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 256th iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)

j = 0
while (j < 256):
    
    # EM Update
    updateSum = 0
    i = 0
    while (i < 23):
        for pair in noisyOr:
            updateSum += probUpdate(pair[0], pair[1], i)
        newProbList[i] = updateSum * (1 / columnXList[i])
        updateSum = 0
        i += 1

    i = 0
    while(i < 23):
        probList[i] = newProbList[i]
        i += 1

    j += 1

# Get the log likelihood 512th iteration
totSum = 0
totMistake = 0
for pair in noisyOr:
    answer = float(probY(pair[0], pair[1]))
    totSum += math.log(answer)

logLike = denom * totSum

print(logLike)
print(totMistake)
print(probList)

# Final probability list
# [7.951298074783526e-05, 0.004805593266871094, 2.564954364606272e-11, 0.265342245
# 3219639, 1.4900159194829788e-05, 0.009460384842582862, 0.24030258818485023, 0.11
# 345097039229, 0.00014364884280306808, 0.5234830841457545, 0.40728941117197065, 9
# .056390314004321e-08, 0.6157965584626918, 5.960212153820985e-06, 0.0448268047645
# 9009, 0.5899815727520106, 0.9999999999999936, 0.9999999820161173, 4.153980293009
# 163e-09, 0.46299324926223895, 0.35319815567445734, 0.5248658159861825, 0.1947579
# 3547097206] 
