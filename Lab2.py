import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def nSidedDie(p):
    randRoll = random.random() # 0 <= n < 1
    sum = 0
    result = 0
    for mass in p:
        sum += mass
        if randRoll < sum:
            return result
        result+=1





def myFunct (p_z, sig_z, sig_o):
    faliure = 0
    n = 100000
    for x in range(n):
        # m = np.random.rand()

        s = nSidedDie([p_z, 1-p_z])

        if (s == 1):
            r = nSidedDie([sig_o, 1 - sig_o])

        elif (s ==0 ):
            r = nSidedDie([1 - sig_z,sig_z])

        if (r != s):
            faliure = faliure+1

    probability = faliure/n
    print("Run 1 probability: ", probability)

myFunct(0.6,.05,0.03)


def myFunct2 (p_z,sig_z,sig_o):
    n = 100000
    success = 0
    counter = 0
    while (counter <n):
        s = nSidedDie([p_z, 1-p_z])
        if (s ==1):
            r = nSidedDie([sig_o, 1 - sig_o])
            if (r == 1):
                success = success+1
                counter = counter+1
            else:
                counter = counter+1
    probability = success/100000
    print("Run 2 probability:", probability)
myFunct2(0.6,.05,0.03)








def myFunct3 (p_z,sig_z,sig_o):
    n = 100000
    success = 0
    counter = 0
    while (counter<n):
        s = nSidedDie([p_z, 1-p_z])

        if (s == 1):
            r = nSidedDie([sig_o, 1 - sig_o])

        elif (s ==0 ):
            r = nSidedDie([1 - sig_z,sig_z])

        if (r ==1):
            counter= counter+1
            if (s == 1):
                success = success+1


    probability = success/100000
    print("Run 3 Probability:" , probability)

myFunct3(0.6,.05,0.03)






def myFunct4(p_z, sig_z, sig_o):
    result = 0

    for i in range(1, 100000):
        S = nSidedDie([p_z, 1 - p_z])
        if (S):
            R1 = nSidedDie([sig_o, 1 - sig_o])
            R2 = nSidedDie([sig_o, 1 - sig_o])
            R3 = nSidedDie([sig_o, 1 - sig_o])
        else:

            R1 = nSidedDie([1 - sig_z, sig_z])
            R2 = nSidedDie([1 - sig_z, sig_z])
            R3 = nSidedDie([1 - sig_z, sig_z])

        # If any two of the three R's are 1 then majority is 1
        if (R1 == R2):
            d = R1
        elif(R1 == R3):
            d = R1
        elif (R2 == R3):
            d = R2

        if (S != d):
            result += 1

    print("Run 4 Probability:", result / 100000)

myFunct4(0.6,.05,0.03)


