import numpy , cv2 
import yappi
  
def invert_numpy(image): 
	img=image.copy()
	img=image[:,:]

	 
	return img

def naive(image):
	img=image.copy()
	rows,cols=image.shape
	
	for i in range(rows):
		for j in range(cols):
			img[i,j]=255-image[i,j]
	return img
			
def display(orig,invert):
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image',600,600)
    cv2.namedWindow('image0',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image0',600,600)
    cv2.imshow('image0',orig)
    cv2.waitKey(0)
    cv2.imshow('image',invert)
    cv2.waitKey(0)
	
def main():
    image=cv2.imread('image.jpg',0) 
    invert_numpy(image)
    invert=naive(image)
    display(image,invert)
    
yappi.start()

main()

yappi.get_func_stats().print_all()

yappi.get_thread_stats().print_all()
print yappi.get_mem_usage()
 

