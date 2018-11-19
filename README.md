# Performance comparison for consensus algorithms
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/eval-consensus-distalgo>

list of pending things (TODOs) in orig.da for shiviz visualization:
1. clock not implemented for all processes. For now it is added in just replica and client
2. also need to add a dictionary in each process to store process-clock info of all the other processes it has received a message from. This is done to ensure we get logs in format which shivix needs in, along with maintaining scalability.
3. for now manually delete vrpaxos.log file before each run. Need to find out how logger can create a new file/truncate the file at starting of each run.

command used to generate vrpaxos.log: 
python -m da orig.da 3 2 1 1 1

copy-paste contents of vrpaxos.log into shiviz tool. Use following as log parsing regular expression:
(?<host>\S*) (?<clock>{.*})\ (?<event>.*)
