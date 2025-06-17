import sys

depths = []
for i in range(4):
    depths.append(int(sys.stdin.readline()))

if depths[0] < depths[1] < depths[2] < depths[3]:
    print("Fish Rising")
elif depths[0] > depths[1] > depths[2] > depths[3]:
    print("Fish Diving")
elif depths[0] == depths[1] == depths[2] == depths[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")
