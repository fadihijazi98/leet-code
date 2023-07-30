

class Solution:

    def twoSum(self, numbers, target):

        num_map = {}
        for _index in range(len(numbers)):

            complement = target - numbers[_index]
            if complement in num_map:
                return [num_map[complement], _index]

            num_map[complement] = _index
        return []
