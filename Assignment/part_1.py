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

def sim_cev(S,r,sgm,gamma,t,n_p,n_s):
    dt=t/n_s
    out=np.zeros((n_p,n_s+1))
    out[:,0]=S
    for i in range(n_s):
        Z=np.random.normal(0,1,n_p)
        out[:,i+1]=np.maximum(out[:,i]+(r*out[:,i]*dt)+(sgm*(out[:,i]**gamma)*(np.sqrt(dt)*Z)),(10**(-8)))
    return out

test_gamma=[0.5,1,1.5]
colors={0.5:"blue",1:"green",1.5:"red"}
fig,axes=plt.subplots(3,1,figsize=(12,12),sharex=True)

for ax,g in zip(axes,test_gamma):
    p=sim_cev(S_0,R,vol_i,g,T,n_paths,n_steps)
    time=np.linspace(0,1,253)
    for i in range(10):
        ax.plot(time,p[i],color=colors[g])
    ax.set_title(f"gamma={g}")
    ax.set_ylabel("Stock Price")

axes[-1].set_xlabel("Time (years)")
plt.tight_layout()

plt.savefig("simulations.jpg")
plt.show()

