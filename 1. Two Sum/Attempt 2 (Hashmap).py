def twoSum(self, nums: list[int], target: int) -> list[int]:
    hashmap = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
        
                
sum = twoSum(0, [2,7,11,15], 9)
print(sum)
