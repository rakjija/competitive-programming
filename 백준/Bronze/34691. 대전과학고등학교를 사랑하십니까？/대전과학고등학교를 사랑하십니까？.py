import sys

while True:
    input = sys.stdin.readline().strip()

    if input == "end":
        break

    if input == "animal":
        print("Panthera tigris")
    elif input == "flower":
        print("Forsythia koreana")
    elif input == "tree":
        print("Pinus densiflora")
