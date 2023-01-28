'''
2125. Number of Laser Beams in a Bank
Medium

Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

'''
# my solution
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = []
        for laser in bank:
            t = [int(i) for i in list(laser)]
            len_laser = sum(t)
            if len_laser!=0:
                res.append(len_laser)
        
        ans = 0
        if len(res) == 1:
            return ans
        for i in range(len(res)-1):
            ans += res[i] * res[i+1]
        return ans

# Others
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre = 0
        ans = 0

        for i in bank:
            laser = i.count("1")
            if laser:
                ans += laser * pre
                pre = laser

        return ans
