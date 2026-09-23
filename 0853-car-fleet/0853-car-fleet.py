class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        prev_time = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            # If this car takes longer, it forms a new fleet
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets
