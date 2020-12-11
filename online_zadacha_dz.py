# хипстер вася
'''socks = list(map(int, input().split()))
a = socks[0]
b = socks[1]
if a > b:
    x = b
else:
    x = a
z = (a + b) - x * 2
c = z // 2
print(x, c)'''
n = int(input())
list1 = list(map(int, input().split()))
ser = 0
dim = 0
i = 0
while i < n:
    scales = max(list1[0], list1[-1])
    if i % 2 == 0:
        ser += scales
    else:
        dim += scales
    i += 1
    list1.remove(scales)
print(ser, dim)
