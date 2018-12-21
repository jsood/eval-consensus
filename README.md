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

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### For adding a new consensus implementation in the framework

1. Understand the underlying algorithm: We need to study how the consensus happens. This will help us to understand the underlying protocols, and also explain the number and type of the messages passed at each iteration. As and when the performance metrics, generated from the driver programs, would give us charts and graphs for varied input parameters, this understanding of the algorithms would help us to draw interesting inferences from them. 

2. Necessary modifications in the implementation: 

Define 'self.proc = psutil.Process(od.getpid())' in the setup of each process in the new implementation. Also, copy below function "record_memory_consumed()" to each process in the implementation, just like we have defined it inside orig.da and raft.da. 

def record_memory_consumed():
    send(('memory', self, proc.memory_info()[1]/1000), to=parent())

Now, inside the new implementation, in each function of all processes, call "record_memory_consumed()" once inside each process.

3. We need to write the driver code to extract performance metrics of running times and memory consumption as described now. We have introduced a new DistAlgo file "monitor_stub.da". This stub file has specific 5 (five) places where code changes has to be made to create a new driver for any DistAlgo/ Python implementation. For ease of understanding, all these places have been demarcated in the stub code file with the comment "custom user code:".

    a. Going by the order of arrangement, firstly we need to modify the methods "start_module" and "end_module" to start and end all the participating components (processes, servers etc.). We have added two sample components (processes, clients) in each of these modules to show how this has to be done.
    b. At the next step, we have to start and setup all the constituent processes and components, and vary their values accrodingly with corresponding user inputs. 
    c. After this, we have kept a place to pass on appropriate parameters (as set up on step c) into the start_module method and start off the driver.
    d. We have also created place after that where we send a message "done" to the parent process to inform that the performance run has been completed.
    e. Lastly, we have a place for setting up and starting the stat processes for n repetitions. 

4. We now need to run Perf_Vis.da. It automatically reads the log files and generate performance comparison graphs.
