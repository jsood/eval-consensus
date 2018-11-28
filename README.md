# Performance comparison for consensus algorithms
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/eval-consensus-distalgo>

## Details of implementation:
1. Driver Programs: We are using individual driver programs written in DistAlgo to compare the implementations. The drivers run the implementations with a varied set of input parameters, and also capture the messages (containing memory consumption data) sent from the implementations. 
Raft Driver: (https://github.com/unicomputing/eval-consensus-py/blob/master/monitor_raft.da)
vrPaxos Driver: (https://github.com/unicomputing/eval-consensus-py/blob/master/stats_monitor.da)

2. Changes in consensus algorithms Implementations: We have used the DistAlgo implementation of vrPaxos (https://github.com/unicomputing/eval-consensus-py/blob/master/orig.da) and raft (https://github.com/unicomputing/eval-consensus-py/blob/master/raft.da). We have modified these files to capture the memory consumption data, which is captured by the psutil library in python. We are sending these data to the drivers, and calculating the average memory consumption details there.

3. Central Monitor: To operate and control all the drivers simultaneously, we have a monitor program(Github link: https://github.com/unicomputing/eval-consensus-py/blob/master/driver.da). The monitor is responsible to run the drivers, get the performance metrics out of them, and put them into performance visualization charts. Invoke ntuitive monitor interface inside eval-consensus-py directory from command line on a system having python and distalgo installed as: python -m da driver.da

4. Central Logger: We have create a central logger system (GitHub link: https://github.com/unicomputing/eval-consensus-py/blob/master/logger.py) to record and dump the performance logs externally.

5. Visualizations: As of now, we have created a file to externally read the log files and generate the graphs using the matplotlib library in python. The code for Chart generator is given in Github link: https://github.com/unicomputing/eval-consensus-py/blob/master/Perf_Vis.da. We are planning to execute this from monitor program to reduce the extra number of files. A sample set of charts can be found at: https://github.com/unicomputing/eval-consensus-py/blob/master/perf_vis.pdf.
