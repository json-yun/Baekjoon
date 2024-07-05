def solution(n, results):
    def add_result():
        for winner, loser in results:
            wins[winner].add(loser)
            loses[loser].add(winner)
            for another_winner in loses[winner]:
                wins[another_winner].add(loser)
                loses[loser].add(another_winner)
            for another_loser in wins[loser]:
                loses[another_loser].add(winner)
                wins[winner].add(another_loser)
    wins = {i+1: set() for i in range(n)}
    loses = {i+1: set() for i in range(n)}
    results.sort(key=lambda x: x, reverse=False)
    add_result()
    # results.sort(key=lambda x: x, reverse=True)
    add_result()

    answer = [len(i) + len(j) for i, j in zip(wins.values(), loses.values())].count(n-1)
    return answer 