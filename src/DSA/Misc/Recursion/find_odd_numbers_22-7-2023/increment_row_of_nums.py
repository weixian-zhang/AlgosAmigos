

def given_a_list_of_nums_generate_consecutive_nums(nums: list[int], limit: int):
    
    def recursion(idx: int, result: list[int], *args):
        
        # base case
        if idx > len(nums) - 1:
            result.append(list(args))
            return
        
        for x in range(limit):
            recursion(idx + 1, result, *args + (nums[idx] + x,))


    result = []
    recursion(0, result)
    return result


def generate_consec_nums_by_num_of_digits(digits: int, limit: int):
    
    def recursion(nums: list[int], idx: int, result: list[int], consecCombo: tuple):
        
        if idx > len(nums) - 1:
            result.append(list(consecCombo))

        else:

            for x in range(limit):
                recursion(nums, idx + 1, result, consecCombo + (nums[idx] + x,))

    nums = [1 for x in range(digits)]

    result = []
    recursion(nums, 0, result, tuple())
    return result




print(generate_consec_nums_by_num_of_digits(2, 5))
# given_a_list_of_nums_generate_consecutive_nums([1,1,1,1], 6)