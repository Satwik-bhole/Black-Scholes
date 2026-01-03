import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy.stats as sts
import scipy.optimize as opt
import math
import function

def IV(price,S,K,T,r):
    floor_p=function.call_price(S,K,T,r,(10**(-10)))
    prc=max(price,floor_p+(10**(-5)))
    try:
        Vol=opt.brentq((lambda V: function.call_price(S,K,T,r,V)-prc),10**(-10),10)
        return Vol
    except ValueError:
        return (10*100)

n_paths=50000
n_steps=252
S_0=100
R=0.02
vol_i=0.2
T=1
K=100
gammas=[0.5,1.0,1.5]

d=function.avg_price_gammas(gammas,S_0,K,R,vol_i,T,n_paths,n_steps)
vol=[]
for idx,prc in d.items():
    tp=IV(prc,S_0,K,T,R)
    tp=tp*100
    vol.append((idx,tp))
for (a,b) in vol:
    print("At gamma= "+str(a)+" Volatility:- "+str(b))

dif_K=[80,90,100,110,120]
gamma=0.5
IV_K=[]
for k in dif_K:
    a_p=function.avg_price(gamma,S_0,k,R,vol_i,T,n_paths,n_steps)
    b=IV(a_p,S_0,k,T,R)
    b=b*100
    IV_K.append(b)

plt.plot(dif_K,IV_K)
plt.xlabel("Strike Price")
plt.ylabel("Implied Volatility")
plt.savefig("Smile Plot")
plt.show()
