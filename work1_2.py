import math
x1 = int(input('Enter X1:'))
y1 = int(input('Enter Y1:'))
z1 = int(input('Enter Z1:'))
x2 = int(input('Enter X2:'))
y2 = int(input('Enter Y2:'))
z2 = int(input('Enter Z2:'))
r1 = [x1, y1, z1]
r2 = [x2, y2, z2]
distance = math.sqrt(((r1[0]-r2[0])**2)+((r1[1]-r2[1])**2)+((r1[2]-r2[2])**2))
print(distance)
