class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)  # closest to target first
        stack = []

        for pos, spd in pairs:
            time = (target - pos) / spd
            stack.append(time)

            # if current car arrives <= car ahead, it merges into that fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)