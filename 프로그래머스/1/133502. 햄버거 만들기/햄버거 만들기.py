def solution(ingredient):
    answer = 0
    counter = 4
    while counter <= len(ingredient):
        if ingredient[counter-4:counter] == [1, 2, 3, 1]:
            answer += 1
            del ingredient[counter-4:counter]
            counter = max(4, counter-5)
        else:
            counter += 1
                    
                
    return answer