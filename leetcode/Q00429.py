'''
429. N-ary Tree Level Order Traversal
BFS
'''

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        queue = collections.deque()
        res = []
        queue.append(root)
        
        while queue:
            queue_len = len(queue)
            temp = []
            for _ in range(queue_len):
                node = queue.popleft()
                temp.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(temp)
        return res
