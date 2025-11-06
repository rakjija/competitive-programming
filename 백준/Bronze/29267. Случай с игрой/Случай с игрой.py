import sys

n, k = map(int, sys.stdin.readline().split())

cur_bullet = 0
saved_bullet = 0
for _ in range(n):
    action = sys.stdin.readline().strip()
    
    if action == 'save':
        saved_bullet = cur_bullet
    elif action == 'load':
        cur_bullet = saved_bullet
    elif action == 'shoot':
        cur_bullet -= 1
    elif action == 'ammo':
        cur_bullet += k
    
    print(cur_bullet)
