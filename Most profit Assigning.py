def maxProfitAssignment(difficulty, profit, worker):
    data = dict(zip(difficulty, profit))
    data = sorted(data)
    print(data)
    i = 0
    j = 0
    sum = 0
    worker.sort()

    while (j<len(worker) and i < len(difficulty)):
        if (worker[j] >= difficulty[i]):
            i += 1
        elif (worker[j] < difficulty[i]):

            if(i==0):
                break
            else:
                sum += data[difficulty[i-1]]
                j += 1
    
    return sum



    # profit_worker = 0
    # for j in range(len(worker)):
    #     for i in range(len(difficulty)):
            
    #         if (worker[j] >= difficulty[i]):
    #             profit_worker += profit[i]



    




difficulty = [13,37,58]
    
profit = [4,90,96]

worker = [34,73,45]
print(maxProfitAssignment(difficulty,profit,worker))