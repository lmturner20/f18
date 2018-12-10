import os.path
import sys

filename = sys.argv[1]
outputname = sys.argv[2]
file = open(filename, 'r')
wf = open(outputname, 'w')
for line in file:
	tokens = line.split()
	wf.write(tokens[0] + " ")
	wf.write(tokens[1] + " ")
	#opathname = tokens[2].split("/")
	#dudename = opathname[2].split("_0")[0]
	dudename = tokens[2].split("_0")[0]
	counter = 0
	for i in range(2):
		#npathname = opathname[0] + "/gninatypes/" + dudename + "_" + str(i) + ".gninatypes"
		npathname = dudename + "_" + str(counter) + ".gninatypes"
		if os.path.isfile("/net/pulsar/home/koes/jss97/DeltaG/" + npathname):
			wf.write(npathname + " ")
			counter += 1
		else:
			#npathname = opathname[0] + "/gninatypes/" + dudename + "_" + str(counter) + ".gninatypes"
			counter = 0
			npathname = dudename + "_" + str(counter) + ".gninatypes"
			wf.write(npathname + " ")
			counter += 1
	wf.write("\n")