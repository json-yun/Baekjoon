def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    last_cam = -30001
    for route in routes:
        if not is_in(route, last_cam):
            last_cam = route[1]
            answer += 1
    return answer

def is_in(route, cam):
    return (route[0] <= cam <= route[1])