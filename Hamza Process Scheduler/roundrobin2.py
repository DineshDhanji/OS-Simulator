class Process: 
    def input_data(self, no_of_processes):
        processess = []
        for i in range(no_of_processes):
            temp = []
            pid = int(input("Enter Process ID: "))
            arrival_time = int(input(f"Enter Arrival Time for Process {pid}: "))
            burst_time = int(input(f"Enter Burst Time for Process {pid}: "))
            temp.extend([pid, arrival_time, burst_time, 0, burst_time]) # 0 is state of process and it means not executed
            processess.append(temp)
        time_slice = int(input("Enter Time Slice: "))
        RoundRobin.schedulingProcess(self, processess, time_slice)

class RoundRobin:
    def schedulingProcess(self, processess, time_slice):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        processess.sort(key=lambda x: x[1]) #sort processess according to arrival_time
        while True:
            normal_queue = []
            temp = []
            for i in range(len(processess)):
                if processess[i][1] <= s_time and processess[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if processess[i][0] == ready_queue[k][0]:
                                present = 1
                    '''
                    The above if loop checks that the next process is not a part of ready_queue
                    '''
                    if present == 0:
                        temp.extend([processess[i][0], processess[i][1], processess[i][2], processess[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    '''
                    The above if loop adds a process to the ready_queue only if it is not already present in it
                    '''
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                    '''
                    The above if loop makes sure that the recently executed process is appended at the end of ready_queue
                    '''
                elif processess[i][3] == 0:
                    temp.extend([processess[i][0], processess[i][1], processess[i][2], processess[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_slice:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(processess)):
                        if processess[j][0] == ready_queue[0][0]:
                            break
                    processess[j][2] = processess[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(processess)):
                        if processess[j][0] == ready_queue[0][0]:
                            break
                    processess[j][2] = 0
                    processess[j][3] = 1
                    processess[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(processess)):
                        if processess[j][0] == normal_queue[0][0]:
                            break
                    processess[j][2] = processess[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(processess)):
                        if processess[j][0] == normal_queue[0][0]:
                            break
                    processess[j][2] = 0
                    processess[j][3] = 1
                    processess[j].append(e_time)
        t_time = RoundRobin.calculateTurnaroundTime(self, processess)
        w_time = RoundRobin.calculateWaitingTime(self, processess)
        RoundRobin.printData(self, processess, t_time, w_time, executed_process)

    def calculateTurnaroundTime(self, processess):
        total_turnaround_time = 0
        for i in range(len(processess)):
            turnaround_time = processess[i][5] - processess[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            processess[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(processess)
        return average_turnaround_time

    def calculateWaitingTime(self, processess):
        total_waiting_time = 0
        for i in range(len(processess)):
            waiting_time = processess[i][6] - processess[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            processess[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(processess)
        return average_waiting_time

    def printData(self, processess, average_turnaround_time, average_waiting_time, executed_process):
        processess.sort(key=lambda x: x[0]) #sort processess accrding to PID
        print("------------------------ Round-Robin ------------------------")
        print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")
        for i in range(len(processess)):
            print(processess[i][0], "\t |", processess[i][1], "\t |", processess[i][4], "\t |", processess[i][5], "\t |",processess[i][6], "\t |", processess[i][7], " |")

        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')

if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    p = Process()
    p.input_data(no_of_processes)