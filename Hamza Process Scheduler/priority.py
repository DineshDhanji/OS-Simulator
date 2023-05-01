class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

def priority_scheduling(processes):
    # Sort the processes based on their priority
    processes = sorted(processes, key=lambda p: p.priority, reverse=True)
    n = len(processes)
    completed = [False] * n
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    print("----------------------- Priority Scheduling -----------------------")
    print("PID\t | AT\t | BT\t | P\t | CT\t | TAT\t | WT |")

    while True:
        # Find the highest priority process that has arrived but has not been executed
        highest_priority = -1
        min_index = -1
        for i in range(n):
            if not completed[i] and processes[i].arrival_time <= current_time and processes[i].priority > highest_priority:
                highest_priority = processes[i].priority
                min_index = i

        if min_index == -1:
            # All processes have been executed
            break

        # Execute the highest priority process
        process = processes[min_index]
        completion_time = current_time + process.burst_time
        turnaround_time = completion_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        completed[min_index] = True
        print(process.pid, "\t |", process.arrival_time, "\t |", process.burst_time, "\t |", process.priority, "\t |", completion_time, "\t |", turnaround_time, "\t |", waiting_time, " |")

        # Update the current time
        current_time = completion_time

    # Calculate the average waiting time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average waiting time
    print("Average waiting time:", avg_waiting_time)
    print("Average turnaround time:", avg_turnaround_time)
if __name__ == '__main__':
    # Create some processes
    processes = [
        Process(pid=1, arrival_time=0, burst_time=5, priority=2),
        Process(pid=2, arrival_time=1, burst_time=3, priority=1),
        Process(pid=3, arrival_time=2, burst_time=8, priority=4),
        Process(pid=4, arrival_time=3, burst_time=2, priority=3),
        Process(pid=5, arrival_time=4, burst_time=4, priority=5)
    ]

    # Call the priority scheduling function
    priority_scheduling(processes)
