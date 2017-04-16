
#!/usr/bin/python

## Open the file with read only permit
f = open('trace.txt')
## Read the first line 
line = f.readline()
total=0
import numpy


phist_table = numpy.zeros(1024)
misprediction=0

## If the file is not empty keep reading line one at a time
## till the file is empty

while line:
	#print line
        total+=1
	pc,action=line.split(' ');
	pc1=int(pc)
	
	#pc2=pc1&0x00007fe0
	#pc3=pc2>>5
	pc2=pc1&0x00003ff0
	pc3=pc2>>4

	if 'T' in action:
		
		if phist_table[pc3]<2:
			phist_table[pc3]+=1			
			misprediction+=1
			if phist_table[pc3] >3:
				phist_table[pc3]=3
		else:
			phist_table[pc3]+=1
			if phist_table[pc3] >3:
				phist_table[pc3]=3

	if 'N' in action:
		
		if phist_table[pc3] <2:
			phist_table[pc3]-=1			
			if phist_table[pc3] <0:
				phist_table[pc3]=0
		else:
			phist_table[pc3]-=1
			misprediction+=1
			if phist_table[pc3] <0:
				phist_table[pc3]=0
  	line = f.readline()	
#when actual and predicted branch matches
print misprediction
print total
#percent=misprediction*100/(total*1.0)
#print " Total misprediction is %.2f percentage = " %percent

f.close()


'''
#while line:
	#print line
        
pc,action=line.split(' ');
pc1=int(pc)
print pc1
print action
	#line = f.readline()	
	
f.close()
'''
