def solution(brown, yellow):
    answer = []
    max_h = brown//2-2
    for w in range(1, brown//2-2):
        h = max_h - w
        if w * h == yellow:
            break
    answer = [max(w, h)+2, min(w, h)+2]
    return answer