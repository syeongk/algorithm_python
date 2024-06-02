r = []

for i in range(10):
    num = int(input())
    r.append(num%42)

print(len(set(r)))
