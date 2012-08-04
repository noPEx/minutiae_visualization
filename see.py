#! /usr/bin/python


"""
	see.py : sees minutiae and plots it
	blue,green and red is the order.
"""


#! /usr/bin/python
import networkx as nx,sys
import math
import copy
import cv
import sys


def conv_to_numbers( minutiaes ) :
	numbers = []
	for m in minutiaes :
		print 'm is : ',m
		numbers.append( [  int( mi ) for mi in m ] )
		
	return numbers

def sort_2d( minutiaes ) :
	minutiaes.sort( key=lambda x: x[1] )
	return minutiaes


def read_minutiaes( ) :

	f = open( sys.argv[1],'r' )
	lines = f.readlines()
	f.close()
	
	#print lines2
	minutiaes = [ a.split()[ : 3 ] for a in lines ]
	##print 'minutiaes are'
	##print minutiaes
	
	minutiaes = conv_to_numbers( minutiaes )
	##print 'minutiaes are :',minutiaes
	
	minutiaes = sort_2d( minutiaes )

	return minutiaes



def create_image( rgbImage,minutiaes ) :
	''' Create an image where the minutiaes are shown with its orientation
	'''
	#image = cv.CreateImage( ( 260,300 ),cv.IPL_DEPTH_8U, 1 )

	#print 'image.height is : ', image.height
	#print 'image.width is : ', image.width

	#image[ 
	"""
	for i in range( image.height ) :
		for j in range( image.width ) :
			image[ i,j ] = 255
	"""

	for point in minutiaes :
		print 'point is : ',point
		#image[ point[1],point[0] ] = 0

		#Draw line starting at that point
		angle = point[2]*2*( math.pi/180.0 )
		if angle >=  2*math.pi  :
			angle = 0
		pt1 = ( point[0],point[1] )
		pt2 = ( int( point[0]+10*math.cos( angle ) ),int( point[1]-10*math.sin( angle ) ) )
		cv.Line( rgbImage,pt1,pt2,cv.RGB( 0,255,0 ) )
	
	return rgbImage
if __name__ == '__main__' :

	if len( sys.argv ) < 3 :
		print 'Correct Usage : python see.py textfile image'
		exit()

	minutiaes = read_minutiaes()
	print 'sorted minutiaes from 2 are :',minutiaes

	#image = create_image( minutiaes )
	image = cv.LoadImage( sys.argv[2],cv.CV_LOAD_IMAGE_UNCHANGED )

	rgbImage = cv.CreateImage( ( image.width, image.height ),cv.IPL_DEPTH_8U,3 )

	for h in range( rgbImage.height ):
		for w in range( rgbImage.width ) :
			rgbImage[h,w] = ( image[ h,w ],image[ h,w ],image[ h,w ] )
	
	marked_image= create_image( rgbImage,minutiaes )
	cv.SaveImage( 'rgbImage.bmp',marked_image )
