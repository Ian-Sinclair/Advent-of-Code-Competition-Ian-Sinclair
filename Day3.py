def part1(rucksacks) :
    fault = 0
    for rucksack in rucksacks :
        c1 = set(list(rucksack)[int(len(rucksack)/2):])
        c2 = set(list(rucksack)[:int(len(rucksack)/2)])
        if list((c2 - (c2-c1)))[0].isupper() :
            fault += ord(list((c2 - (c2-c1)))[0])-65+27
        else : 
            fault += ord(list((c2 - (c2-c1)))[0]) - 96
    return fault



def part2Helper(triple : list) :
    c0 = set(triple[0])
    c1 = set(triple[1])
    c2 = set(triple[2])

    common = c0 - (c0 - c1)
    common = common - (common - c2)
    print(common)
    if list(common)[0].isupper() :
        return ord(list((common))[0])-65+27
    else : 
        return ord(list(common)[0]) - 96



def part2(rucksacks) :
    n=3
    team_sum = 0
    teams = [rucksacks[i:i + n] for i in range(0, len(rucksacks), n)]
    for team in teams :
        team_sum += part2Helper(team)
    return team_sum




input = []
with open('Day3Data.txt') as f:
    input = f.readlines()
input = [a.replace("\n", "") for a in input]
#print(input)

# Part 1
'''
s = part1(input)
print(s)
''' 


#  Part 2
print(part2(input))