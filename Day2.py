your_move = {'X' : 1 , 'Y' : 2, 'Z' : 3}

fixed_win = {'X' : 0, 'Y' : 3, 'Z' : 6}


mod_winner_part2 = {
    ('A','X') : 3,
    ('A','Y') : 1,
    ('A','Z') : 2,
    ('B','X') : 1,
    ('B','Y') : 2,
    ('B','Z') : 3,
    ('C','X') : 2,
    ('C','Y') : 3,
    ('C','Z') : 1,
} 





winner = {
    ('A','X') : 3,
    ('A','Y') : 6,
    ('A','Z') : 0,
    ('B','X') : 0,
    ('B','Y') : 3,
    ('B','Z') : 6,
    ('C','X') : 6,
    ('C','Y') : 0,
    ('C','Z') : 3,
} 


def part1(moves) :
    return sum([your_move[list(move)[1]] + winner[(list(move)[0],list(move)[1])] for move in moves])

def part2(moves) :
    return sum([mod_winner_part2[(list(move)[0],list(move)[1])] + fixed_win[list(move)[1]] for move in moves])


input = []
with open('Day2Data.txt') as f:
    input = f.readlines()
input = [a.replace("\n", "") for a in input]
input = [a.split(' ') for a in input]
print(input)


print('part1: \t' + str(part1(input)))
print('part2: \t' + str(part2(input)))