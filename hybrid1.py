
#!/usr/bin/python

## Open the file with read only permit
f = open('trace.txt')
## Read the first line 
line = f.readline()
total=0
#import numpy

count=[0]*1024
mispred_gshare=[0]*1024
mispred_1level=[0]*1024
phist_table = [0]*1024
phist_table1=[0]*1024 	#for local different history table
#local_table=[0]*128
misprediction=0
ghist=0

## If the file is not empty keep reading line one at a time
## till the file is empty

while line:
	#print line
        total+=1
	pc,action=line.split(' ');
	pc1=int(pc)
	
	#taking middle 10 bits for gshare and one level
	pc2=pc1&0x00003ff0
	pc3=pc2>>4
	#taking middle 7 bits for local
	#pc4=pc1&0x00007f0
	#pc5=pc4>>4
	
	#a=local_table[pc5]
	#a=a&0xffffffff
	#a=a<<1
	
	if 'T' in action:
		

				
		
	
		if mispred_1level[pc3] <4:
			#implement 1level
			#addr4=local_table[pc5]&0x00003ff0
			#addr5=addr4>>4	
			if mispred_1level[pc3]==4:
				mispred_gshare[pc3]=0
				phist_table[pc3]=2		

						
#mapping 10 bits of local hist table with the pattern history table

			if phist_table1[pc3]<2:
				phist_table1[pc3]+=1			
				misprediction+=1
				mispred_1level[pc3]+=1
				if phist_table1[pc3] >3:
					phist_table1[pc3]=3
			else:
				phist_table1[pc3]+=1
				if phist_table1[pc3] >3:
					phist_table1[pc3]=3
 






		else:	
		
			if mispred_gshare[pc3]==4:
				mispred_1level[pc3]=0
				phist_table1[pc3]=2
			#if mispred_1level[pc3]==4:

				#phist_table[pc3]=2
			#global
			ghist=ghist&0xffffffff
			ghist=ghist<<1
			ghist=ghist+1
			ghist=ghist&0xffffffff
		
		
		
			addr1=ghist&0x00003ff0
			addr3=addr1>>4
			addr2=addr3^pc3

			if phist_table[addr2]<2:
				phist_table[addr2]+=1			
				misprediction+=1
				mispred_gshare[pc3]+=1
				if phist_table[addr2] >3:
					phist_table[addr2]=3
			else:
				phist_table[addr2]+=1
				if phist_table[addr2] >3:
					phist_table[addr2]=3

		



	if 'N' in action:
		#count[pc3]+=1   #counter to detect gshare or local
		#local
		#a=a+1
		#a=a&0xffffffff
		#local_table[pc5]=a

		#global
		
		if mispred_1level[pc3] <4: #implement local
			#implement 1level
			#addr4=local_table[pc5]&0x00003ff0
			#addr5=addr4>>4	
			if mispred_1level[pc3]==4:
				mispred_gshare[pc3]=0
				phist_table[pc3]=0		

						
#mapping 10 bits of local hist table with the pattern history table

			if phist_table1[pc3]<2:
				phist_table1[pc3]-=1			
				
				if phist_table1[pc3] <0:
					phist_table1[pc3]=0
			else:
				phist_table1[pc3]-=1
				misprediction+=1
				mispred_1level[pc3]+=1
				if phist_table1[pc3] <0:
					phist_table1[pc3]=0
 
			
		
			
		else:			#implement gshare
			if mispred_gshare[pc3]==4:
				mispred_1level[pc3]=0
				phist_table1[pc3]=0
			#if mispred_1level[pc3]==4:
				#phist_table[pc3]=2
			#global
			ghist=ghist&0xffffffff
			ghist=ghist<<1
			ghist=ghist+1
			ghist=ghist&0xffffffff
		
		
		
			addr1=ghist&0x00003ff0
			addr3=addr1>>4
			addr2=addr3^pc3

			if phist_table[addr2]<2:
				phist_table[addr2]-=1			
				#misprediction+=1
				#mispred_gshare[pc3]+=1
				if phist_table[addr2] <0:
					phist_table[addr2]=0
			else:
				phist_table[addr2]-=1
				misprediction+=1
				mispred_gshare[pc3]+=1
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
