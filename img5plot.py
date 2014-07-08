### Not reliable for final image orientation, crosscheck with AFNI or FSL
def plot_5images(imgarray, titlearray, outputname, foldname, img_voxels):

	import os
	import nibabel as nib
	import matplotlib.pyplot as plt
	import numpy as np
	import matplotlib.cm as cm
	import code


	img_aspect=[]

	for i, element in enumerate(imgarray):
		img_shape=imgarray[i].shape
		curr_voxels=img_voxels[i]
		img_aspect_temp=float(img_shape[0]/curr_voxels[0])/float(img_shape[1]/curr_voxels[1])
		img_aspect_temp=round(img_aspect_temp*100)
		img_aspect.append(img_aspect_temp)

	 
	fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(ncols=5, figsize=(20,7))

	
	
	#for i,element in enumerate(imgarray):
	#	name="ax%s"%(str(i+1))
	#	print name
	#	globals()[name].imshow(imgarray[i], extent=[0,100,0,1], aspect=img_aspect[i], cmap = cm.Greys_r)
	#	globals()[name].set_title(titlearray[i])

	ax1.imshow(imgarray[0], extent=[0,100,0,1], aspect=img_aspect[0], cmap = cm.Greys_r)
	#ax1.imshow(imgarray[0], extent=[0,100,0,1], aspect=100, cmap = cm.Greys_r)
	ax1.set_xlabel('(Right) Radiological Convention (Left)', fontsize=10)
	ax1.set_title(titlearray[0])
	
	ax2.imshow(imgarray[1], extent=[0,100,0,1], aspect=img_aspect[1], cmap = cm.Greys_r)
	#ax2.imshow(imgarray[1], extent=[0,100,0,1], aspect=100, cmap = cm.Greys_r)
	ax2.set_xlabel('(Right) Radiological Convention (Left)', fontsize=10)
	ax2.set_title(titlearray[1])
	
	ax3.imshow(imgarray[2], extent=[0,100,0,1], aspect=img_aspect[2], cmap = cm.Greys_r)
	#ax3.imshow(imgarray[2], extent=[0,100,0,1], aspect=100, cmap = cm.Greys_r)
	ax3.set_xlabel('(Right) Radiological Convention (Left)', fontsize=10)
	ax3.set_title(titlearray[2])
	
	ax4.imshow(imgarray[3], extent=[0,100,0,1], aspect=img_aspect[3], cmap = cm.Greys_r)
	#ax4.imshow(imgarray[3], extent=[0,100,0,1], aspect=100, cmap = cm.Greys_r)
	ax4.set_xlabel('(Right) Radiological Convention (Left)', fontsize=10)
	ax4.set_title(titlearray[3])
	
	ax5.imshow(imgarray[4], extent=[0,100,0,1], aspect=img_aspect[4], cmap = cm.Greys_r)
	#ax5.imshow(imgarray[4], extent=[0,100,0,1], aspect=100, cmap = cm.Greys_r)
	ax5.set_xlabel('(Right) Radiological Convention (Left)', fontsize=10)
	ax5.set_title(titlearray[4])

	

	plt.suptitle(foldname, fontsize=20)
	plt.tight_layout()
	plt.savefig(outputname)
	plt.show()
