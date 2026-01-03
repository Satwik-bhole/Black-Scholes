from math import log,sqrt,pi,exp
from scipy.stats import norm
from datetime import datetime,date
import numpy as np
import pandas as pd
from datetime import datetime

def d1(S,K,T,r,sgm):
    d1=(log(S/K)+(r+(sgm**2)/2)*T)/(sgm*sqrt(T))
    return d1
def d2(S,K,T,r,sgm):
    d2=d1(S,K,T,r,sgm)-(sgm*sqrt(T))
    return d2
def call_price(S,K,T,r,sgm):
    cp=S*norm.cdf(d1(S,K,T,r,sgm))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sgm))
    return cp
def put_price(S,K,T,r,sgm):
    pp=K*exp(-r*T)-S+call_price(S,K,T,r,sgm)
    return pp
def call_delta(S,K,T,r,sgm):
    delta=norm.cdf(d1(S,K,T,r,sgm))
    return delta
def call_gamma(S,K,T,r,sgm):
    gamma=norm.pdf(d1(S,K,T,r,sgm))/(S*sgm*sqrt(T))
    return gamma
def call_vega(S,K,T,r,sgm):
    vega=0.01*(S*norm.pdf(d1(S,K,T,r,sgm))*sqrt(T))
    return vega
def call_theta(S,K,T,r,sgm):
    theta=((-(S*norm.pdf(d1(S,K,T,r,sgm))*sgm)/(2*sqrt(T))-r*K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sgm))))/365
    return theta
def call_rho(S,K,T,r,sgm):
    rho=0.01*(K*T*exp(-r*T)*norm.cdf(d2(S,K,T,r,sgm)))
    return rho
def put_delta(S,K,T,r,sgm):
    delta=(-norm.cdf(-d1(S,K,T,r,sgm)))
    return delta
def put_gamma(S,K,T,r,sgm):
    gamma=norm.pdf(d1(S,K,T,r,sgm))/(S*sgm*sqrt(T))
    return gamma
def put_vega(S,K,T,r,sgm):
    vega=0.01*(S*norm.pdf(d1(S,K,T,r,sgm))*sqrt(T))
    return vega
def put_theta(S,K,T,r,sgm):
    theta=((-(S*norm.pdf(d1(S,K,T,r,sgm))*sgm)/(2*sqrt(T))+r*K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sgm))))/365
    return theta
def put_rho(S,K,T,r,sgm):
    rho=0.01*(-K*T*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sgm)))
    return rho
def exp_time_yr(exp_date):
    exp_date=datetime.strptime(exp_date,"%m-%d-%Y")
    T=((exp_date-datetime.now()).days)/365
    return T
def volatility_calc(price,S,K,T,r,option):
    price=float(price)
    vol=0.0001
    if(option=='C'):
        while vol<2:
            cp=call_price(S,K,T,r,vol)
            if abs(price-cp)<0.01:
                return vol
            vol=vol+0.0001
        return "Volatility not in range for call option"
    else:
        vol=0.0001
        while vol<2:
            pp=put_price(S,K,T,r,vol)
            if abs(price-pp)<0.01:
                return vol
            vol=vol+0.0001
        return "Volatility not in range for put option"

def sim_cev(S,r,sgm,gamma,t,n_p,n_s):
    dt=t/n_s
    out=np.zeros((n_p,n_s+1))
    out[:,0]=S
    for i in range(n_s):
        Z=np.random.normal(0,1,n_p)
        out[:,i+1]=np.maximum(out[:,i]+(r*out[:,i]*dt)+(sgm*(out[:,i]**gamma)*(np.sqrt(dt)*Z)),(10**(-8)))
    return out

def avg_price(g,S,K,r,sgm,t,n_p,n_s):
    np.random.seed(42)
    p=sim_cev(S,r,sgm,g,t,n_p,n_s)
    pay=np.maximum(p[:,-1]-K,0)
    pay_mean=pay.mean()
    prc=np.exp(-r*t)*pay_mean
    return prc

def avg_price_gammas(gammas,S,K,r,sgm,t,n_p,n_s):
    temp={}
    for g in gammas:
        np.random.seed(42)
        p=sim_cev(S,r,sgm,g,t,n_p,n_s)
        pay=np.maximum(p[:,-1]-K,0)
        pay_mean=pay.mean()
        prc=np.exp(-r*t)*pay_mean
        temp[g]=prc
    return temp

