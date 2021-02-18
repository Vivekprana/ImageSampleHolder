#!/usr/bin/env python3
import fileinput
import sys
import re

print('hello world')

inputFile = sys.argv[1]
outputFile = "modified-" + inputFile 
changeLine = True

with open(inputFile, "rt") as fin:
    with open(outputFile, "wt") as fout:
        for line in fin:
            if changeLine == True:
                # fout.write(line.replace('fill', 'giantPicklesRainingfrom', 1))
                # fillIndex=line.index("fill")
                # opacityLine = re.sub(r'(fill="#*[a-zA-Z0-9]*")', r'\1 opacity="0"', line, 1)
                opacityLine = re.sub(r'(fill="[^\"]*")', r'\1 opacity="0"', line, 1)
                fout.write(opacityLine)
                changeLine = False
            else:
                fout.write(line)
            

