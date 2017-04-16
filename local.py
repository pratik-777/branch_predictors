
#!/usr/bin/python

## Open the file with read only permit
f = open('trace.txt')
## Read the first line 
line = f.readline()
total=0
#import numpy


phist_table = [0]*1024
misprediction=0
ghist=0
local_table=[0]*128

## If the file is not empty keep reading line one at a time
## till the file is empty

while line:
	#print line
        total+=1
	pc,action=line.split(' ');
	pc1=int(pc)
	
#taking middle 7 bits of pc
	
	pc1=pc1&0x000007f0
	pc3=pc1>>4
	
#mapping the 7 bits with the local table
	
	
#shifting and inserting according to the action T or N
	a=local_table[pc3]
	a=a&0xffffffff
	a=a<<1
	if 'T' in action:
		
		a=a+1
		a=a&0xffffffff
		local_table[pc3]=a
		#local_table[pc3]=a

# taking middle 10 bits from local history table
	
		
		#addr2=addr>>11
		addr=local_table[pc3]&0x00003ff0
		addr2=addr>>4
#mapping 10 bits of local hist table with the pattern history table

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
		a=a+0
		a=a&0xffffffff
		local_table[pc3]=a

# taking middle 10 bits from local history table
	
		#addr=local_table[pc3]&0x001ff800
		#addr2=addr>>11
		addr=local_table[pc3]&0x00003ff0
		addr2=addr>>4
		
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


