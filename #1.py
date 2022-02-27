class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos=0
        res=[]
        for i in range(pos , len(nums)-1):
            for j in range(pos+1,len(nums)):
                if(nums[i]+nums[j] == target and i!=j):
                    res.append(i)
                    res.append(j)
                    break;
                else:
                    j+=1
            i+=1
        return set(res)
        
