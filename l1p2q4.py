def max_activities(activities):
    activities.sort(key=lambda x: x[1])  # Sort activities by finish time
    selected_activities = [activities[0]]  # Select the first activity

    for i in range(1, len(activities)):
        if activities[i][0] >= selected_activities[-1][1]:  # Check if the next activity can be performed
            selected_activities.append(activities[i])

    return selected_activities

# Input activities as pairs of start and finish times
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

result = max_activities(activities)
print("Maximum number of activities performed by a single person:")
print(result)
