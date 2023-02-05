from random import choice,choices
import time

def createRandomExercises(numberOfEx = 2):
    randomLst = []
    randomAnswers = [1, 2, 3]
    exercises = [1,-1,-2,2,3,-3]
    answer = choice(randomAnswers)
    while(True):
        randomNumbers = choices(exercises,k = numberOfEx)
        if answer ==  sum(randomNumbers) and randomNumbers[0] > 0:
            for i in range(len(randomNumbers)):
                if( randomNumbers[i] > 0 and i != 0): 
                    randomLst.append("+"+str(randomNumbers[i]))
                else:
                    randomLst.append(str(randomNumbers[i]))
            break
    return {
        "exercises": "".join(randomLst),
        "answer": answer
    }