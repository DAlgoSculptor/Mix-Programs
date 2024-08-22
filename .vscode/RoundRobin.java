//Implementation of RR scheduling

public class RoundRobin 
{
	// processes
	static void findWaitingTime(int processes[], int n,int bt[], int wt[], int quantum)
	{
		
		// burst times.
		int rem_bt[] = new int[n];
		for (int i = 0 ; i < n ; i++)
			rem_bt[i] = bt[i];
	
		int t = 0; // Current time
	
		
		
		while(true)
		{
			boolean done = true;
	
			
			for (int i = 0 ; i < n; i++)
			{
				
				if (rem_bt[i] > 0)
				{
					done = false; 
	
					if (rem_bt[i] > quantum)
					{
						
						t += quantum;
	
						
						rem_bt[i] -= quantum;
					}
	
					
					else
					{
						
						t = t + rem_bt[i];
	
						
						wt[i] = t - bt[i];
	
					
						rem_bt[i] = 0;
					}
				}
			}
	
			// If all processes are done
			if (done == true)
			break;
		}
	}
	
	// Method to calculate turn around time
	static void findTurnAroundTime(int processes[], int n,
							int bt[], int wt[], int tat[])
	{
	
		for (int i = 0; i < n ; i++)
			tat[i] = bt[i] + wt[i];
	}
	

	static void findavgTime(int processes[], int n, int bt[],
										int quantum)
	{
		int wt[] = new int[n], tat[] = new int[n];
		int total_wt = 0, total_tat = 0;
	
	
		findWaitingTime(processes, n, bt, wt, quantum);
	
		findTurnAroundTime(processes, n, bt, wt, tat);
	
	
		System.out.println("PN " + " B " +
					" WT " + " TAT");
	
		
		for (int i=0; i<n; i++)
		{
			total_wt = total_wt + wt[i];
			total_tat = total_tat + tat[i];
			System.out.println(" " + (i+1) + "\t\t" + bt[i] +"\t " +
							wt[i] +"\t\t " + tat[i]);
		}
	
		System.out.println("Average waiting time = " +
						(float)total_wt / (float)n);
		System.out.println("Average turn around time = " +
						(float)total_tat / (float)n);
	}
	
	// Driver Method
	public static void main(String[] args)
	{
		// process id's
		int processes[] = { 1, 2, 3};
		int n = processes.length;
	
		// Burst time of all processes
		int burst_time[] = {10, 5, 8};
	
		// Time quantum
		int quantum = 2;
		findavgTime(processes, n, burst_time, quantum);
	}
}
