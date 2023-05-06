class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin_scheduling(processes, time_quantum):
# Initialize the current time and waiting time
    current_time = 0
    waiting_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    n = len(processes)
    print("------------------------ Round-Robin ------------------------")
    print("PID\t | AT\t | BT\t | CT\t | TAT\t | WT |")
    # Initialize a list to keep track of completed processes
    completed = [False] * n

    # Loop through the processes and calculate their waiting time
    while True:
        all_completed = True
        # Loop through the processes and execute them for the time quantum
        for i in range(n):
            if not completed[i]:
                all_completed = False
                process = processes[i]
                if process.remaining_time > time_quantum:
                    # Execute the process for the time quantum
                    process.remaining_time -= time_quantum
                    current_time += time_quantum
                else:
                    # Execute the process for the remaining time
                    current_time += process.remaining_time
                    process.remaining_time = 0
                    completed[i] = True
                    # Calculate the waiting time for the completed process
                    completion_time = current_time
                    turnaround_time = completion_time - process.arrival_time
                    waiting_time = turnaround_time - process.burst_time
                    total_turnaround_time += turnaround_time
                    total_waiting_time += waiting_time
                    print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", completion_time, "\t |",turnaround_time, "\t |", waiting_time, " |")

        if all_completed:
            break

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)

# Example usage
if __name__ == '__main__':
# Create some processes
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

    # Set the time quantum
    time_quantum = 2

    # Run the Round-robin scheduling algorithm
    round_robin_scheduling(processes, time_quantum)
