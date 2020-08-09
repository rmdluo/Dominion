from InvVilLabChapVSVilAmb import SingleGame
import statistics

NUM_RUNS = 10000

wins1 = 0
wins2 = 0

totalPoints1 = 0
totalPoints2 = 0

points1 = []
points2 = []

totalMarginOfVictory1 = 0
totalMarginOfVictory2 = 0

marginOfVictories1 = []
marginOfVictories2 = []

totalSilver1 = 0
totalSilver2 = 0

silvers1 = []
silvers2 = []

totalTurnGold1 = 0
totalTurnGold2 = 0

turnGolds1 = []
turnGolds2 = []

totalGameLength = 0
gameLengths = []

for number in range(NUM_RUNS):
    game = SingleGame()
    game.simulateRun()

    p1Score = game.numProvinces1 * 6 + game.numDuchies1 * 3 + game.numEstate1 - game.numCurse1
    #p1Score = int((len(game.deck1) + len(game.discard1) + len(game.hand1)) / 10) * game.numGarden1 + game.numEstate1
    totalPoints1 += p1Score
    points1.append(p1Score)

    p2Score = game.numProvinces2 * 6 + game.numDuchies2 * 3 + game.numEstate2 - game.numCurse2
    totalPoints2 += p2Score
    points2.append(p2Score)

    if(p1Score > p2Score):
        wins1 += 1
        totalMarginOfVictory1 += (p1Score - p2Score)
        marginOfVictories1.append(p1Score - p2Score)
    elif(p1Score < p2Score):
        wins2 += 1
        totalMarginOfVictory2 += (p2Score - p1Score)
        marginOfVictories2.append(p2Score - p1Score)

    totalSilver1 += game.numSilver1
    totalSilver2 += game.numSilver2

    silvers1.append(game.numSilver1)
    silvers2.append(game.numSilver2)

    totalTurnGold1 += game.turnGold1
    totalTurnGold2 += game.turnGold2
    
    turnGolds1.append(game.turnGold1)
    turnGolds2.append(game.turnGold2)

    totalGameLength += int((game.turnNumber / 2))
    gameLengths.append(int((game.turnNumber / 2)))

    #totalVillage1 += game.numVillage1
    #totalVillage2 += game.numVillage2

    #totalInventor1 += game.numInventor1

print("Player 1 Winrate: " + str(wins1 / NUM_RUNS))
print("Player 2 Winrate: " + str(wins2 / NUM_RUNS))

print("Player 1 Average Points: " + str(totalPoints1 / NUM_RUNS))
print("Player 2 Average Points: " + str(totalPoints2 / NUM_RUNS))

print("Player 1 Points Standard Deviation: " + str(statistics.stdev(points1)))
print("Player 2 Points Standard Deviation: " + str(statistics.stdev(points2)))

print("Player 1 Average Margin of Victory: " + str(totalMarginOfVictory1 / NUM_RUNS))
print("Player 2 Average Margin of Victory: " + str(totalMarginOfVictory2 / NUM_RUNS))

print("Player 1 Margin of Victory Standard Deviation: " + str(statistics.stdev(marginOfVictories1)))
print("Player 2 Margin of Victory Standard Deviation: " + str(statistics.stdev(marginOfVictories2)))

print("Player 1 Average Silvers: " + str(totalSilver1 / NUM_RUNS))
print("Player 2 Average Silvers: " + str(totalSilver2 / NUM_RUNS))

print("Player 1 Silvers Standard Deviation: " + str(statistics.stdev(silvers1)))
print("Player 2 Silvers Standard Deviation: " + str(statistics.stdev(silvers2)))

print("Player 1 Average Turn for First Gold: " + str(totalTurnGold1 / NUM_RUNS))
print("Player 2 Average Turn for First Gold: " + str(totalTurnGold2 /   NUM_RUNS))

print("Player 1 Turn for First Gold Standard Deviation: " + str(statistics.stdev(turnGolds1)))
print("Player 2 Turn for First Gold Standard Deviation: " + str(statistics.stdev(turnGolds2)))

print("Average Game Length: " + str(totalGameLength / NUM_RUNS))
print("Game Length Standard Deviation: " + str(statistics.stdev(gameLengths)))

