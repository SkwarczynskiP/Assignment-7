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
        if not root:
            return []
        queue = deque([root])
        levels = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
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
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))
        edges.sort()
        parent = [i for i in range(n)]
        rank = [0] * n
        cost = 0
        for distance, i, j in edges:
            if union(parent, rank, i, j):
                cost += distance
        return cost

# Time Complexity:
# Space Complexity: