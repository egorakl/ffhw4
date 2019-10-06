import numpy as np
import matplotlib.pyplot as plt
import json


code = np.array([+1, +1, +1, -1, -1, -1, +1, -1, -1, +1, -1], dtype=np.int8)
code = np.repeat(code, 5)

with open('Раздьяконов.dat') as f:
    data = np.array(f.readlines(), dtype=np.float)

# plt.plot(data)

conv = np.convolve(data, code[::-1], mode='full')

up = 30
low = -30

uu = np.full(conv.shape, up)
ll = np.full(conv.shape, low)
plt.plot(conv)
plt.plot(uu)
plt.plot(ll)

bits = []
for x in range(1, conv.size-1):
    if conv[x] >= up and conv[x-1] < conv[x] and conv[x+1] < conv[x]:
        bits.append(1)
    elif conv[x] <= low and conv[x-1] > conv[x] and conv[x+1] > conv[x]:
        bits.append(0)

bits = np.array(bits)
# print(bits.shape)
num = np.packbits(bits)
b = num.tobytes()
s = b.decode('ascii')
# print(s)
# plt.show()

data = {"message": s}
with open('wifi.json', 'w') as out:  
    json.dump(data, out)
