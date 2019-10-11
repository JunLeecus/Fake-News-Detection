import tensorflow as tf
import csv
import numpy as np
import re

def _read_csv(filepath):
    with tf.gfile.Open(filepath, "r") as f:
        reader = csv.reader(f, delimiter=",")
        lines = []
        for line in reader:
            lines.append(line)
        #lines = np.array(lines)
    return lines

a = _read_csv("/Users/lijun/Desktop/submit.csv")
for (i,line) in enumerate(a):
   print(line)
