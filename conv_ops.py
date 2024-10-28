# conv_ops.py
# cd Desktop\Phyton
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#  Example python3 conv_ops.py 3 30 30 4 3 3 1 0
#  4
#  28
#  28
#  84672
#  84672
#  0
#
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  n_filt: number of filters in the convolution layer
#  h_filt: filter height count
#  w_filt: filter width count
#  s: stride of convolution filters
#  p: amount of padding on each of the four input map sides
#  ...
# Output:
#  print(int(c_out)) # output channel count
#  print(int(h_out)) # output height count
#  print(int(w_out)) # output width count
#  print(int(adds))  # number of additions performed
#  print(int(muls))  # number of multiplications performed
#  print(int(divs))  # number of divisions performed
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# initialize script arguments
c_in = 0.0
h_in = 0.0
w_in = 0.0
n_filt = 0.0 
h_filt = 0.0 
w_filt = 0.0
s = 0.0 
p = 0.0

# parse script arguments
if len(sys.argv)==9:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    n_filt = float(sys.argv[4]) 
    h_filt = float(sys.argv[5]) 
    w_filt = float(sys.argv[6])
    s = float(sys.argv[7]) 
    p = float(sys.argv[8])
    
else:
   print(\
    'Usage: '\
    'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
   )
   exit()

# write script below this line

c_out = n_filt
h_out = (1/s) * (h_in + 2*p - h_filt) + 1
w_out = (1/s) * (w_in + 2*p - w_filt) + 1
adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt

#Due to Convolution Operation
divs = 0

#output
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed