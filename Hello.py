from pixy import *
import sys

def main():
	pixy_init()
	get_pixy()



def get_pixy():
	blocks = BlockArray(100)
	frame = 0

	while 1 :
		count = pixy_get_blocks(100, blocks)
		if count > 0 :
	  		print 'count = %d' % count

if __name__ == "__main__":
	main()
	sys.exit(0)