#! /usr/bin/env python3
import sys
import os
from text_lib.frequency_calc import *

# genrate token for all files
folder=sys.argv[1]
file_list=list(os.walk(folder))[0][2]
for i in file_list:
    local_file_path=str(sys.argv[1]) + "/" + str(i)
    print(local_file_path)
    gen_freq_file(local_file_path)
