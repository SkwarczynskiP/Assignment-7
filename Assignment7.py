# Question 1
# Give an algorithm to solve this problem. Determine the asymptotic time and space complexity of your algorithm with
# respect to the size n of the tree.
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:                        # If the root is None, return an empty list
            return []
        queue = deque([root])               # Initialize the queue with the root node
        levels = []                         # List to store the level order traversal
        while queue:                        # Continue the traversal until the queue is empty
            level = []                      # List to store the nodes at the current level
            for _ in range(len(queue)):     # Traverse all the nodes at the current level
                node = queue.popleft()      # Pop the node from the queue
                level.append(node.val)      # Add the node value to the current level
                if node.left:               # Add the left and right children of the node to the queue
                    queue.append(node.left)
                if node.right:              # Add the left and right children of the node to the queue
                    queue.append(node.right)
            levels.append(level)            # Add the current level to the level order traversal
        return levels

# Time Complexity: O(n) where n is the number of nodes in the tree.
# This is because the algorithm traverses each node in the tree once to construct the level order traversal.
# Space Complexity: O(n) where n is the number of nodes in the tree.
# This is because the algorithm uses a queue to store nodes at each level, which can have at most n nodes in the queue.

# Question 2
# Give an algorithm to solve this problem. Determine the asymptotic time and space complexity of your algorithm with
# respect to the number of points n.
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points) # Number of points
        if n == 0:      # If there are no points, return 0
            return 0

        min_heap = [(0, 0)] # (cost, point_index) Min-heap to store the minimum cost edge at the top
        visited = set()     # Set to store the visited points
        total_cost = 0      # Total cost to connect all points

        while len(visited) < n:               # Continue until all points are visited
            cost, i = heapq.heappop(min_heap) # Pop the minimum cost edge from the heap
            if i in visited:                  # Skip if the point is already visited
                continue
            visited.add(i)                    # Mark the point as visited
            total_cost += cost                # Add the cost to the total cost

            for j in range(n):                # Calculate the distance to all unvisited points
                if j not in visited:          # Add the distance to the heap
                    distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (distance, j))

        return total_cost # Return the total cost

# Time Complexity: O(n^2 * log(n)) where n is the number of points.
# This is because the while loop runs n times to visit all points. In each iteration of the while loop, the inner for
# loop runs n times to calculate the distance to all unvisited points. The heapq operations take O(log(n)) time.
# Space Complexity: O(n^2) where n is the number of points.
# This is because the algorithm uses a min-heap to store the distances between all pairs of points, which can have at
# most n^2 entries in the heap.
