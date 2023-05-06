# Process class to represent each process
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

# FCFS scheduling algorithm implementation
def fcfs_scheduling(processes):
    # Sort the processes based on their arrival time
    processes = sorted(processes, key=lambda p: p.arrival_time)
    
    # Initialize the current time and waiting time
    cur_time = processes[0].arrival_time
    current_time = []
    completion_time = []
    wait_time = 0
    waiting_time = []
    ta_time = 0
    turnaround_time = []
    total_turnaround_time = 0
    total_waiting_time = 0
    print("--------------------------- FCFS ---------------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")

    # Loop through the processes and calculate their waiting time
    for process in processes:
        # Calculate the waiting time for the current process
        cur_time = max(cur_time, process.arrival_time)
        current_time.append(cur_time)
        compl_time = cur_time + process.burst_time
        completion_time.append(compl_time)
        ta_time = compl_time - process.arrival_time
        turnaround_time.append(ta_time)
        wait_time = ta_time - process.burst_time
        waiting_time.append(wait_time)

        # Update the current time
        cur_time += process.burst_time
        total_turnaround_time += ta_time
        total_waiting_time += wait_time
        print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", compl_time, "\t |",ta_time, "\t |", wait_time, " |")

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)

# Example usage
if __name__ == '__main__':
    
    # Create some processes
    processes = [
        Process(1, 0, 10),
        Process(2, 1, 4),
        Process(3, 2, 2),
        Process(4, 4, 5)
    ]
    # no_processess = int(input("Enter number of processes : "))
    # processes = []
    # for i in range(0, no_processess):
    #     arr_time = int(input("Arrival Time : "))
    #     bur_time = int(input("Burst Time : "))
    #     processes.append(Process(i+1, arr_time, bur_time))


    # Run the FCFS scheduling algorithm
    fcfs_scheduling(processes)
