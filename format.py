#!/usr/bin/python
#coding=utf-8

import sys
import json

def format(in_file, out_file):
	with open(out_file, 'w') as output:
		with open(in_file) as input:
			for line in input.readlines():
				try:
					proxy = json.loads(line)
					output.write('http://{0}:{1}\n'.
						format(proxy['ip'], proxy['port']))
				except:
					continue


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Invalid Parameters. inputfile outputfile')
	else:
		format(sys.argv[1], sys.argv[2])

