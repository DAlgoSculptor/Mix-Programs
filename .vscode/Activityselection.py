def activity_selection(start_times, end_times):
    n = len(start_times)
    
    activities = [(start_times[i], end_times[i], i) for i in range(n)]
    
    activities.sort(key=lambda x: x[1])
    
    result = [activities[0]]
    
    for i in range(1, n):
        if activities[i][0] >= result[-1][1]:
            result.append(activities[i])
    
    selected_activities = [activity[2] for activity in result]
    
    return selected_activities

start_times = [1, 3, 0, 5, 8]
end_times = [2, 4, 6, 7, 9]

selected_activities = activity_selection(start_times, end_times)

print("Selected Activities:", selected_activities)