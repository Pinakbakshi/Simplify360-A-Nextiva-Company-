from collections import defaultdict, deque

def topological_sort(graph, indegree):
    topo_order = []
    q = deque([node for node in indegree if indegree[node] == 0])
    
    while q:
        node = q.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
                
    return topo_order

def calculate_times(tasks, dependencies):
    graph = defaultdict(list)
    indegree = {task: 0 for task in tasks}
    duration = {task: tasks[task] for task in tasks}
    
    for u, v in dependencies:
        graph[u].append(v)
        indegree[v] += 1
    
    topo_order = topological_sort(graph, indegree)
    
    EST = {task: 0 for task in tasks}
    EFT = {task: 0 for task in tasks}
    
    for node in topo_order:
        EFT[node] = EST[node] + duration[node]
        for neighbor in graph[node]:
            EST[neighbor] = max(EST[neighbor], EFT[node])
    
    max_EFT = max(EFT.values())
    
    LFT = {task: max_EFT for task in tasks}
    LST = {task: 0 for task in tasks}
    
    for node in reversed(topo_order):
        for neighbor in graph[node]:
            LFT[node] = min(LFT[node], LST[neighbor])
        LST[node] = LFT[node] - duration[node]
    
    return max_EFT, max(LFT.values())

def main():
    print("Enter the number of tasks:")
    n = int(input())
    
    tasks = {}
    print("Enter each task name followed by its duration (e.g., 'A 4'):")
    for _ in range(n):
        task, duration = input().split()
        tasks[task] = int(duration)
    
    print("Enter the number of dependencies:")
    d = int(input())
    
    dependencies = []
    print("Enter each dependency as a pair of tasks (e.g., 'A B' means A must finish before B starts):")
    for _ in range(d):
        u, v = input().split()
        dependencies.append((u, v))
    
    earliest_time, latest_time = calculate_times(tasks, dependencies)
    print(f"\nEarliest time all tasks will be completed: {earliest_time}")
    print(f"Latest time all tasks will be completed: {latest_time}")

if __name__ == "__main__":
    main()



# from collections import defaultdict, deque

# # Helper function to perform topological sorting
# def topological_sort(graph, indegree):
#     topo_order = []
#     q = deque([node for node in indegree if indegree[node] == 0])
    
#     while q:
#         node = q.popleft()
#         topo_order.append(node)
#         for neighbor in graph[node]:
#             indegree[neighbor] -= 1
#             if indegree[neighbor] == 0:
#                 q.append(neighbor)
                
#     return topo_order

# def calculate_times(tasks, dependencies):
#     # Initialize graph, durations, and indegrees
#     graph = defaultdict(list)
#     indegree = {task: 0 for task in tasks}
#     duration = {task: tasks[task] for task in tasks}
    
#     # Build the graph and calculate indegree
#     for u, v in dependencies:
#         graph[u].append(v)
#         indegree[v] += 1
    
#     # Perform topological sort
#     topo_order = topological_sort(graph, indegree)
    
#     # Initialize time dictionaries
#     EST = {task: 0 for task in tasks}
#     EFT = {task: 0 for task in tasks}
    
#     # Calculate EST and EFT
#     for node in topo_order:
#         EFT[node] = EST[node] + duration[node]
#         for neighbor in graph[node]:
#             EST[neighbor] = max(EST[neighbor], EFT[node])
    
#     # Calculate LFT and LST
#     LFT = {task: float('inf') for task in tasks}
#     LST = {task: float('inf') for task in tasks}
    
#     # The project completion time is determined by the maximum EFT
#     max_EFT = max(EFT.values())
    
#     for task in tasks:
#         if not graph[task]:  # Leaf node
#             LFT[task] = max_EFT
    
#     # Process in reverse topological order
#     for node in reversed(topo_order):
#         LST[node] = LFT[node] - duration[node]
#         for neighbor in graph[node]:
#             LFT[node] = min(LFT[node], LST[neighbor])
    
#     # The latest finish time is the maximum LFT
#     max_LFT = max(LFT.values())
    
#     return max_EFT, max_LFT

# # Example usage:
# tasks = {
#     'T_START': 0,
#     'A': 4,
#     'B': 3,
#     'C': 2,
#     'D': 5,
#     'E': 3,
#     'F': 2
# }

# dependencies = [
#     ('T_START', 'A'),
#     ('A', 'B'),
#     ('A', 'C'),
#     ('B', 'D'),
#     ('C', 'D'),
#     ('D', 'E'),
#     ('E', 'F')
# ]

# earliest_time, latest_time = calculate_times(tasks, dependencies)
# print(f"Earliest time all tasks will be completed: {earliest_time}")
# print(f"Latest time all tasks will be completed: {latest_time}")


