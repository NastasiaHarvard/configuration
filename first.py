import random
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def cm_to_inch(value):
    return value / 2.54


start = 0
stop = 2
N = 1000

x1 = [random.uniform(start, stop) for _ in range(N)]
x2 = [random.uniform(start, stop) for _ in range(N)]
z1 = [random.uniform(start, stop) for _ in range(N)]
z2 = [random.uniform(start, stop) for _ in range(N)]

j = 0
num: int = 0
f1 = [0] * pow(N, 2)
f2 = [0] * pow(N, 2)
f1_new = [0] * N
f2_new = [0] * N
v1 = [0] * N
v2 = [0] * N

for k in range(0, N):
    for l in range(0, N):
        f1[num] = (math.pow(x1[k], 2) + math.pow(x2[k], 2) - x2[k] * (math.pow(z1[l], 2) - math.pow(z2[l], 2)))
        f2[num] = (math.pow(x1[k], 2) - math.pow(x2[k], 2) - x1[k] * (math.pow(z1[l], 2) + math.pow(z2[l], 2)))
        num = num + 1

for i in range(0, pow(N, 2), N):
    l = 0
    for k in range(i, (i + N)):
        f1_new[l] = f1[k]
        f2_new[l] = f2[k]
        l = l + 1
    v1[j] = min(f1_new)
    v2[j] = min(f2_new)
    f1_new = [0] * N
    f2_new = [0] * N
    j = j + 1

#  считаем Bk
bk = [0] * N
for i in range(0, N):
    for j in range(0, N):
        if i != j and (v1[i] - v1[j] >= 0) and (v2[i] - v2[j] >= 0):
            bk[i] = bk[i] + 1

# считаем Ф, Порето и и коэффициенты и рисуем точки
F = [0] * N
P = [0] * N
K = [0] * N
fig, ax = plt.subplots(figsize=(cm_to_inch(25), cm_to_inch(25)))
for i in range (0, N):
    # F[i] = 1/(1+(bk[i]/(N-1)))
    # if F[i] == 1:
    #     P[i] = 1
    #     ax.scatter(v1[i], v2[i], c='r')
    # elif  F[i] < 1:
    #     ax.scatter(v1[i], v2[i], c = 'b')
    ax.scatter(f1[i], f2[i], c = 'b')
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.grid()
ax.set_xlabel('f1')
ax.set_ylabel('f2')
plt.savefig('f1f2.png')
# q1 = []
# q2 = []
#
# q1.append(-1.9496697435406656)
# q1.append(-1.725216615790944)
# q1.append(-1.9776960568724289)
# q1.append(-1.8926906476192098)
# q1.append(-1.9885841869215315)
# q1.append(-1.989535549547507)
#
# q2.append(-6.717260480111172)
# q2.append(-6.941626168702582)
# q2.append(-7.945845312626689)
# q2.append(-7.614687034570163)
# q2.append(-7.76821944768132)
# q2.append(-7.906666379304882)
#
# fig, ax = plt.subplots(figsize=(cm_to_inch(25), cm_to_inch(25)))
# for i in range (0, 5):
#    ax.scatter(q1[i], q2[i], c = 'b')
# ax.xaxis.set_major_locator(ticker.MultipleLocator(0.05))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
# ax.grid()
# ax.set_xlabel('v1')
# ax.set_ylabel('v2')
# plt.savefig('pareto.png')
