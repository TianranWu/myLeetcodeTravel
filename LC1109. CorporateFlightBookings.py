class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        array = [0] * n

        for left, right, inc in bookings:
            array[left - 1] += inc
            if right < n:
                array[right] -= inc
        
        for i in range(1, n):
            array[i] += array[i - 1]
        
        return array
