""" Test moduel - this is docstring. without this, there will be C0111 pylint warning """

# Mesaure some strings
# Constanst should be all CAP case
WORDS = ['Monday', 'Tuesday', 'Wednesday']
for w in WORDS:
    print(w, len(w))

# Fibonacci series
A, B = 0, 1
if B > 0:
    print('Non zero')

while B < 100:
    print(B, end=',')
    A, B = B, A+B
