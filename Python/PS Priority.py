class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

def priority_scheduling(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    cur_time = processes[0].arrival_time
    # Sort the processes based on their priority
    processes = sorted(processes, key=lambda p: p.priority, reverse=True)
    n = len(processes)
    completed = [False] * n
    current_time = []
    completion_time = []
    turnaround_time = []
    waiting_time = []
    total_turnaround_time = 0
    total_waiting_time = 0
    print("----------------------- Priority Scheduling -----------------------")
    print("PID\t | AT\t | BT\t | P\t | CT\t | TAT\t | WT |")

    while True:
        # Find the highest priority process that has arrived but has not been executed
        highest_priority = 1000000 #Supposing a max 
        min_index = -1
        for i in range(n):
            if not completed[i] and processes[i].arrival_time <= cur_time and processes[i].priority < highest_priority:
                highest_priority = processes[i].priority
                min_index = i

        if min_index == -1:
            # All processes have been executed
            break

        # Execute the highest priority process
        process = processes[min_index]
        current_time.append(cur_time)
        compl_time = cur_time + process.burst_time
        completion_time.append(compl_time)
        ta_time = compl_time - process.arrival_time
        turnaround_time.append(ta_time)
        wait_time = ta_time - process.burst_time
        waiting_time.append(wait_time)
        total_turnaround_time += ta_time
        total_waiting_time += wait_time
        completed[min_index] = True
        print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", process.priority, "\t |", compl_time, "\t |", ta_time, "\t |", wait_time, " |")

        # Update the current time
        cur_time = compl_time

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)
if __name__ == '__main__':
    # Create some processes
    processes = [
        Process(1, 0, 10, 7),
        Process(2, 1, 40, 3),
        Process(3, 2, 20, 2),
        Process(4, 5, 5, 5)
    ]
    # Call the priority scheduling function
    priority_scheduling(processes)
