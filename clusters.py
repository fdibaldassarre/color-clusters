#!/usr/bin/env python3

import argparse
import os
import sys

from src import ColorClusters

parser = argparse.ArgumentParser(description="Color Clusters")
parser.add_argument('input_image', help='Input image')
parser.add_argument('dest_image', help='Desination image with the colors')
parser.add_argument('colors', help='Number of colors')

args = parser.parse_args()

# Get the input path
path = args.input_image
if not os.path.exists(path):
    print("Input file does not exists.")
    sys.exit(1)
# Get the output path
savepath = args.dest_image
# Get the color number
try:
    k = int(args.colors)
except Exception:
    print("Invalid number of colors")
    sys.exit(2)

# Compute the clusters
cs = ColorClusters()
centers = cs.getClusters(path, k)
# Save the image
cs.saveCentersToImage(centers, savepath)
