#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import argparse

# get image file name
parser = argparse.ArgumentParser()
parser.add_argument("image")
args = parser.parse_args()

filename = args.image

# convert to hexadecimal
columnum = 25
all_lines = ""

with open(filename, "rb") as imageFile:
    f = imageFile.read()
    b = bytearray(f)
print(len(b))
for i in range(len(b)/columnum+1):
    b_line = ""
    for j in range( min(len(b)-i*columnum, columnum) ):
        b_line += '0x{:02X},'.format(int(b[i*columnum+j]))
    print(b_line)
    all_lines += b_line + "\n"

# save as text file
with open("output.txt", mode='w') as outputFile:
    outputFile.write(all_lines)
