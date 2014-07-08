### Not reliable for final image orientation, crosscheck with AFNI or FSL
def midslice(imagefile, datatype):

	import os
	import nibabel as nib
	import matplotlib.pyplot as plt
	import numpy as np
	import matplotlib.cm as cm
	import code

	imorient=os.popen('fslorient '+imagefile).read()
	print imorient

	img = nib.nifti1.load(imagefile)

	header=img.get_header()
	#print header

	img_shape=img.shape
	img_voxels=img.get_header().get_zooms()
	print img.shape
	img_data_type=img.get_data_dtype()
	#print img_data_type

	img_aff=img.get_affine()
	#print img_aff

	img_data=img.get_data()

	img_all=np.array(img_data)
	
	if 'RADIOLOGICAL' in imorient:
		if datatype == 'anat':
			mid_img_index=round(img_shape[2]/2)
			img_slice=img_all[:,:,mid_img_index]
			img_slice=img_slice.T
			img_slice=img_slice[ ::-1,:]
			#img_slice=np.fliplr(img_slice) #If allowed in code should produce left is left image

		if datatype == 'rest':
			mid_img_index=round(img_shape[2]/2)
			img_slice=img_all[:,:,mid_img_index,1]
			img_slice=img_slice.T
			img_slice=img_slice[ ::-1,:]
			#img_slice=np.fliplr(img_slice)
	
	if 'NEUROLOGICAL' in imorient:
		if datatype == 'anat':
			mid_img_index=round(img_shape[2]/2)
			img_slice=img_all[:,:,mid_img_index]
			img_slice=img_slice.T
			img_slice=img_slice[ ::-1,:]
			img_slice=np.fliplr(img_slice)

		if datatype == 'rest':
			mid_img_index=round(img_shape[2]/2)
			img_slice=img_all[:,:,mid_img_index,1]
			img_slice=img_slice.T
			img_slice=img_slice[ ::-1,:]
			img_slice=np.fliplr(img_slice)

	
	#img_aspect=[]

	
	#img_shape=img_slice.shape
	#img_aspect_temp=float(img_shape[0])/float(img_shape[1])
	#img_aspect_temp=round(img_aspect_temp*100)
	#img_aspect.append(img_aspect_temp)

	 
	#fig, (ax1) = plt.subplots(ncols=1, figsize=(20,7))
	#ax1.imshow(img_slice, extent=[0,100,0,1], aspect=img_aspect[0], cmap = cm.Greys_r)
	#plt.suptitle('Image', fontsize=20)
	#plt.tight_layout()
	#plt.show()



	return (img_slice, img_voxels)
