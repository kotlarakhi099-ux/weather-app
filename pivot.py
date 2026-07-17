class Solution:
  def piovt_index(self,nums:list[int])->int:
    left_sum=0
    total_sum=sum(nums)
    n=len(nums)
    for i in range(n):
      right_sum=total_sum-left_sum-nums[i]
      if right_sum==left_sum:
        return i
      else:
       left_sum+=nums[i]
    return -1
s=Solution()
print(s.piovt_index([1, 7, 3, 6, 5, 6]))