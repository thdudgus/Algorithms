n = int(input())
people = []

for i in range(n):
    tmp = input().split(' ')
    people.append(tmp)
people.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(people[-1][0])
print(people[0][0])
