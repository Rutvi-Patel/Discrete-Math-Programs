import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

from numpy.random.mtrand import randint, rand




def nDieSingleRoll(r, p):
     n = np.size(p)
     cs = np.cumsum(p)
     cp = np.append(0, cs)
     for k in range(0, n):
          if r > cp[k] and r <= cp[k + 1]:
               d = k + 1
     return d

# nDieSingleRoll([0.3, 0.2,0.1,0.2, 0.1, 0.1])

def nSidedDie(p):
     N = 1000
     n = np.size(p)
     s = np.zeros((N, 1))
     # print(s)
     for x in range(0,N):
         r = rand()
         s[x] = nDieSingleRoll(r,p)
     print("Die outcomes for", N, "rolls" , "\n",s)

     # Plotting
     b = range(1, n + 2)
     sb = np.size(b)
     h1, bin_edges = np.histogram(s, bins=b)
     b1 = bin_edges[0:sb - 1]
     plt.close('all')


     prob = h1 / N
     plt.stem(b1, prob)
     # Graph labels
     plt.title('PMF for n-sided die')
     plt.xlabel('Number on the face of the die')
     plt.ylabel('Probability')
     plt.xticks(b1)
     plt.show()



# Problem 1
nSidedDie([0.1,0.15,0.2,0.05,0.3,0.1,0.1])


# p = [0.1,0.15,0.2,0.05,0.3,0.1,0.1]





# ----------------------------------------------------------------------Problem 2--------------------------------------------------

def numOfRolls (N):
     r = random
     # sadd = np.zeros((N,1))
     sadd = [-1]*N
     for x in range(N):

          numR = 0
          a = True
          while(a == True ):
               d1 = r.randint(1, 7)
               d2 = r.randint(1, 7)
               msum= d1 + d2
               if msum == 7:
                    a = False
               else:
                    numR = numR+1
          sadd[x] = numR
     print(sadd)


     minv = min(sadd)
     maxv = max(sadd)
     b = range(0,maxv)
     # print(b)
     sb = np.size(b)
     h1, bin_edges = np.histogram(sadd, bins = b)
     b1 = bin_edges[0:sb-1]
     plt.close('all')
     #
     fig2 = plt.figure(2)
     p1 = h1 / N
     plt.stem(b1, p1)
     plt.title('PMF - Rolls needed to get 7: Probability mass function')
     plt.xlabel('# of Rolls')
     plt.ylabel('Probability')
     plt.show()
     #
     fig1 = plt.figure(1)
     plt.stem(b1, h1)
     plt.title('Stem plot - Seven with 2 dice')
     plt.xlabel('# of Rolls')
     plt.ylabel('Number of occurrences')
     plt.show()


# Problem 2
# numOfRolls(100000)






# -----------------------------------------------------------------------Problem 3 -------------------------------------------------------
def fiftyHeads (N):
     success = 0
     for x in range (N):
          hVals = 0
          for y in range (100):
               f = np.random.randint(0,2)
               if (f==1):
                    hVals = hVals+1
          if (hVals == 50):
               success = success +1
     print(success,"Successes", "out of",N)
     p = success/N
     print("Probability of 50 heads in tossing 100 fair coins = ",p)


# problem 3
# fiftyHeads(100000)


# ------------------------Problem 3 Output --------------------





# -----------------------------------------------------------------Problem 4 -----------------------------------------------------
def PassHacking (m, k, myWord):
     letters = "abcdefghijklmnopqrstuvwxyz"
     N = 1000
     success = 0
     for x in range (N):
          for y in range (m):
              val = np.random.randint(0, 26, 4)
              oword = letters[val[0]]+ letters[val[1]] + letters[val[2]]+ letters[val[3]]

              if myWord == oword:
                   success = success +1
                   break

     p = success/N
     print("M: ", m, "Sucess", success, "Probability: ", p)



def PassHackWithK (m, k, myWord):
     letters = "abcdefghijklmnopqrstuvwxyz"
     N = 1000
     successTwo = 0
     for j in range(N):
          for i in range (k*m):
               val = np.random.randint(0, 26, 4)
               moword = letters[val[0]] + letters[val[1]] + letters[val[2]] + letters[val[3]]
               # print(oword)

               if myWord == moword:
                    successTwo = successTwo + 1
                    break

     p2 = successTwo/N
     print("M: ", m, "K", k, " Sucess", successTwo, " Probability: ", p2)



# PassHacking(80000,7,"ahtk")















