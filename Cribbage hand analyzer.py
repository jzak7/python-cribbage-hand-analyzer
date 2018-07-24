#Cribbage hand analyzer
#ZG Fabry June 2017


import random
from itertools import combinations
import sys
import time


runAgain = True

print('''Welcome to the cribbage hand analyzer.
Please enter a 4, 5, or 6 card hand, or type 'instructions' or 'quit'. ''')
print()


def showInstructions():
    print('''Instructions:
    Enter a cribbage hand, separated by spaces.  For instance,
    if you want to determine which 4-card hand has the expected value
    from the hand containing the Ace of Hearts, the 4 of Diamonds,
    the Jack of Clubs, the 5 of Spades, the 6 of Hearts,
    and the 7 of Clubs, you would enter 'Ah 4d Jc 5s 6h 7c'.

    Entering a 4-card hand returns the expected value of the hand.

    Type 'quit' to exit the program.

    Press enter to continue.''')
    input()
    print()

   
    



def enterHand(): #lets the user enter an n-card hand, returns an n-item list
    startingHand = input('Hand: ')
    startingHand = startingHand.split()
      
    if startingHand == []:
        print('Please enter a 4, 5, or 6 card hand.')
        print()
        startingHandvalidHandList = [startingHand, False]
        return startingHandvalidHandList
    if startingHand[0].lower().startswith('i'):
        showInstructions()
    if startingHand == ['quit'] or startingHand == ['Quit'] or startingHand == ['QUIT'] or startingHand == ['QUit'] or startingHand == ['QUIt'] or startingHand == ['quiT']:
        print('Goodbye!')
        time.sleep(.75)
        sys.exit()
    if len(startingHand) < 4 or len(startingHand) > 6:
        print('Please enter a 4, 5, or 6 card hand.')
        print()
        startingHandvalidHandList = [startingHand, False]
        return startingHandvalidHandList
    elif len(startingHand) >= 4 and len(startingHand) <= 6:
        validHandList = []
        for r in range(len(startingHand)):
            if len(startingHand[r]) == 3:
                first = startingHand[r][0]
                middle = startingHand[r][1]
                last = startingHand[r][len(startingHand[r])-1]
                first = first.upper()
                last = last.lower()
                #print(first)
                #print(last)
                startingHand[r] = first + middle + last

            else:       
                first = startingHand[r][0]
                last = startingHand[r][len(startingHand[r])-1]
                first = first.upper()
                last = last.lower()
                #print(first)
                #print(last)
                startingHand[r] = first + last
            if startingHand[r] in cardNumVal:
                validHandList.append(1)
        if sum(validHandList) == len(startingHand):
            print('Starting Hand: ', startingHand)
            startingHandvalidHandList = [startingHand, True]
            return startingHandvalidHandList  #need to return both startingHand and 'True'
            
        else:
            print("I'm sorry, it looks like you've entered something I don't recognize.")
            print()
            startingHandvalidHandList = [startingHand, False]
            return startingHandvalidHandList

def scorePairs(handList):  #scores the pairs in each hand
    listOfPossiblePairs = list(combinations(handList, 2))
    pairs = []
    for i in range(len(listOfPossiblePairs)):
        if listOfPossiblePairs[i][0][0] == listOfPossiblePairs[i][1][0]:
            pairs.append(listOfPossiblePairs[i])
    #print(pairs)
    numberOfPairs = len(pairs)
    pairsScore = 2*numberOfPairs
    #print(pairsScore)
    handScoreList.append(pairsScore)



#Get all the possible combinations of the 4 cards, excluding single cards, to help check for 15s
def getAllCombinations(handList):
    listOfCombinations = []
    for i in range(2, len(handList) + 1):
        x = list(combinations(handList, i))
        for r in range(len(x)):
            listOfCombinations.append(x[r])
    return listOfCombinations




def scoreFifteens(handList): #score the 15s in each hand
    fifteensList = []
    for r in range(len(combinationsList)):
        numValList = []
        for i in range(len(combinationsList[r])):
            numValList.append(cardNumVal[combinationsList[r][i]])
        #print(numValList)
        combinationSum = sum(numValList)
        if combinationSum == 15:
            fifteensList.append(combinationsList[r])
        #print(fifteensList)
        numberOfFifteens = len(fifteensList)
        fifteensScore = 2*numberOfFifteens
    #print(fifteensScore)
    handScoreList.append(fifteensScore)




def scoreNobs(handList): #scores Nobs
    #print(handList)
    deletedCard = handList[4]
    del handList[4]
    #print('Original 4 card hand ', handList)
    
    if 'Jh' in handList and starter[len(starter)-1] == 'h':
        nobsScore = 1
    elif 'Jd' in handList and starter[len(starter)-1] == 'd':
        nobsScore = 1
    elif 'Jc' in handList and starter[len(starter)-1] == 'c':
        nobsScore = 1
    elif 'Js' in handList and starter[len(starter)-1] == 's':
        nobsScore = 1
    else:
        nobsScore = 0
    #print(nobsScore)
    handScoreList.append(nobsScore)
    handList.append(deletedCard)



def scoreFlush(handList):  #scores a flush if it exists; if you want to run this program for the crib, just comment out the 2 lines about 4-card flushes
    if handList[0][len(handList[0])-1] == handList[1][len(handList[1])-1] == handList[2][len(handList[2])-1] == handList[3][len(handList[3])-1] == handList[4][len(handList[4])-1]:
        flushScore = 5
    elif handList[0][len(handList[0])-1] == handList[1][len(handList[1])-1] == handList[2][len(handList[2])-1] == handList[3][len(handList[3])-1]:
        flushScore = 4
    else:
        flushScore = 0
    #print(flushScore)
    handScoreList.append(flushScore)





def scoreRuns(handList):
    #check for a 5 card run
    fiveList1stChars = []
    for i in range(len(handList)):
        for r in range(len(cardOrderTuplesList)):
            if handList[i][0] == cardOrderTuplesList[r][0]:
                fiveList1stChars.append(cardOrderTuplesList[r])
    
    sorted5List = sorted(fiveList1stChars,key=lambda x: x[1]) #fiveList1stChars.sort(key=lambda x: x[1])
    sorted5List2 = []
    #print(sorted5List)
    for l in range(len(sorted5List) - 1):
        if sorted5List[l][1] + 1 == sorted5List[l+1][1]:  #need some way to check if each iteration is true, not just check whether one is true each time
            sorted5List2.append(sorted5List[l])                                        #possibly by modifying or creating a new list?

    #print(sorted5List2)
    if len(sorted5List2) == 4:
        totalRunScore = 5
        handScoreList.append(totalRunScore)
        #print(totalRunScore)
    else:
        #move into scoring the 4 card runs here
        listOf4CardCombos = list(combinations(handList, 4))
        #print(listOf4CardCombos)
        runScoreList = []
        for r in range(len(listOf4CardCombos)):
            fourList = list(listOf4CardCombos[r])
            fourList1stChars = []
            for l in range(len(fourList)):
                for r in range(len(cardOrderTuplesList)):
                    if fourList[l][0] == cardOrderTuplesList[r][0]:
                        fourList1stChars.append(cardOrderTuplesList[r])

            sorted4List = sorted(fourList1stChars,key=lambda x: x[1])
            sorted4List2 = []

            for l in range(len(sorted4List) - 1):
                if sorted4List[l][1] + 1 == sorted4List[l+1][1]:
                    sorted4List2.append(sorted4List[l])

            if len(sorted4List2) == 3:
                runScore = 4
                runScoreList.append(runScore)

        #print(runScoreList)
        if len(runScoreList) > 0:
            totalRunScore = sum(runScoreList)
            handScoreList.append(totalRunScore)
            #print(totalRunScore)

        else:
            listOf3CardCombos = list(combinations(handList, 3))
            for r in range(len(listOf3CardCombos)):
                threeList = list(listOf3CardCombos[r])
                threeList1stChars = []
                for l in range(len(threeList)):
                    for r in range(len(cardOrderTuplesList)):
                        if threeList[l][0] == cardOrderTuplesList[r][0]:
                            threeList1stChars.append(cardOrderTuplesList[r])

                sorted3List = sorted(threeList1stChars,key=lambda x: x[1])
                sorted3List2 = []
        
            
                for l in range(len(sorted3List) - 1):
                    if sorted3List[l][1] + 1 == sorted3List[l+1][1]:
                        sorted3List2.append(sorted3List[l])

                if len(sorted3List2) == 2:
                    runScore = 3
                    runScoreList.append(runScore)

            if len(runScoreList) > 0:
                totalRunScore = sum(runScoreList)
                handScoreList.append(totalRunScore)
                #print(totalRunScore)

            else:
                totalRunScore = 0
                handScoreList.append(totalRunScore)
                #print(totalRunScore)
                
            
        #print(runScore)








#assigns numerical values to each card in the deck
cardNumVal = {'Ah': 1, 'Ad': 1, 'Ac': 1, 'As': 1, '2h': 2, '2d': 2, '2c': 2, '2s': 2, '3h': 3, '3d': 3, '3c': 3, '3s': 3, '4h': 4, '4d': 4, '4c': 4, '4s': 4,
              '5h': 5, '5d': 5, '5c': 5, '5s': 5, '6h': 6, '6d': 6, '6c': 6, '6s': 6, '7h': 7, '7d': 7, '7c': 7, '7s': 7, '8h': 8, '8d': 8, '8c': 8, '8s': 8,
              '9h': 9, '9d': 9, '9c': 9, '9s': 9, '10h': 10, '10d': 10, '10c': 10, '10s': 10, 'Jh': 10, 'Jd': 10, 'Jc': 10, 'Js': 10,
              'Qh': 10, 'Qd': 10, 'Qc': 10, 'Qs': 10, 'Kh': 10, 'Kd': 10, 'Kc': 10, 'Ks': 10}


#orders the cards by creating a list of tuples to be referenced when checking for runs; '10' is listed as '1' to only have to check the first character
cardOrderTuplesList = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('1', 10), ('J', 11), ('Q', 12), ('K', 13)]





def main():
    startingHandvalidHandList = [0, False]

    while startingHandvalidHandList[1] == False:
        startingHandvalidHandList = enterHand()
        #print(startingHandvalidHandList[1])

    startingHand = startingHandvalidHandList[0]

    possibleHands = list(combinations(startingHand, 4))
    #print(len(possibleHands))

    EVTupleList = []
    maxTupleList = []
    for r in range(len(possibleHands)):
        handList = list(possibleHands[r])


        #choose a starter
        possibleStarters = cardNumVal.copy()
        for r in range(len(handList)):
            del possibleStarters[handList[r]]
        #print(possibleStarters)
        #print('Chosen hand: ', handList)


        #iterate over all possible starters
        masterScoreList = []
        for key in possibleStarters:
            global starter
            starter = key
            #print(key)
            handList.append(key)
            #print('Hand after starter is chosen: ', handList)
            


            #score each hand
            global handScoreList
            handScoreList = []
            

            #score the pairs
            scorePairs(handList)
            

            #score the 15s
            global combinationsList
            combinationsList = getAllCombinations(handList)
            scoreFifteens(handList)


            #score nobs
            scoreNobs(handList)

            #score a flush if it exists
            scoreFlush(handList)


            #score any runs
            scoreRuns(handList)

            
            #score the whole hand
            #print(handScoreList)
            #return handScoreList
            handScore = sum(handScoreList)
            masterScoreList.append(handScore)
            #print(handScore)

            del handList[4]

        #print(masterScoreList)
        EV = sum(masterScoreList)/len(masterScoreList)
        maxScore = max(masterScoreList)
        minScore = min(masterScoreList)
        
        #print('Expected Value: ', EV)
        #print('Maximum possible score: ', maxScore)
        #print('Minumum possible score: ', minScore)

        EVTuple = (handList, EV)
        EVTupleList.append(EVTuple)

        maxTuple = (handList, maxScore)
        maxTupleList.append(maxTuple)
        

    
    
    
    bestHand = max(EVTupleList, key = lambda x: x[1])
    bestHandEV = bestHand[1]
    EVList = []
    for r in range(len(EVTupleList)):
        EVList.append(EVTupleList[r][1])
    maxEVIndices = [index for index, val in enumerate(EVList) if val == bestHandEV]
    #print(maxEVIndices)
    bestHandsList = []
    for r in range(len(maxEVIndices)):
        bestHandsList.append(EVTupleList[maxEVIndices[r]])
    #print(bestHandsList)
    
    maxHand = max(maxTupleList, key = lambda x: x[1])
    maxPossibleScore = maxHand[1]
    maxList = []
    for r in range(len(maxTupleList)):
        maxList.append(maxTupleList[r][1])
    maxIndices = [index for index, val in enumerate(maxList) if val == maxPossibleScore]
    #print(maxIndices)
    maxHandsList = []
    for r in range(len(maxIndices)):
        maxHandsList.append(maxTupleList[maxIndices[r]])

    print()
    
    print('Highest EV Hand(s): ')
    for r in range(len(bestHandsList)):
        print(bestHandsList[r][0])
    print('EV: ', bestHand[1])
    print()
    print('Hand(s) with highest possible score: ')
    for r in range(len(maxHandsList)):
        print(maxHandsList[r][0])
    print('Max score: ', maxHand[1])
    print()


while runAgain == True:
    main()



        
        

