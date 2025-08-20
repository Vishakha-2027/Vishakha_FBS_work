def find_missing_coin(nums):
    result=0
    for num in nums:
        result^=num
    return result
coins=[5,7,2,7,5,2,5]
print("missing coin:",find_missing_coin(coins))