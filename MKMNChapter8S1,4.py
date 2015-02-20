'''Authors: Matt Kachlik, and Megan Nilles.
This is a program that makes a set of fragments from 
a single sequence and determines the overlap
02/24/2015
'''
import random
from random import randint
import math
import collections
from collections import defaultdict

#function to determine if coverage met
def coverageMet(coverage, fold):
	i = 0
	met = True
	while (i < len(coverage) and met == True):
		if coverage[i] < fold:
			met = False
		i += 1
	return met

#function to determine overlap
def overlap (numFrag,frags):
	for i in range(0,(numfrag-1)):
		for j in range(i+1, numfrag):
			f1Len = len(frags[i])
			f2Len = len(frags[j])
			minLen = min(f1Len, f2Len)
			overlap = 0
			frag1 = frag[i]
			frag2 = frag[j]
			k = (minLen - 1)
			while (k >= 1 and overlap == 0):
				print "overlap"
				if (frag1[f1Len-k: f1Len] == frag2[0:k]):
					contig = (frag1[0:f1Len-k])+frag2
					overlap = k
					print frag1, frag2, contig, overlap
				elif (frag2[f2Len-k:f2Len])==frag1[0:k]:
					contig = frag2[0:f2Len-k] +frag1
					overlap = k
					print frag1, frag2, contig, overlap
				k -= 1
					
					
#input
data = raw_input('seq?')
seq = data
minimum = 3
maximum = 5
cFold = 3
coverage =  collections.defaultdict(int)
for i in range(0,len(seq)-1):
	coverage[seq[i]] = 0

#step #1: Generate a set fragments from the input seq
numFrag = 0
frags = collections.defaultdict(str)
while (not coverageMet(coverage, cFold)): 
	randL = randint(3,5)
	end = len(seq)-randL
	randS = randint(0,end)
	frags[numFrag] = seq[randS:randS+randL]
	numFrag += 1
	#update coverage
	for i in range(randS, randS+randL -1):
		coverage[i] += 1
print 'here'
print frags

#step 2: determine overlap
overlap(frags, numFrag)
	
