
# Given an array of ints, return True if the array is length 1 or more,
# and the first element and the last element are equal.
#
#
# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True


# Read input numbers
# Determine if len(array)>1, and if array[0] == array[-1]
    # Return True
# Else
    # Return False

def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False


# Their solution: (didn't use if/else, had function check directly in return)
def same_first_last(nums):
    return (len(nums) >= 1 and nums[0] == nums[-1])

