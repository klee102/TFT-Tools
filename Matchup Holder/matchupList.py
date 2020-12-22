#With 7 other players alive, you will not revisit the last 4 you have faced.
#With 6 others alive, the last 3.
#With 5 others alive, the last 2.
#With 4 or 3 others alive, you will not visit the last player you faced.

#When someone is eliminated, the match history is reset, so you can fight anyone.

#Ghosts act as "empty" players, meaning you can play the actual version of the ghost you just fought.

playerList = ["A", "B", "C", "D", "E", "F", "G"]

#the key represents how many other players are alive
#the value for the key represents who you cannot play again (aka length of match history)
possiblePlayerCount = {7:4, 6:3, 5:2, 4:1, 3:1}
otherPlayersAlive = 7
matchHistory = ["B", "F"]

def updateMatchHistory(player):
    global otherPlayersAlive
    global matchHistory
    global playerList
    global possiblePlayerCount

    matchHistory.append(player)

    #check players alive to determine length of match history
    #pop the first (oldest) entry if the length of the list is too long
    #it's too long if the number of others alive 

    if len(matchHistory) > possiblePlayerCount[otherPlayersAlive]:
        matchHistory.pop(0)

    return matchHistory

def eliminatePlayer(player):
    global otherPlayersAlive
    global matchHistory
    global playerList
    global possiblePlayerCount

    otherPlayersAlive -= 1
    playerList.remove(player)
    matchHistory = []
    
    return matchHistory