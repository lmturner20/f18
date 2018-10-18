import os.path

file = open('alldude.types', 'r')
wf = open('dude_9_2.types', 'w')
for line in file:
	tokens = line.split()
	wf.write(tokens[0] + " ")
	wf.write(tokens[1] + " ")
	opathname = tokens[2].split("/")
	dudename = opathname[2].split("_0")[0]
	counter = 0
	for i in range(9):
		npathname = opathname[0] + "/gninatypes/" + dudename + "_" + str(i) + ".gninatypes"
		if os.path.isfile("/net/pulsar/home/koes/dkoes/DUDe/" + npathname):
			wf.write(npathname + " ")
			counter = i
		else:
			npathname = opathname[0] + "/gninatypes/" + dudename + "_" + str(counter) + ".gninatypes"
			wf.write(npathname + " ")
	wf.write("\n")