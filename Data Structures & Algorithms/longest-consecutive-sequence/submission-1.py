class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        longest = 0

        for n in nums:
            if (n - 1) in nums:
                continue
            
            else: 
                count = 1                   #[1,2,3,4]
                current = n
                while (current+1) in nums:
                    count += 1
                    current +=1
                if count > longest:
                    longest = count


            
        return longest

        #[0,3,2,5,4,6,1,1]
        #[0,1,1,2,3,4,5,6]