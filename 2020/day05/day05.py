# Advent of Code Day 5


if __name__ == "__main__":
    input_file = 'input05.txt'
    with open(input_file) as f:
        passes = f.read().splitlines()

    seat_ids = []
    for boarding_pass in passes:
        rows = list(range(128))
        row_data = boarding_pass[:7]
        for c in row_data:
            if c == 'F':
                rows = rows[:len(rows) // 2]
            if c == 'B':
                rows = rows[len(rows) // 2:]

        seats = list(range(8))
        seat_data = boarding_pass[7:]
        for c in seat_data:
            if c == 'L':
                seats = seats[:len(seats) // 2]
            if c == 'R':
                seats = seats[len(seats) // 2:]

        seat_ids.append(rows[0] * 8 + seats[0])

    # Part One
    print(max(seat_ids))

    # Part Two
    full_plane = set(range(min(seat_ids), max(seat_ids)))
    print(full_plane.difference(set(seat_ids)))
