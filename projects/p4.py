# Assignment 4: Bowling Scores
# Tiziana Rizzato
# 2/12/26
# sentinel-controlled loop to determine high, low, average
# bowling scores

# variables 

min = 301
max = -1
numberBowlers = 0
totalScore = 0

#input

scoreNumber = 1 
print( "Enter score (-1 to quit) ") 
n = int  ( input() )


# processing 

while n != -1:
    if n < 0 or n > 300:
        print( "Invalid score, Expecting 0-300" )
    else: 
        numberBowlers += 1
        totalScore += n

        if n > max:
            max = n
        if n < min:
            min = n

    scoreNumber += 1

# repeat input

    print("Enter value (-1 to quit)")
    n = int( input() )

# calculate average

if numberBowlers > 0:
    avg = totalScore / numberBowlers
else:
    avg = 0
    min = 0
    max = 0

  
# Output
print()
print(f"Number of Bowlers: {numberBowlers}")
print(f"High Score: {max}")
print(f"Low Score: {min}")
print(f"Avg Score: {avg:.2f}")