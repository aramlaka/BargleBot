import random
import numpy as np
import pprint as pp


def calc(epochs, initialBet):
    net = []

    for i in range(50):
        bet = (i * initialBet) + initialBet
        net.append(-50)
        chicken = .5
        wins = 0
        superChicken = False
        dumbChickenCount = 0
        superChickenCount = 0
        winStreak = 0
        winStreaks = 0
        bestWinStreak = 0
        winStreakCount = 0
        lossStreak = 0
        lossStreaks = 0
        worstLossStreak = 0
        lossStreakCount = 0

        for j in range(epochs - 1):
            net[i] -= bet

            if chicken >= random.random():
                net[i] += bet * 2
                wins += 1
                winStreak += 1

                if lossStreak > worstLossStreak:
                    worstLossStreak = lossStreak

                if lossStreak:
                    lossStreaks += lossStreak
                    lossStreak = 0
                    lossStreakCount += 1

                if chicken < .7:
                    chicken += .01
                elif not superChicken:
                    superChicken = True
                    superChickenCount += 1
            else:
                dumbChickenCount += 1
                lossStreak += 1

                if winStreak > bestWinStreak:
                    bestWinStreak = winStreak

                if winStreak:
                    winStreaks += winStreak
                    winStreak = 0
                    winStreakCount += 1

                net[i] -= 50
                chicken = .5
                superChicken = False

        net[i] = (bet, net[i] / epochs, wins / epochs, winStreaks / winStreakCount, bestWinStreak,
                  lossStreaks / lossStreakCount, worstLossStreak, superChickenCount)

    return net


def strategy(epochs, initialBet, strat):
    net = []

    for i in range(50):
        net.append(-50)
        chicken = .5

        for j in range(epochs - 1):
            if chicken >= strat:
                bet = (i * initialBet) + initialBet
            else:
                bet = 100

            net[i] -= bet

            if chicken >= random.random():
                net[i] += bet * 2

                if chicken < .7:
                    chicken += .01
            else:
                net[i] -= 50
                chicken = .5

        bet = (i * initialBet) + initialBet
        net[i] = (bet, net[i] / epochs)

    return net

def strategy_divison(epochs, initialBet, divisor):
    net = []

    for i in range(50):
        bet = (i * initialBet) + initialBet
        net.append(-50)
        chicken = .5
        wins = 0
        superChicken = False
        dumbChickenCount = 0
        superChickenCount = 0
        winStreak = 0
        bestWinStreak = 0
        lossStreak = 0
        worstLossStreak = 0

        for j in range(epochs - 1):
            if chicken >= .51:
                bet = (i * initialBet) + initialBet
            else:
                bet /= divisor

            net[i] -= bet

            if chicken >= random.random():
                net[i] += bet * 2
                wins += 1
                winStreak += 1

                if lossStreak > worstLossStreak:
                    worstLossStreak = lossStreak

                lossStreak = 0

                if chicken < .7:
                    chicken += .01
                elif not superChicken:
                    superChicken = True
                    superChickenCount += 1
            else:
                dumbChickenCount += 1
                lossStreak += 1

                if winStreak > bestWinStreak:
                    bestWinStreak = winStreak

                winStreak = 0
                net[i] -= 50
                chicken = .5
                superChicken = False

        bet = (i * initialBet) + initialBet
        net[i] = (bet, net[i] / epochs, wins / epochs, bestWinStreak, worstLossStreak, superChickenCount)

    return net


pp.pprint(strategy(1000000, 100, .50))
