# Process class to represent each process
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

# SJF (Non preemptive) scheduling algorithm implementation
def sjf_np_scheduling(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    cur_time = processes[0].arrival_time
    processes = sorted(processes, key=lambda p: p.burst_time)
    n = len(processes)
    completed = [False] * n
    current_time = []
    completion_time = []
    turnaround_time = []
    waiting_time = []
    total_turnaround_time = 0
    total_waiting_time = 0
    print("----------------------- SJF Non-Preemptive -----------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")

    while True:
        # Find the shortest job that has arrived but has not been executed
        min_burst_time = float('inf')
        min_index = -1
        for i in range(n):
            if (not completed[i] and processes[i].arrival_time <= cur_time and processes[i].burst_time < min_burst_time):
                min_burst_time = processes[i].burst_time
                min_index = i
        if min_index == -1:
            # All processes have been executed
            break

        # Execute the shortest job
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
        print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", compl_time, "\t |",ta_time, "\t |", wait_time, " |")

        # Update the current time
        cur_time = compl_time

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)

def sjf_p_scheduling(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    cur_time = processes[0].arrival_time
    n = len(processes)
    completed = [False] * n
    current_time = []
    completion_time = []
    turnaround_time = []
    waiting_time = []
    total_turnaround_time = 0
    total_waiting_time = 0
    print("----------------------- SJF Preemptive -----------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")

    while True:
        # Find the process with the shortest remaining time
        min_remaining_time = float('inf')
        min_index = -1
        for i in range(n):
            if not completed[i] and processes[i].arrival_time <= cur_time and processes[i].remaining_time < min_remaining_time:
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
            current_time.append(cur_time)
            compl_time = cur_time + 1
            completion_time.append(compl_time)
            ta_time = compl_time - process.arrival_time
            turnaround_time.append(ta_time)
            wait_time = ta_time - process.burst_time
            waiting_time.append(wait_time)
            total_turnaround_time += ta_time
            total_waiting_time += wait_time
            completed[min_index] = True
            print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", compl_time, "\t |",ta_time, "\t |", wait_time, " |")

        # Update the current time
        cur_time += 1

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)


# Example usage
if __name__ == '__main__':
    
    # Create some processes
    processes = [
        Process(1, 0, 10),
        Process(2, 1, 40),
        Process(3, 2, 20),
        Process(4, 45, 5)
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
