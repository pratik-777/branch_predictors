
#!/usr/bin/python

## Open the file with read only permit
f = open('trace.txt')
## Read the first line 
line = f.readline()
total=0
#import numpy


#phist_table = numpy.zeros(1024)
phist_table=[0]*1024
misprediction=0
ghist=0
## If the file is not empty keep reading line one at a time
## till the file is empty

while line:
	#print line
        total+=1
	pc,action=line.split(' ');

	if 'T' in action:
		ghist=ghist&0xffffffff
		ghist=ghist<<1
		ghist=ghist+1
		ghist=ghist&0xffffffff
		
		#addr=ghist&0x001ff800
		#addr2=addr>>11
			
		addr1=ghist&0x00003ff0
		addr2=addr1>>4
		#addr2=addr>>5

		if phist_table[addr2]<2:
			phist_table[addr2]+=1			
			misprediction+=1
			if phist_table[addr2] >3:
				phist_table[addr2]=3
		else:
			phist_table[addr2]+=1
			if phist_table[addr2] >3:
				phist_table[addr2]=3

	if 'N' in action:
		ghist=ghist&0xffffffff
		ghist=ghist<<1
		ghist=ghist+0
		ghist=ghist&0xffffffff
		
		
		#addr=ghist&0x00007fe0
		#addr2=addr>>5
		addr1=ghist&0x00003ff0
		addr2=addr1>>4
		#addr2=addr2>>4
		
		if phist_table[addr2]<2:
			phist_table[addr2]-=1			
			if phist_table[addr2] <0:
				phist_table[addr2]=0
		else:
			phist_table[addr2]-=1
			misprediction+=1
			if phist_table[addr2] <0:
				phist_table[addr2]=0
  	line = f.readline()	
#when actual and predicted branch matches
				
print misprediction
print total
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
