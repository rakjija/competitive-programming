import sys

seminar_position = {
    "Algorithm": "204",
    "DataAnalysis": "207",
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": "501",
    "TestStrategy": "105",
}

N = int(sys.stdin.readline().rstrip("\n"))

for _ in range(N):
    seminar = sys.stdin.readline().rstrip("\n")
    print(seminar_position[seminar])
