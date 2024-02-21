class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * n
        for booking in bookings:
            first, last, seats_reserved = booking
            seats[first - 1] += seats_reserved
            if last < n:
                seats[last] -= seats_reserved

        total_seats = 0
        for i in range(n):
            total_seats += seats[i]
            seats[i] = total_seats

        return seats
            