



def part1(input : list) :
    out = 0
    for team in input :
        s1,e1 = tuple(team[0])
        s2,e2 = tuple(team[1])
        if (s2 <= s1 and e1 <= e2) or (s1 <= s2 and e2 <= e1) :
            out += 1
    return out




def part2(input) :
    pass


input = []
with open('Day4Data.txt') as f:
    input = f.readlines()
input = [a.replace("\n", "") for a in input]

input = [a.split(',') for a in input]
input = [[a.split('-') for a in pair] for pair in input]
#print(input)

a = part1(input)
print(a)

