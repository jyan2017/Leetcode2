'''
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
'''

class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        output=[0]*(length+1)
        for x in updates:
            output[x[0]]+=x[2]
            output[x[1]+1]-=x[2]
        for i in range(1,length+1):
            output[i]+=output[i-1]
        return output[:length]
