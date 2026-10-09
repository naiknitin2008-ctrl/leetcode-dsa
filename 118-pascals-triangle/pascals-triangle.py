class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(numRows):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=a[i-1][j-1] + a[i-1][j]
            a.append(r)
        return a