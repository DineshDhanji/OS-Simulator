class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin(processes, quantum):
    """Simulates a Round Robin process scheduling algorithm and returns a list of tuples
    representing the order in which processes are executed.
    
    Args:
    processes (list): A list of process objects containing information such as process ID and burst time.
    quantum (int): The time quantum or time slice for each process.
    
    Returns:
    list: A list of tuples representing the order in which processes are executed.
    """
    n = len(processes)
    time = 0
    remaining_burst_time = [process.burst_time for process in processes]
    waiting_queue = []
    order = []
    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                    waiting_queue.append(i)
                    order.append((processes[i].pid, time))
                else:
                    time += remaining_burst_time[i]
                    order.append((processes[i].pid, time))
                    remaining_burst_time[i] = 0
        if done == True:
            break
        while len(waiting_queue) > 0:
            i = waiting_queue.pop(0)
            if remaining_burst_time[i] > 0:
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                    waiting_queue.append(i)
                    order.append((processes[i].pid, time))
                else:
                    time += remaining_burst_time[i]
                    order.append((processes[i].pid, time))
                    remaining_burst_time[i] = 0
    return order

processes = [
        Process(1, 0, 10),
        Process(2, 1, 40),
        Process(3, 2, 20),
        Process(4, 45, 5)
    ]

a = round_robin(processes, 2)
print(a)
