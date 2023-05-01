# Process class to represent each process
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

# FCFS scheduling algorithm implementation
def sjf_np_scheduling(processes):
    # Sort the processes based on their burst time
    processes = sorted(processes, key=lambda p: p.burst_time)
    n = len(processes)
    completed = [False] * n
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    print("----------------------- SJF Non-Preemptive -----------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")

    while True:
        # Find the shortest job that has arrived but has not been executed
        min_burst_time = float('inf')
        min_index = -1
        for i in range(n):
            if not completed[i] and processes[i].arrival_time <= current_time and processes[i].burst_time < min_burst_time:
                min_burst_time = processes[i].burst_time
                min_index = i

        if min_index == -1:
            # All processes have been executed
            break

        # Execute the shortest job
        process = processes[min_index]
        completion_time = current_time + process.burst_time
        turnaround_time = completion_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        completed[min_index] = True
        print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", completion_time, "\t |",turnaround_time, "\t |", waiting_time, " |")

        # Update the current time
        current_time = completion_time

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)

# class Process:
#     def __init__(self, pid, arrival_time, burst_time):
#         self.pid = pid
#         self.arrival_time = arrival_time
#         self.burst_time = burst_time
#         self.remaining_time = burst_time

def sjf_p_scheduling(processes):
    # Sort the processes based on their arrival time
    processes = sorted(processes, key=lambda p: p.arrival_time)
    n = len(processes)
    completed = [False] * n
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    print("----------------------- SJF Preemptive -----------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")

    while True:
        # Find the process with the shortest remaining time
        min_remaining_time = float('inf')
        min_index = -1
        for i in range(n):
            if not completed[i] and processes[i].arrival_time <= current_time and processes[i].remaining_time < min_remaining_time:
                min_remaining_time = processes[i].remaining_time
                min_index = i

        if min_index == -1:
            # All processes have been executed
            break

        # Execute the process for 1 time unit
        process = processes[min_index]
        process.remaining_time -= 1

        # If the process has completed, calculate its completion time, turnaround time, and waiting time
        if process.remaining_time == 0:
            completion_time = current_time + 1
            turnaround_time = completion_time - process.arrival_time
            waiting_time = turnaround_time - process.burst_time
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time
            completed[min_index] = True
            print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", completion_time, "\t |",turnaround_time, "\t |", waiting_time, " |")

        # Update the current time
        current_time += 1

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)


# Example usage
if __name__ == '__main__':
    
    count = 0
    # Create some processes
    processes = [
        Process(1, 0, 10),
        Process(2, 1, 4),
        Process(3, 2, 2),
        Process(4, 3, 1)
    ]
    # no_processess = int(input("Enter number of processes : "))
    # processes = []
    # for i in range(0, no_processess):
    #     arr_time = int(input("Arrival Time : "))
    #     bur_time = int(input("Burst Time : "))
    #     processes.append(Process(i+1, arr_time, bur_time))

	# Run the SJF Non-Preemptive scheduling algorithm
    sjf_np_scheduling(processes)
print("\n\n")
# Run the SJF Preemptive scheduling algorithm
sjf_p_scheduling(processes)
    # Print the average waiting time
