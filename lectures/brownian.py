import numpy as np
import matplotlib.pyplot as plt

T = 1
n = 365
dt = T/n
q = 10000 # number of independent realizations (trajectories)

z = np.random.randn(q, n) # sampling from the standard normal distribution. 

x = np.sqrt(dt) * z

w = np.cumsum(x, axis=1)



t = np.linspace(dt, T, n)
ci = 3*np.sqrt(t) # 99.7 %


for omega in range(q):
    plt.plot(w[omega], label=str(omega + 1))
    plt.plot(-ci)
    plt.plot(ci)
plt.grid()
plt.show()

# z = np.array([max(w[omega][-1],0) for omega in range(q)]).mean()

# print(z)

# for omega in range(q):
#     plt.plot(np.exp(w[omega]), label=str(omega + 1))
#     # plt.plot(np.exp(ci),'--',c='black')
#     # plt.plot(np.exp(-ci),'--',c='black')
# plt.grid()
# # plt.legend()
# plt.show()



# s0 = 1.0 # initial price of the asset
# mu = 0.1 # drift parameter
# sigma = 1. # volatility parameter

# t = np.linspace(dt, T, n)
# ci = 3*np.sqrt(t)

# for omega in range(q):
#     tmp = s0 * np.exp((mu-0.5*sigma**2)*t)
#     st = tmp * np.exp(sigma * w[omega])
#     plt.plot(st, label=str(omega+1))

# plt.grid()
# plt.legend()
# plt.show()
    
