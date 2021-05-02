#import timing
import random

tulokset = {}

def luolista():
    A = []
    pituus = int(input("Anna listan pituus: "))
    #import timing
    for i in range(0,pituus):
        arvo = random.randint(0,10)
        A.append(arvo)
    return A

def main():
    A = luolista()
    A.sort()
    x=0
    for i in range(len(A)):
        b = len(A) - i
        #print("ass " + str(A[i]))
        z = len(A) - 1
        for s in range(b):
            if A[i] == A[i-1]:
                continue
            if i == 0:
                s = 0 + s
            if i > 0:
                s += i
            if A[s] == A[i]:
                x += 1
            #print("z: {}".format(z))
            #print("s: {}".format(s))
            if s == z or (i == 0 and s == z-1):
                tulokset[str(A[i])] = x
            #    print(tulokset)
                x = 0
                break
            else:
                continue
    
    print(tulokset)
    print("Moodi on: " + max(tulokset, key=tulokset.get))
    #print("Moodi on: " + str(key))

main()