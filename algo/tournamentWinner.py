def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {}
    for i, group in enumerate(competitions):
        team1 = group[0]
        team2 = group[1]
        if team1 not in scores.keys():
            scores[team1] = 0
        if team2 not in scores.keys():
            scores[team2] = 0
        if results[i] == 1:
            scores[team1] += 1
        else:
            scores[team2] += 1

    max_val = max(scores.items(), key=lambda x: x[1])

    return max_val[0]
