def scoreTosses(numPlayers, tosses):
    # Write your code here
    # A or R = 1
    # O or G = 3 
    # B = 6
    # Space in between = sum of both + 1
    # Toss with "+" at end is +2
    # format in "player#-score"
    answer = ""
    playerList = []
    scoreList = []
    tossesList = []
    for player in range(1, numPlayers + 1): # Iterate through all players
        tempScore = 0
        roundScore = tosses[player-1].split(" ")
        # Finds point values
        for score in roundScore: # Iterate through each round's score
            for char in score:
                if(char == "A" or char == "R"):
                    tempScore += 1
                elif(char == "O" or char == "G"):
                    tempScore += 3
                elif(char == "B"):
                    tempScore += 6
                elif(char == "+"):
                    tempScore += 2
            if(len(score) > 1 and score[0].isalpha() and score[1].isalpha()): 
                tempScore += 1
        # Sorts the points
        if(not scoreList): # Check if scoreList empty
            scoreList.append(tempScore)
            playerList.append(player)
            tossesList.append(len(roundScore))
        else:
            done = False
            for index in range(len(scoreList)): 
                if(tempScore > scoreList[index]):
                    scoreList.insert(index, tempScore)
                    playerList.insert(index, player)
                    tossesList.insert(index, len(roundScore))
                    done = True
                    break
            if(not done):
                scoreList.append(tempScore)
                playerList.append(player)
                tossesList.append(len(roundScore)) 

    
    print(scoreList)
    print(playerList)
    print(tossesList)
    
    # Tiebreakers
    for i in range(len(playerList)-1):
        if(scoreList[i] == scoreList[i+1] and tossesList[i] > tossesList[i+1]):
            tScore = scoreList[i]
            tPlayer = playerList[i]
            tTosses = tossesList[i]
            
            scoreList[i] = scoreList[i+1]
            playerList[i] = playerList[i+1]
            tossesList[i] = tossesList[i+1]
            scoreList[i+1] = tScore
            playerList[i+1] = tPlayer
            tossesList[i+1] = tTosses
            
            
    
    for i in range(numPlayers):
        answer += f'{playerList[i]}-{scoreList[i]} '
    return answer
    
    # Good luck understanding this code
