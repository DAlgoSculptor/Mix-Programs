import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Process {
    int id;
    int arrivalTime;
    int burstTime;
    int waitingTime;
    int turnaroundTime;

    public Process(int id, int arrivalTime, int burstTime) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.burstTime = burstTime;
        this.waitingTime = 0;
        this.turnaroundTime = 0;
    }
}

public class CPUScheduler {
    public static void main(String[] args) {
        List<Process> processes = new ArrayList<>();
        processes.add(new Process(1, 0, 8));
        processes.add(new Process(2, 1, 4));
        processes.add(new Process(3, 2, 9));
        processes.add(new Process(4, 3, 5));

        simulateFCFS(processes);

        printResults(processes);
    }

    public static void simulateFCFS(List<Process> processes) {
        Collections.sort(processes, Comparator.comparingInt(p -> p.arrivalTime));

        int currentTime = 0;
        for (Process process : processes) {
            process.waitingTime = currentTime - process.arrivalTime;
            process.turnaroundTime = process.waitingTime + process.burstTime;
            currentTime += process.burstTime;
        }
    }

    public static void printResults(List<Process> processes) {
        double avgTurnaroundTime = 0;
        int maxWaitingTime = Integer.MIN_VALUE;
        int maxBurstTime = Integer.MIN_VALUE;

        System.out.println("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time");
        for (Process process : processes) {
            System.out.printf("%d\t\t%d\t\t\t%d\t\t\t%d\t\t\t%d%n",
                    process.id, process.arrivalTime, process.burstTime,
                    process.waitingTime, process.turnaroundTime);

            avgTurnaroundTime += process.turnaroundTime;
            maxWaitingTime = Math.max(maxWaitingTime, process.waitingTime);
            maxBurstTime = Math.max(maxBurstTime, process.burstTime);
        }

        avgTurnaroundTime /= processes.size();

        System.out.println("\nAverage Turnaround Time: " + avgTurnaroundTime);
        System.out.println("Maximum Waiting Time: " + maxWaitingTime);
        System.out.println("Maximum Burst Time: " + maxBurstTime);
    }
}
