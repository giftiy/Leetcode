class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        boats = 0
        people.sort()
        
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        
        return boats