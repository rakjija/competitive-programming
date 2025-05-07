import sys

for line in sys.stdin:
    line = line.rstrip("\n")

    result = []
    for c in line:
        if c == "i":
            result.append("e")
        elif c == "e":
            result.append("i")
        elif c == "I":
            result.append("E")
        elif c == "E":
            result.append("I")
        else:
            result.append(c)
    print("".join(result))
