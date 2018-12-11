# Performance comparison for consensus algorithms
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/eval-consensus-distalgo>

## Steps to Run

### For Performance Comparison

a. driver_test_perf.da - Run driver_perf.da using "python -m da driver_test_perf.da". It will give us2 options to choose implementations to run - DistAlgo Paxos and DistAlgo Raft.

b. On entering 1,  it asks for DistAlgo Paxos to choose from varying number of acceptors andnumber of requests per client.  On entering ’a’,  it runs DistAlgo Paxos for varying range ofacceptors. On entering ’b’, it runs DistAlgo Paxos for varying range of requests per client.

c. On entering 2, it asks for DistAlgo Raft to choose from varying number of servers and numberof requests per client.  On entering ’a’, it runs DistAlgo Raft for varying range of servers.  On entering ’b’, it runs DistAlgo Raft for varying range of requests per client.

d. The default values for paxos are 5 acceptors, 4 replicas, 2 leaders, 3 clients, 3 requests and 8 runs.Default values for raft are 5 servers, 3 clients, 3 requests, 3000 timeout and 8 runs. All runs bydefault are without leader crash.

e. Two log files named raftlogfile.csv and paxoslogfile.csv will be generated.

f. Run Perf.Vis.da and 3 pdf files will be generated with names output1.pdf,  output2.pdf andoutput3.pdf will be generated containing the performance comparison visualizations

### For ShiViz Logs

a. driver.daRun driver.da using "python -m da driver.da".  It will give us 2 options to chooseimplementations to run - DistAlgo Paxos and DistAlgo Raft.

b. For example: Choose 1 for running DistAlgo Paxos for generating logs for Shiviz. Enter 3 2 1 1 11 for count of accpetors, replicas, leaders, clients, operations and runs respectively.•A file named vrpaxos-buffer.log file is generated.

c. Open "https://bestchai.bitbucket.io/shiviz/" and click on ’Try out on ShiViz’, upload the logfile "vrpaxos-buffer.log" and click on Visualize.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Details of implementation:
1. Monitor Programs: We have a monitor program per consensus implementation written in DistAlgo to compare the implementations. The monitors run the implementations with a varied set of input parameters, and also capture the messages (containing memory consumption data) sent from the implementations. 
vrPaxos Monior: (https://github.com/unicomputing/eval-consensus-py/blob/master/stats_monitor.da)
Raft Monitor: (https://github.com/unicomputing/eval-consensus-py/blob/master/monitor_raft.da)

2. Changes in consensus algorithms Implementations: We have used the DistAlgo implementation of vrPaxos (https://github.com/unicomputing/eval-consensus-py/blob/master/orig.da) and raft (https://github.com/unicomputing/eval-consensus-py/blob/master/raft.da). We have modified these files to capture the memory consumption data, which is captured by the psutil library in python. We are sending these data to the drivers, and calculating the average memory consumption details there. Both the implementations have a separate version with one leader crashing. Paxos:(https://github.com/unicomputing/eval-consensus-py/blob/master/orig_failure.da) and Raft:(https://github.com/unicomputing/eval-consensus-py/blob/master/raft_failure.da).

3. Central Driver: To operate and control all the monitors, we have a driver program (Github link: https://github.com/unicomputing/eval-consensus-py/blob/master/driver.da). The monitor is responsible to run the monitors, get the performance metrics out of them, and put them into performance visualization charts. Invoke intuitive driver interface inside eval-consensus-py directory from command line on a system having python and distalgo installed as: python -m da driver.da

4. Central Logger: We have create a central logger system (GitHub link: https://github.com/unicomputing/eval-consensus-py/blob/master/logger.py) to record and dump the shiviz logs externally.

5. Visualizations: As of now, we have created a file to externally read the log files and generate the graphs using the matplotlib library in python. The code for Chart generator is given in Github link: https://github.com/unicomputing/eval-consensus-py/blob/master/Perf_Vis.da. We are planning to execute this from monitor program to reduce the extra number of files. A sample set of charts can be found at: https://github.com/unicomputing/eval-consensus-py/blob/master/perf_vis.pdf.

