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

'''
coverageMet
checks if the coverage of all the sequences are met by checking
against the fold
'''
def coverageMet(coverage, fold):
	i = 0
	met = True
	while (i < len(coverage) and met == True):
		if(coverage[i] < fold):
			met = False
		i += 1
	return met

'''
overlap
determines if there is overlap and then determines where the overlap is
by iterating through the fragments then from the largest to the smallest 
possible overlap 
'''
def overlap (numFrag,frags):
	for i in range(0,numFrag-1):
		for j in range(i+1, numFrag):
			f1Len = len(frags[i])
			f2Len = len(frags[j])
			minLen = min(f1Len, f2Len)
			overlap = 0
			frag1 = frags[i]
			frag2 = frags[j]
			k = (minLen - 1)
			#starting from the highest number of overlap to lowest possible overlap 
			while (k >= 1 and overlap == 0):
				#comapring suffix of frag1 to prefix of frag2
				if (frag1[f1Len-k: f1Len] == frag2[0:k] and not frag1[0:k] in frag2):
					contig = (frag1[0:f1Len-k])+frag2
					overlap = k
					print frag1, frag2, contig, overlap				
				elif (frag2[f2Len-k:f2Len]==frag1[0:k] and frag1[f1Len-k: f1Len] not in frag2):
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
	coverage[i] = 0

#step #1: Generate a set fragments from the input seq
numFrag = 0
frags = collections.defaultdict(str)
while (coverageMet(coverage, cFold) == False): 
	randL = randint(minimum,maximum)
	randS = randint(0,len(seq)-randL)
	frags[numFrag] = seq[randS:randS+randL]
	numFrag += 1
	#update coverage
	for i in range(randS, randS+randL -1):
		coverage[i] += 1


#step 2: determine overlap
overlap(numFrag,frags)
	
