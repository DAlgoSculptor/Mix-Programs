def job_scheduling(J, D, P):
    # Combine jobs, deadlines, and profits into tuples
    jobs = list(zip(J, D, P))
    
    # Sort the jobs based on profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize variables
    scheduled_jobs = []  # Set of scheduled jobs
    total_profit = 0  # Total profit earned
    
    # Loop through each job
    for job, deadline, profit in jobs:
        # Check if scheduling the job is feasible
        if deadline > 0:
            # Schedule the job in the latest possible free slot meeting its deadline
            scheduled_jobs.append(job)
            total_profit += profit
            deadline -= 1  # Decrease the deadline
            
    return scheduled_jobs, total_profit

# Example usage
J = ["Job1", "Job2", "Job3", "Job4"]
D = [2, 1, 2, 1]  # Deadlines
P = [100, 50, 200, 80]  # Profits

scheduled_jobs, total_profit = job_scheduling(J, D, P)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", total_profit)
