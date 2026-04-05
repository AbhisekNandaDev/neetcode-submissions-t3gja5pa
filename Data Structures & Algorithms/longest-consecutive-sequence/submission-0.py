import collections

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:

            if (num - 1) not in num_set:
                current_num = num
                current_sequence_length = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_sequence_length += 1

                longest_sequence = max(longest_sequence, current_sequence_length)

        return longest_sequence

