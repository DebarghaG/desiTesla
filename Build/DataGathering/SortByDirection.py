import sys, os
import subprocess
os.system("sh SortByDirection.sh")

list1 = ["FF", "FR", "FL", "NN"]
for i in range(len(list1)):
	source1 = "/home/pi/Desi-Tesla/Build/DataGathering/" + list1[i]
	dest11 = "/home/pi/Desi-Tesla/Build/DataGathering/" + list1[i]
	files = os.listdir(source1)
	import shutil
	import numpy as np
	count = 0
	total = 0
	for f in files:
		total+=1
	
	for f in files:
		if np.random.rand(1) < 0.7:
			if (count < (total*0.3)):
				shutil.move(source1 + '/'+ f, dest11 + '/'+ f)
				count+=1
	print("Total is ", total, " Test split is ", count)

os.system("sh SplitFolders.sh")
