cards = input().split()
team_a = []
team_b = []
terminated = False
for card in cards:
    team, number = card.split("-")
    if team == "A":
        team_a.append(number)
    elif team == "B":
        team_b.append(number)
    if 11 - len(set(team_a)) < 7 or 11 - len(set(team_b)) < 7:
        terminated = True
        break

print(f"Team A - {11 - len(set(team_a))}; Team B - {11 - len(set(team_b))}")

if terminated:
    print("Game was terminated")

