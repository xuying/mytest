# Mesaure some strings
words = ['Monday', 'Tuesday', 'Wednesday']
for w in words:
    print (w, len(w))

# Fibonacci series
a, b = 0, 1
if b > 0:
    print ('Non zero')

while b < 100:
    print (b, end=',')
    a, b = b, a+b