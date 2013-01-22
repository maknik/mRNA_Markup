#! /usr/bin/env python
import sys,re
museqbox=open(sys.argv[1],'r')
blastquery=open(sys.argv[2],'r')
hits_chim=[]
hits=[]
chimera=0
#notinblastquery
f=open(sys.argv[3],'w')
#inblastquery
f=open(sys.argv[4],'w')


dane=0
lines=museqbox.read()
l=lines.split('\n')
for i in range(len(l)):
	if '------' in l[i]:
		dane=i
		break
	for i in xrange(i+1,len(l)):
		if len(l[i].split()) > 10 and l[i].split()[0] == "!Potential":
			hits_chim.append(l[i].split()[3])
		elif len(l[i].split()) > 10 and 'no_hits' not in l[i]:
			hits.append(l[i].split()[0])

for line in blastquery:
	if '>lcl' in line and hits_chim != []:
		f.close()
		if line.split()[0].split('|')[1] not in hits_chim:
			f=open(sys.argv[3],'a')
			f.write(line)
		else:
			f=open(sys.argv[4],'a')
			f.write(line)
	elif '>lcl' in line and hits_chim == [] and hits != []:
		f.close()
		if line.split()[0].split('|')[1] not in hits:
			f=open(sys.argv[3],'a')
			f.write(line)
		else:
			f=open(sys.argv[4],'a')
			f.write(line)
	else:
		f.write(line)


