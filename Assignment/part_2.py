import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy.stats as sts
import math
import function


n_paths=50000
n_steps=252
S_0=100
R=0.02
vol_i=0.2
T=1
K=100
x=0.95

test_gamma=[0.5,1,1.5]

for g in test_gamma:
    np.random.seed(42)
    p=function.sim_cev(S_0,R,vol_i,g,T,n_paths,n_steps)
    pay=np.maximum(p[:,-1]-K,0)
    pay_mean=pay.mean()
    price=np.exp(-R*T)*pay_mean
    std_payoff=pay.std(ddof=1)
    error=np.exp(-R*T)*(std_payoff/(np.sqrt(n_paths)))
    ci_95=sts.norm.ppf((1+x)/2)
    ci_upper=price+(ci_95*error)
    ci_lower=price-(ci_95*error)
    print("For gamma= "+str(g)+" :")
    print("Average discounted payoff= "+str(price))
    print("Standard Error= "+str(error))
    print("95% confidence interval: ")
    print("Upper limit :"+str(ci_upper))
    print("Lower limit :"+str(ci_lower))
    BS_price=function.call_price(S_0,K,T,R,vol_i)
    print("Black Scholes price :"+str(BS_price))
    print()


