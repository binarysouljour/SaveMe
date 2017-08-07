#!/usr/bin/python

import os, time, math, requests, json


def getsignal():
		i=6
		signal=""
		while(i<len(sig)):
			signal+=(sig[i])
			i+=1
		return signal

def getfrequency():
	j=10
	frequency=""
	while(j<len(freq)):
		frequency+=(freq[j])
		j+=1
	frequency=float(frequency)
	frequency*=1000
	return int(frequency)

vals=[]


def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

while True:

	sig=[]
	freq=[]
	os.system("iwconfig wlan0 | grep =- > sig.txt")
	os.system("iwconfig wlan0 | grep Frequency > freq.txt")
	sigfile=open("sig.txt",'r')
	freqfile=open("freq.txt",'r')
	for sigcolumns in (sigraw.strip().split() for sigraw in sigfile):
		pass
	for freqcolumns in (freqraw.strip().split() for freqraw in freqfile):
		pass

	for freqkey in freqcolumns[1]:
		freq.append(freqkey)

	for sigkey in  sigcolumns[3]:
		sig.append(sigkey)

	#time.sleep(1)
	dist = (27.55 * math.log10(getfrequency())+math.fabs(float(getsignal()))/20)
	distmtr = math.pow(10,dist)

	sigfile.close()
	freqfile.close()
	#deleteContent(sigfile)
	#deleteContent(freqfile)
	f = open('sig.txt', 'w')
	f.close()
	g = open('freq.txt','w')
	f.close()
	#os.system("rm sig.txt && rm freq.txt")
	#time.sleep(1)

	fdistmtrs=str(float(distmtr))
	for fdistmtr in fdistmtrs:
		vals.append(fdistmtr)

	final = int(vals[len(vals)-2]+vals[len(vals)-1]+vals[0])/10.0
	#print vals
	del vals[:]
	time.sleep(3)
	requests.post('http://192.168.43.69:3000/get', data={'val':final})
	#requests.post('http://192.168.43.69:3000/get', data=str(final))
	print final
