class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numlist=list(set(nums))
        count={}
        for i in range(len(numlist)):
            if numlist[i]-1 in numlist:
                continue
            count[numlist[i]]=1
            inc=1
            while numlist[i]+inc in numlist:
                count[numlist[i]]+=1
                inc+=1

        res=0
        for v in count.values():
            if v>res:
                res=v
        return res




        