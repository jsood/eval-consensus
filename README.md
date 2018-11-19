# Performance comparison for consensus algorithms
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/eval-consensus-distalgo>

### command used to generate vrpaxos.log: 
#python -m da orig.da 3 2 1 1 1

# copy-paste contents of vrpaxos.log into shiviz tool
# use following as log parsing regular expression:
(?<host>\S*) (?<clock>{.*})\ (?<event>.*)
