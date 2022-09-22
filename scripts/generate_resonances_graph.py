#!/usr/bin/env python3

import os
import glob
import sys

axe = sys.argv[1].lower()

source = "/tmp"
dest = "/home/pi/klipper_config/resonances"

os.chdir(source)
csv_file = glob.glob('resonances_'+axe+'_*.csv')[0]
graph_file = os.path.splitext(csv_file)[0] + ".png"

if not os.path.exists(dest):
    os.makedirs(dest)

generate_command = "~/klipper/scripts/calibrate_shaper.py " + source + "/" + csv_file + " -o " + dest + "/" + graph_file
os.system(generate_command)

os.rename(source + "/" + csv_file, dest + "/" + csv_file)
