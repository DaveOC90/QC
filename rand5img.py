## random 5 Images
### for final image orientation, crosscheck with AFNI or FSL
def rand5img():

	import os
	import nibabel as nib
	import matplotlib.pyplot as plt
	import numpy as np
	import random
	from image_grab import midslice
	from img5plot import plot_5images
	import re
	import code


	direc='/home/data/Incoming/CORR/ExtractedArchives/Organized_Data/ipcas_beijing_liu/'#raw_input('Please Enter Directory (Full Path) (/home/data/..):') #/home/data/Incoming/CORR/ExtractedArchives/
	sublist='/home/data/Incoming/CORR/ExtractedArchives/Subject_Lists/ipcas_beijing_liu2_sublist.txt'#raw_input('Please Enter the Subject List (Full Path) (/home/data/..):') #/home/data/Incoming/CORR/ExtractedArchives/
	outputname='/home/data/Incoming/CORR/ExtractedArchives/LR_Orientation_Screenshot_Script/ipcas_beijing_liu_anat_screenshots.png'#raw_input('Please Enter the Desired File Output Name with Extension and Output Direc (/home/data/../file.png):')
	foldname='IPCAS Beijing Liu'#raw_input('Please Enter the Site Indentifier:')
	filetype='anat'#raw_input('Please Enter the Image Type Required (rest/anat):')


	subnum=[]
	sesh_num=[]
	img_mid=[]
	img_voxels=[]
	for i in range(0,5):
		if filetype == "rest":
			os.chdir(direc) #direc
			randsub=random.choice(os.listdir("."))
			subnum.append(randsub)
			print randsub
			os.chdir('./'+randsub+'/')
			rand_sesh=random.choice(os.listdir('.'))
			sesh_num.append(rand_sesh)
			print rand_sesh
			os.chdir('./'+rand_sesh+'/rest_1/')
			imgs=os.listdir('.')
			img_ip=imgs[0]
			img_op1, img_op2=midslice(img_ip, filetype)
			img_mid.append(img_op1)
			img_voxels.append(img_op2)
		if filetype == "anat":
			os.chdir(direc) #direc
			randsub=random.choice(os.listdir("."))
			subnum.append(randsub)
			print randsub
			os.chdir('./'+randsub+'/')
			rand_sesh=random.choice(os.listdir('.'))
			sesh_num.append(rand_sesh)
			print rand_sesh
			os.chdir('./'+rand_sesh+'/anat_1/')
			imgs=os.listdir('.')
			img_ip=imgs[0]
			img_op1, img_op2=midslice(img_ip, filetype)
			img_mid.append(img_op1)
			img_voxels.append(img_op2)

	
	org_sub=[]
	for element in subnum:
		#org_sub.append(element)
		with open(sublist) as tfile: #sublist
	  		for line in tfile:
				subdeets=re.findall(r'\w+', str(line))
				if element[2:7] in subdeets[1]:
					#print subdeets
					org_sub.append(subdeets[0])
	
	plot_titles=[]
	for i in range(0,5):
		title=str(sesh_num[i]+' '+org_sub[i])
		plot_titles.append(title)
	
	
	plot_5images(img_mid, plot_titles, outputname, foldname, img_voxels)
