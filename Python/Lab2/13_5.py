def sort_team_points(point):
    return point[1]


def sort_team_alphabet(team):
    return team


n = int(input())
results_list = []
for i in range(n):
    team_name = input()
    team_points = int(input())
    results_list.append((team_name, team_points))
results_list.sort(key=sort_team_points)
final_list = []
elimination_list = []
for result in results_list:
    if results_list.index(result) >= len(results_list) // 2:
        final_list.append(result[0])
    else:
        elimination_list.append(result[0])
final_list.sort(key=sort_team_alphabet)
elimination_list.sort(key=sort_team_alphabet)
print('\n'.join(final_list))
print('\n'.join(elimination_list))
