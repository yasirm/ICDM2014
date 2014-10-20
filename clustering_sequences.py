
import sys
import random
import os
import glob

def main():
	
	pp = sys.argv[1]
	
	directory=pp+'/mixedClusters'
	os.chdir(directory)
	files=glob.glob('*.txt')
	for ff in files:
		os.remove(ff)
	
	fid = pp+'/seq_file.txt'
	clustersNb = int(sys.argv[2])
	f = open(fid,'r')
	item_id = -1
	clFile = open(pp+'/mixedClusters/temp.txt','w')
	
	for line in f:
		l = line.strip().split(' ')
		cluster = random.randrange(1,clustersNb+1)
		clFile = open(pp+'/mixedClusters/withDelaysClus_'+str(cluster)+'.txt', 'a')
		
		for ele in l:
			clFile.write(ele+' ')
		clFile.write('\n')
	
	clFile.close()
	#end


if __name__=='__main__':
     main()
