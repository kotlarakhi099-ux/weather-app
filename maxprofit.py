class solution:
  def maxprofit(self,prices:list[int])->int:
    min_price=prices[0]
    n=len(prices)
    ans=0
    for i in range (1,n):
      current_profit=prices[i]-min_price
      ans=max(current_profit,ans)
      min_price=min(min_price,prices[i])
    return ans
s1=solution()
print(s1.maxprofit([7,1,5,3,6,4]))
