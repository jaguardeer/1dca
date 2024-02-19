import cv2 as cv
import numpy as np
import itertools
import sys

window = 'test'
initial_rule = int(sys.argv[1]) if len(sys.argv) > 1 else 82

def on_trackbar(trackbar_val):
	arr_size = (1200, 1200)
	arr = np.zeros(arr_size, dtype = np.uint8)
	arr[0, arr_size[0] // 2] = 255 # initial cell
	img = draw_1dca(arr, trackbar_val)
	resized = cv.resize(arr, None, fx = 1, fy = 1, interpolation = cv.INTER_NEAREST)
	cv.imshow(window, resized)

def draw_1dca(arr, rule):
	#rule_table = [1 if rule & (1 << i) != 0 else 0 for i in range(8)]

	for row_prev, row_curr in itertools.pairwise(arr):
		row_curr[0] = row_prev[0]
		row_curr[-1] = row_prev[-1]
		for x in range(1, len(row_curr) - 1):
			val = 0
			for i in row_prev[x - 1 : x + 2]:
				val <<= 1
				val += i & 1
			row_curr[x] = 255 if rule & (1 << val) != 0 else 0



cv.namedWindow(window)
trackbar = cv.createTrackbar('rule', window, initial_rule, 255, on_trackbar)
on_trackbar(initial_rule)
cv.waitKey()