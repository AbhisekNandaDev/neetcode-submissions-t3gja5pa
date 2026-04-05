import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize hashmaps (dictionaries of sets in Python)
        # rows[i] will store numbers seen in row i
        rows = collections.defaultdict(set)
        # cols[j] will store numbers seen in column j
        cols = collections.defaultdict(set)
        # boxes[(r // 3, c // 3)] will store numbers seen in the 3x3 sub-box
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # Skip empty cells
                if num == '.':
                    continue

                # Check row validity
                if num in rows[r]:
                    return False
                rows[r].add(num)

                # Check column validity
                if num in cols[c]:
                    return False
                cols[c].add(num)

                # Check 3x3 sub-box validity
                box_index = (r // 3, c // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

        # If no duplicates found after checking all cells
        return True