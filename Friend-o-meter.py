from collections import defaultdict, deque

class SocialNetwork:
    def __init__(self):
        self.friends = defaultdict(set)

    def add_friendship(self, person1, person2):
        self.friends[person1].add(person2)
        self.friends[person2].add(person1)

    def find_common_friends(self, person1, person2):
        if person1 not in self.friends or person2 not in self.friends:
            return set()
        return self.friends[person1] & self.friends[person2]

    def find_connection_level(self, person1, person2):
        if person1 not in self.friends or person2 not in self.friends:
            return -1

        if person1 == person2:
            return 0

        queue = deque([(person1, 0)])
        visited = set([person1])

        while queue:
            current_person, level = queue.popleft()

            for friend in self.friends[current_person]:
                if friend == person2:
                    return level + 1
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, level + 1))

        return -1

def main():
    network = SocialNetwork()

    # Adding some friendships
    network.add_friendship('Alice', 'Bob')
    network.add_friendship('Bob', 'Charlie')
    network.add_friendship('Charlie', 'Janice')
    network.add_friendship('Alice', 'David')
    network.add_friendship('David', 'Emma')
    
    # Find common friends between Alice and Bob
    print("Common friends between Alice and Bob:", network.find_common_friends('Alice', 'Bob'))
    
    # Find the nth connection between Alice and Janice
    print("Connection level between Alice and Janice:", network.find_connection_level('Alice', 'Janice'))
    
    # Find the nth connection between Alice and Emma
    print("Connection level between Alice and Emma:", network.find_connection_level('Alice', 'Emma'))
    
    # Find the nth connection between Alice and someone with no connection
    print("Connection level between Alice and unknown person:", network.find_connection_level('Alice', 'Unknown'))

if __name__ == "__main__":
    main()


# Time Complexity:
# Building the graph takes O(V + E), where V is the number of tasks and E is the number of dependencies.
# topological sorting step takes O(V + E), as we process each task and edge exactly once.
# Calculate Earliest Start Time (EST) and Earliest Finish Time (EFT) step takes O(V + E) since we're iterating over each task and its dependencies.
# Calculate Latest Finish Time (LFT) and Latest Start Time (LST) step also takes O(V + E) for the same reasons as the EST/EFT calculation.
# Return Results is O(V) since we’re iterating over the tasks to get these values.
# Time Complexity Summary

# Space Complexity:
# The space complexity is dominated by the adjacency list (graph), which is O(V + E), along with the space for the dictionaries. Thus, the overall space complexity is O(V + E).
