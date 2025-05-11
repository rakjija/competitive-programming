import sys

msg_dict = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later",
}

while True:
    S = sys.stdin.readline().rstrip("\n")
    if S in msg_dict.keys():
        print(msg_dict[S])
    else:
        print(S)
    if S == "TTYL":
        break
