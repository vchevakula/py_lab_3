#!/usr/local/bin/python3
import argparse

# build the parser
parser = argparse.ArgumentParser(prog='reverse_arg',description='Read a file in reverse')
parser.add_argument ('filename', help = 'the file to read')
parser.add_argument ('--limit','-l', type=int, help='the number of lines to read')
parser.add_argument ('--version','-v', action= 'version', version='%(prog)s 1.0')
args = parser.parse_args()

with open(args.filename) as f:
    lines = f.readlines()
    rev = lines.reverse()
    print(rev)
    
    #if args.limit:
    #    lines = lines[:args.lmit]
    #for line in lines:
    #    print(line.strip()[::-1])


#print(args)

# parse the arguments

# read the file and reverse the contents and print the file



