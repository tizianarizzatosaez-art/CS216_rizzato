import random

# p3.py
# spring 2026
# Tiziana Rizzato
# 2/3/2026
# Chutes and Ladders
# 1. Begin by updating the functions to play a two person game
#    Do not modify the processTurn function
# 2. Update the main logic to create a four player game


# get a random spin between 1 and 6
def getSpin():
    import random
    number = random.randint(1,6)
    return number

# define ladders and chutes positions
def offBoard( N ):
    result = N
    if N < 1 or N > 100:
        result = True 
    else:
        result = False
    return result

# define winning position
def gameWon( N ):
    result = N
    if N == 100:
        result = True 
    else:
        result = False
    return result

# define bottom of ladder positions
def isLadder( N ):
    result = False
    if N == 1:
        result = True
    if N == 4:
        result = True
    if N == 9:
        result = True
    if N == 21:
        result = True
    if N == 28:
        result = True
    if N == 36:
        result = True
    if N == 51:
        result = True
    if N == 71:
        result = True
    if N == 80:
        result = True
    return result
    
# define top of chute positions
def isChute( N ):
    result = False
    if N == 16:
        result = True
    if N == 47:
        result = True
    if N == 49:
        result = True
    if N == 56:
        result = True
    if N == 62:
        result = True
    if N == 64:
        result = True
    if N == 87:
        result = True
    if N == 93:
        result = True
    if N == 95:
        result = True
    if N == 98:
        result = True
    return result 
  

# define bottom of ladders
def upLadder( N ):
    result = N
    if N == 1:
        result = 38
    elif N == 4:
        result = 14
    elif N == 9:
        result = 31
    elif N == 21:
        result = 42
    elif N == 28:
        result = 84
    elif N == 36:
        result = 44
    elif N == 51:
        result = 67
    elif N == 71:
        result = 91
    elif N == 80:
        result = 100
    
    return result
    
# define top of chutes
def downChute( N ):
    result = N
    if N == 16:
        result = 6
    elif N == 47:
        result = 26
    elif N == 49:
        result = 11
    elif N == 56:
        result = 53
    elif N == 62:
        result = 19
    elif N == 64:
        result = 60
    elif N == 87:
        result = 24
    elif N == 93:
        result = 73
    elif N == 98:
        result = 78
    elif N == 95:
        result = 75

    return result

# *** do not modify processTurn **
def processTurn( player, position ):
    
    spin = getSpin()
    
    print(f"{player} Spin = {spin}".format(player, spin))
    
    nextPosition = position + spin
    
    if isLadder( nextPosition ) == True:
        endingPosition = upLadder( nextPosition )
        print( f"{player} Up ladder at {nextPosition} to {endingPosition}".format( player, nextPosition, endingPosition ) )            
        position = endingPosition

    elif isChute( nextPosition ) == True:
        endingPosition = downChute( nextPosition )
        print( f"{player} Down chute at {nextPosition} to {endingPosition}" )            
        position = endingPosition
    
    elif offBoard( nextPosition ) == True:
        print( " Off board, try again ..." )
               
    else:
        print( f"{player} Move to {nextPosition}" )
        position = nextPosition
    
    if gameWon(position):
        print()
        print( f"Game Over ... Congratulations {player}, you Win!!!" )

    return position


# *** main game logic ***
if __name__ == "__main__":

    #random.seed( -1 () #can set number to get same random numbers
        
    
    print ("Enter player 1 name: " )
    player1 = input( )

    print( "Enter player 2 name: " )
    player2 = input( )

    print( "Enter player 3 name: " )
    player3 = input( )

    print( "Enter player 4 name: " )
    player4 = input( )

    
    print()
    
    player1Position = 0
    player2Position = 0
    player3Position = 0
    player4Position = 0
    
    gameOver = False
    while gameOver != True:
        
        player1Position = processTurn( player1, player1Position )
        gameOver = gameWon( player1Position )
        
        if gameOver != True:
            player2Position = processTurn( player2, player2Position )
            gameOver = gameWon( player2Position )

        if gameOver != True:
            player3Position = processTurn( player3, player3Position )
            gameOver = gameWon( player3Position )
        
        if gameOver != True:
            player4Position = processTurn( player4, player4Position )
            gameOver = gameWon( player4Position )
        #while loop

            
               