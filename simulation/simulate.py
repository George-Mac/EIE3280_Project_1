import numpy as np
import scipy.stats as ss

theta = 0.85
N = eval(input("Enter number of nodes:"))
pi_0 = []
for i in range(N):
    pi_0.append(1/N)

out_link = []
for i in range(N):
    out = input()
    out = out.split()
    for j in range(len(out)):
        out[j] = eval(out[j])
    out_link.append(out)
    
# out_link = [[2],
            # [2],
            # [2],
            # [2]]
H = []
for link in out_link:
    row = []

    if(len(link)>0):
        for i in range(N):
            row.append(0)
        for out in link:
            row[out-1] = 1/(len(link))

    elif (len(link)==0):
        for i in range(N):
            row.append(1/N)

    H.append(row)
    
H = np.array(H)

balance_matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(1)
    balance_matrix.append(row)
    
balance_matrix = np.array(balance_matrix)
G = theta*H + (1-theta)*(1/N)*balance_matrix

pi_old = np.array(pi_0)
iter_num = 0

while True:
    pi_new = np.dot(pi_old.T, G)
    diff = pi_new - pi_old
    if ((abs(diff) <= 0.000001).all()):
        # rank = ss.rankdata(pi_new)
        rank = ss.rankdata([-1 * i for i in pi_new]).astype(int)
        print("final pi: ")
        print(pi_new)
        print("rank:")
        print(rank)
        break
    
    pi_old = pi_new
    iter_num = iter_num + 1

