
a =[]

for i in range(5):
    i = float(input())
    a.append(i)
    

for i in range(len(a)):
    a[i] = a[i] * a[i]

print('Tavan 2 Majmoe barabar ast ba:')

print(a)

print('Min va Max Majmome')

print(min(a))

print(max(a))
