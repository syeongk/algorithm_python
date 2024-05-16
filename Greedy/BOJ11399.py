n = int(input())
li = list(map(int, input().split()))
new_li = sorted(li)

my_time = 0
total = 0

for i in range(n):
    my_time += new_li[i]
    total += my_time

print(total)
