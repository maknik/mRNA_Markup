#! /usr/bin/env python
import sys
allseq=open(sys.argv[1],'r')
VC_mRNA=open(sys.argv[2],'r')
BC_mRNA=open(sys.argv[3],'r')
RA_mRNA=open(sys.argv[4],'r')
FL_mRNA=open(sys.argv[5],'r')
not_FL_mRNA=open(sys.argv[6],'r')
PC_mRNA=open(sys.argv[7],'r')
not_PC_mRNA=open(sys.argv[8],'r')
AA_mRNA=open(sys.argv[9],'r')
CD_mRNA=open(sys.argv[10],'r')
not_CD_mRNA=open(sys.argv[11],'r')
summary=open(sys.argv[12],'w')

def count_sequences(seq_file):
	accumulator=0
	for line in seq_file:
		if '>' in line:
			accumulator += 1
	return str(accumulator)

summary.write("mRNAmarkup Report\n\n\n")
summary.write("Number of input sequences:                            "+count_sequences(allseq)+"\n")
summary.write("Number of potential vector-contaminated sequences:    "+count_sequences(VC_mRNA)+"\n")
summary.write("Number of potential bacterial-contaminated sequences: "+count_sequences(BC_mRNA)+"\n")
summary.write("Number of sequences matching the ReferenceDB:         "+count_sequences(RA_mRNA)+"\n")
summary.write("  Number of potential full-length coding sequences:   "+count_sequences(FL_mRNA)+"\n")
summary.write("  Non-qualifying sequences:                           "+count_sequences(not_FL_mRNA)+"\n")
summary.write("    Number of potential chimeric sequences:           "+count_sequences(PC_mRNA)+"\n")
summary.write("    Non-qualifying sequences:                         "+count_sequences(not_PC_mRNA)+"\n")
summary.write("Number of sequences matching the AllProteinDB:        "+count_sequences(AA_mRNA)+"\n")
summary.write("Number of sequences matching the ProteinDomainDB:     "+count_sequences(CD_mRNA)+"\n")
summary.write("Number of remaining sequences:                        "+count_sequences(not_CD_mRNA)+"\n")
