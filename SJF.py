print("                           this process is for SHortest Job first")
size = int(raw_input("Enter How many Process you want to Enter ??"))

process = [0] * size
arrival = [0] * size
burst = [0] * size
for i in range(size):
    process[i] = (raw_input("Enter process name"))
    arrival[i] = int(raw_input("Enter Arrival Time for the process"))
    burst[i] = int(raw_input("Enter Burst time for the Process"))
print(" ")
print("                             your Enter Pocess Information")
for i in range(size):
    print(process[i], "     ", arrival[i], "      ", burst[i])
start = [0] * size
turn = [0] * size
waiting_Time = [0] * size
turn_Time = [0] * size

for i in range(0, size):
    min1 = i
    for j in range(i + 1, (size)):
        if burst[min1] > burst[j]:
            temp1 = burst[j]
            burst[j] = burst[min1]
            burst[min1] = temp1

            temp2 = arrival[j]
            arrival[j] = arrival[min1]
            arrival[min1] = temp2

            temp3 = process[j]
            process[j] = process[min1]
            process[min1] = temp3

for j in range(size):
    if j == 0:
        start[j] = arrival[j]
        turn[j] = arrival[j] + burst[j]
    if j >= 1:
        start[j] = turn[j - 1]
        turn[j] = burst[j] + turn[j - 1]

for j in range(size):
    first1 = min(burst)
    runn = burst.index(first1)
    print(process[j], 'arrival time is', arrival[j], ' starts at ', start[j], 'and ends at ', turn[j])

for m in range(size):
    waiting_Time[m] = start[m] - arrival[m]
    turn_Time[m] = turn[m] - arrival[m]
sum1 = 0
sum2 = 0
print("")
for l in range(size):
    sum1 += waiting_Time[l]
    sum2 += turn_Time[l]
    print(process[l], 'waiting time is', waiting_Time[l])
    print(process[l], 'turn time is', turn_Time[l])
awaiting_Time = sum1 / size
aturn_Time = sum2 / size
print("")
print('average waiting time is: ', awaiting_Time)
print('average turn around time is: ', aturn_Time)
