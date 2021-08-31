class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        array = [0] * n

        # for left, right, inc in bookings:
        #     nums[left - 1] += inc
        #     if right < n:
        #         nums[right] -= inc

        for left, right, inc in bookings:
            array[left - 1] += inc
            if right < n:
                array[right] -= inc
        
        # array = array[0] + [array[i-1]+array[i] for i in range(1,n)]
        for i in range(1, n):
            array[i] += array[i - 1]
        
        return array
