from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()  

       
        for i in range(k): #preprocess the 1st winodw
            while dq and nums[dq[-1]] < nums[i]: #check if last smaller then current then pop from the bcak
                dq.pop()
            dq.append(i) #append the indexex in the dq

        
        res.append(nums[dq[0]]) # top of the dq will contain the max elemt for the current window 

        
        for i in range(k, len(nums)): 
           
            if dq and dq[0] <= i - k: #this will ensure ki top is lies in the range of the window let say k=3 and i = 4 then 4-3 top should be greater than and equal to 1
                dq.popleft() # top is less than 1 so we wil pop it
            
            while dq and nums[dq[-1]] < nums[i]: # checks if last samller then current elemet
                dq.pop()
            
            dq.append(i)
            res.append(nums[dq[0]]) # top will conatin the result 

        return res #########monotic queue 
