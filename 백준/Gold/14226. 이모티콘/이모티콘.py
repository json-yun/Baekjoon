from collections import deque

S = int(input())

q = deque()
q.append((1, 1, 1))
visited = {}
while True:
    now, clipboard, time = q.popleft()
    if now == S:
        print(time)
        break

    if (now, clipboard) in visited:
        continue
    visited[(now, clipboard)] = True
    if now != clipboard:
        q.append((now, now, time+1))
    if now < S:
        q.append((now+clipboard, clipboard, time+1))
    if now > 0:
        q.append((now-1, clipboard, time+1))