import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy.stats as sts
import math

np.random.seed(42)
n_paths=50000
n_steps=252
S_0=100
R=0.02
vol_i=0.2
T=1


test_gamma=[0.5,1,1.5]
colors={0.5:"blue",1:"green",1.5:"red"}
fig,axes=plt.subplots(3,1,figsize=(12,12),sharex=True)

for ax,g in zip(axes,test_gamma):
    p=function.sim_cev(S_0,R,vol_i,g,T,n_paths,n_steps)
    time=np.linspace(0,1,253)
    for i in range(10):
        ax.plot(time,p[i],color=colors[g])
    ax.set_title("gamma= "+ str(g))
    ax.set_ylabel("Stock Price")

axes[-1].set_xlabel("Time (years)")
plt.tight_layout()
plt.savefig("simulations.jpg")
plt.show()

