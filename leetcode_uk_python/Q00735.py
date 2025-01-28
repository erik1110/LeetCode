class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for star in asteroids:
            while stack and star < 0 and stack[-1] > 0:
                if abs(star) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(star) == abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(star)
        return stack
