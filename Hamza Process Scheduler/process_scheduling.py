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
    for process in processes:
        print(process.pid, process.arrival_time, process.burst_time)
    
    print("\n")
    # Initialize the current time and waiting time
    current_time = 0
    waiting_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    print("--------------------------- FCFS ---------------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")

    # Loop through the processes and calculate their waiting time
    for process in processes:
        # Calculate the waiting time for the current process
        current_time = max(current_time, process.arrival_time)
        completion_time = current_time + process.burst_time
        turnaround_time = completion_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time
        # waiting_time += max(0, current_time - process.arrival_time)

        # Update the current time
        current_time += process.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", completion_time, "\t |",turnaround_time, "\t |", waiting_time, " |")

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)

def sjf_np_scheduling(processes):
    # Sort the processes based on their burst time
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.burst_time))

    for process in processes:
        print(process.pid, process.arrival_time, process.burst_time)
    
    print("\n")
    
    # Initialize the current time, waiting time, and total time
    current_time = 0
    waiting_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    print("--------------------------- SJF Non-Preemptive ---------------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")

    # Loop through the processes and calculate their waiting time
    for process in processes:
        # Calculate the waiting time for the current process
        current_time = max(current_time, process.arrival_time)
        completion_time = current_time + process.burst_time
        turnaround_time = completion_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time
        # waiting_time += max(0, current_time - process.arrival_time)

        # Update the current time and total time
        current_time += process.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", completion_time, "\t |",turnaround_time, "\t |", waiting_time, " |")

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)

def sjf_p_scheduling(processes):
    # Initialize the current time, waiting time, and total time
    current_time = 0
    waiting_time = 0
    total_time = 0

    # Loop through the processes and calculate their waiting time
    while len(processes) > 0:
        # Sort the remaining processes based on their burst time
        processes = sorted(processes, key=lambda p: p.burst_time)

        # Get the process with the shortest burst time
        current_process = processes[0]

        # Calculate the waiting time for the current process
        waiting_time += max(0, current_time - current_process.arrival_time)

        # Update the current time and total time
        current_time += current_process.burst_time
        total_time += waiting_time

        # Remove the current process from the list of processes
        processes.remove(current_process)

    # Calculate the average waiting time
    avg_waiting_time = total_time / len(processes)

    # Return the average waiting time
    return avg_waiting_time



# Example usage
if __name__ == '__main__':
    
    count = 0
    # Create some processes
    processes = [
        Process(1, 0, 3),
        Process(2, 3, 4),
        Process(3, 8, 12),
        Process(4, 2, 2),
        Process(5, 6, 5)
    ]
    # no_processess = int(input("Enter number of processes : "))
    # processes = []
    # for i in range(0, no_processess):
    #     arr_time = int(input("Arrival Time : "))
    #     bur_time = int(input("Burst Time : "))
    #     processes.append(Process(i+1, arr_time, bur_time))


    # Run the FCFS scheduling algorithm
    fcfs_scheduling(processes)
    print("\n\n")
    sjf_np_scheduling(processes)

    # Print the average waiting time
