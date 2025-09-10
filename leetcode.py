# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]== target:
#                     return [i,j]


# 283class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     pos=0
    #     for i in range(len(nums)):
    #         if nums[i]!=0:
    #             nums[pos]=nums[i]
    #             pos+=1
    #     for i in range(pos,len(nums)):
    #         nums[i]=0
    #     print(nums)



# 189
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         k=k%len(nums)
#         nums[:]=nums[-k:]+nums[:-k]    
        

# 74
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#             for i in range(len(matrix)):
#                 for j in range(len(matrix[0])):
#                     if matrix[i][j]== target:
#                         return True
#             return False

# 58
# class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     a=s.split()
    #     return len(a[-1])
        

# 66
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n=len(digits)
#         for i in range(n-1,-1,-1):
#             if digits[i] <9:
#                 digits[i]+=1
#                 return digits
#             digits[i]=0
#         return [1]+digits


# 3618
# class Solution:
#     def splitArray(self, nums: List[int]) -> int:
#         def is_prime(n: int) -> bool:
#             if n < 2:
#                 return False
#             if n == 2:
#                 return True
#             if n % 2 == 0:
#                 return False
#             for i in range(3, int(math.sqrt(n)) + 1, 2):
#                 if n % i == 0:
#                     return False
#             return True


#         sum_A = 0  # Prime indices
#         sum_B = 0  # Non-prime indices

#         for i, num in enumerate(nums):
#             if is_prime(i):
#                 sum_A += num
#             else:
#                 sum_B += num

#         return abs(sum_A - sum_B)

# # 70
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==0 or n==1:
#             return n
#         else:
#             a,b=1,1
#             for i in range(2,n+1):
#                 a,b=b,a+b 
#             return b
            
























































































































    

        
