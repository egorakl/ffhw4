import numpy as np
import matplotlib.pyplot as plt
import json

pulsar = np.fromfile(r'pulsar.dat')
print(pulsar.shape)
# plt.plot(pulsar[:1000])

trans = np.fft.fft(pulsar)
n = 5000
up = 0.5e+24
for x in range(0, n):  # Убираем низкие частоты
    trans[x] = 0
    trans[-x] = 0
for x in range(0, trans.shape[0]):  # Убираем шумы
    if abs(trans[x]) <= up:
        trans[x] = 0

fun = np.fft.ifft(trans)
peaks = np.empty(fun.shape)
count = 0

x1, x2 = 0, 0
for x in range(0, fun.shape[0]):  # Тут ищем положение двух соседних пиков
    if count == 0:
        x1 = x
    if fun[x] >= 1.5e+19:
        peaks[x] = fun[x]
        count += 1
        if count == 2:
            x2 = x
            break

t = x2 - x1  # Период
print(t)

plt.plot(fun[10:210])
plt.savefig('pulsar.png')
plt.plot(peaks[10:210], 'o')
plt.show()

data = {"period": t}
with open('pulsar.json', 'w') as out:
    json.dump(data, out)
