from control.matlab import *

s = tf('s')
G = (s+1) / (s**2 + 2*s + 1)

