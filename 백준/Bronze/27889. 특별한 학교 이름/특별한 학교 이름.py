import sys

schools = {
    "NLCS": "North London Collegiate School",
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School",
    "SJA": "St. Johnsbury Academy",
}

N = sys.stdin.readline().strip()

print(schools[N])
