#! /usr/bin/python

"""
	see.py : sees minutiae and plots it
"""


#! /usr/bin/python
import networkx as nx,sys
import math
import copy
import cv



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



def create_image( minutiaes ) :
	''' Create an image where the minutiaes are shown with its orientation
	'''
	image = cv.CreateImage( ( 260,300 ),cv.IPL_DEPTH_8U, 1 )

	print 'image.height is : ', image.height
	print 'image.width is : ', image.width

	#image[ 
	for i in range( image.height ) :
		for j in range( image.width ) :
			image[ i,j ] = 255

	for point in minutiaes :
		print 'point is : ',point
		image[ point[1],point[0] ] = 0
	print 'Done with assignments '
	cv.SaveImage( 'blank.jpg',image )

if __name__ == '__main__' :

	minutiaes = read_minutiaes()
	print 'sorted minutiaes from 2 are :',minutiaes

	image = create_image( minutiaes )
