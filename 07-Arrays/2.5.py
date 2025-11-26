# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    rows = len(seats)
    cols = len(seats[0])
    return rows * cols

def seats_available(seats):
    count = 0
    for row in seats:
        for place in row:
            if place == 'A':
                count += 1
    return count

def seats_booked(seats):
    count = 0
    for row in seats:
        for place in row:
            if place == 'B':
                count += 1
    return count

def seat_status(seats, row, place):
    # row, place – liczone od 1
    value = seats[row - 1][place - 1]
    if value == 'A':
        return "available"
    else:
        return "booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
