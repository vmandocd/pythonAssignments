# Von Jhiro Mandocdoc
# A09999946
# 5/23/17

############# HW5.3 EM algorithm for binary matrix completion #############
import math

# Open given files and set to a variable
movieRatings    = [line.rstrip('\n') for line in open('hw5_movieRatings.txt')]
movieTitles     = [line.rstrip('\n') for line in open('hw5_movieTitles.txt')]
studentPIDs     = [line.rstrip('\n') for line in open('hw5_studentPIDs.txt')]
probRgivenZ     = [line.rstrip('\n') for line in open('hw5_probRgivenZ_init.txt')]
probZinit       = [line.rstrip('\n') for line in open('hw5_probZ_init.txt')]

# Initialize list for probability of Z
probZList = []
i = 0
while (i < len(probZinit)):
    probZList.append(probZinit[i])
    i += 1

# Variables for totals
totStudents = 258
totMovies   = 50

############ PART A ############

# Function to sort by number of occurrences
def getRatio(movieList):
    return float(movieList[1])

# List of total students who saw the movie
movieSeen   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

movieRec    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Get the total times a movie has been seen and recommended
for movie in movieTitles:
    for student in movieRatings:
        rating = student.split()
        i = 0
        while (i < 50):
            if (rating[i] == '1'):
                movieRec[i] += 1

            if (rating[i] == '0') or (rating[i] == '1'):
                movieSeen[i] += 1
            i += 1

movieRatio = []
i = 0
while (i < 50):
    ratio = float(movieRec[i]) / float(movieSeen[i])
    movieRatio.append([movieTitles[i], ratio])
    i += 1

sortedList = sorted(movieRatio, key = getRatio)
print(sortedList)

# ['The_Last_Airbender', 0.24166666666666667]
# ['Fifty_Shades_of_Grey', 0.29292929292929293]
# ['Magic_Mike', 0.45614035087719296]
# ['Prometheus', 0.5057471264367817]
# ['Man_of_Steel', 0.5193798449612403]
# ['World_War_Z', 0.5655737704918032]
# ['Room', 0.5909090909090909]
# ['Pitch_Perfect', 0.6428571428571429]
# ['Bridemaids', 0.6447368421052632]
# ['Fast_Five', 0.680327868852459]
# ['American_Hustle', 0.6833333333333333]
# ['Midnight_in_Paris', 0.6842105263157895]
# ['Jurassic_World', 0.7058823529411765]
# ['The_Hunger_Games', 0.7061611374407583]
# ['The_Great_Gatsby', 0.7204968944099379]
# ['Frozen', 0.7287234042553191]
# ['Thor', 0.7439024390243902]
# ['The_Perks_of_Being_a_Wallflower', 0.746031746031746]
# ['Iron_Man_2', 0.7547169811320755]
# ['Her', 0.7560975609756098]
# ['Mad_Max:_Fury_Road', 0.7580645161290323]
# ['Drive', 0.7681159420289855]
# ['The_Revenant', 0.7727272727272727]
# ['12_Years_a_Slave', 0.7796610169491526]
# ['Captain_America:_The_First_Avenger', 0.7989130434782609]
# ['The_Girls_with_the_Dragon_Tattoo', 0.8026315789473685]
# ['The_Hateful_Eight', 0.8113207547169812]
# ['Star_Wars:_The_Force_Awakens', 0.8125]
# ['Now_You_See_Me', 0.8211920529801324]
# ['Avengers:_Age_of_Ultron', 0.8273809523809523]
# ['Gone_Girl', 0.8279569892473119]
# ['The_Theory_of_Everything', 0.8375]
# ['Black_Swan', 0.8390804597701149]
# ['Ex_Machina', 0.8411214953271028]
# ['Harry_Potter_and_the_Deathly_Hallows:_Part_1', 0.8434343434343434]
# ['The_Martian', 0.8518518518518519]
# ['The_Avengers', 0.8551401869158879]
# ['The_Help', 0.86]
# ['Django_Unchained', 0.8604651162790697]
# ['Toy_Story_3', 0.8608247422680413]
# ['Wolf_of_Wall_Street', 0.8622754491017964]
# ['21_Jump_Street', 0.8701298701298701]
# ['Les_Miserables', 0.8737864077669902]
# ['Harry_Potter_and_the_Deathly_Hallows:_Part_2', 0.8783068783068783]
# ['The_Social_Network', 0.8881578947368421]
# ['X-Men:_First_Class', 0.8930817610062893]
# ['Interstellar', 0.8958333333333334]
# ['The_Dark_Knight_Rises', 0.9095477386934674]
# ['Shutter_Island', 0.9541284403669725]
# ['Inception', 0.967741935483871]
