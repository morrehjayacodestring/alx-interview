#!/usr/bin/python3
""" Log parsing module """

import signal
import sys

lp = []
c = 0
size = 0
codes = {'200': 0,
         '301': 0,
         '400': 0,
         '401': 0,
         '403': 0,
         '404': 0,
         '405': 0,
         '500': 0
         }

try:
    for line in sys.stdin:
        num = line.split(" ")[-2:]
        if num and len(num) == 2:
            if num[0] in codes.keys():
                codes[num[0]] += 1
            if num[1][:-1].isdigit():
                size += int(num[1][:-1])
            c += 1
        if c % 10 == 0:
            lp = list(codes.values())
            print("File size: {}".format(size))
            for x, y in codes.items():
                if y:
                    print('{}: {}'.format(x, y))
finally:
    if size:
        print("File size: {}".format(size))
        for x, y in codes.items():
            if y:
                print('{}: {}'.format(x, y))