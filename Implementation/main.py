from math import log,sqrt,pi,exp
from scipy.stats import norm
from datetime import datetime,date
import numpy as np
import pandas as pd
from datetime import datetime
import function
st=input("What would you like to do?\n" "Enter 'V' to calculate Volatility (from Price, S, K, T, r,option type)\n" "Enter 'A' to calculate Price and Greeks (from S, K, T, r, Volatility)\n" "Choice: ").upper().strip()

if st=='V':
    S=input("Enter stock price S:")
    S=float(S)
    K=input("Enter strike price K:")
    K=float(K)
    t=input("Enter expiry date in format(mm-dd-yyyy):")
    T=function.exp_time_yr(t)
    r=input("Enter risk-neutral interest rate r:")
    r=float(r)
    r=r/100
    price=input("Enter current price of option :")
    price=float(price)
    option=input("Enter type of option C for call and P for put:").upper().strip()
    volatilty=function.volatility_calc(price,S,K,T,r,option)
    print("For :")
    print(f"Stock price (S): {S}")
    print(f"Strike price (K): {K}")
    print(f"Risk free interest rate (r): {r}")
    print(f"Time to expiry (in years) (T): {T:.4f}")
    print(f"Option price : {price}")
    print(f"Option type : {'Call' if option=='C' else 'Put'}")
    if isinstance(volatilty,float):
        print(f"Calculated volatility: {(volatilty*100):.2f}%")
    else:
        print(volatilty)
elif st=='A':
    S=input("Enter stock price S:")
    S=float(S)
    K=input("Enter strike price K:")
    K=float(K)
    t=input("Enter expiry date in format(mm-dd-yyyy):")
    T=function.exp_time_yr(t)
    r=input("Enter risk-neutral interest rate r:")
    r=float(r)
    r=r/100
    V=input("Enter volatility V:")
    V=float(V)
    V=V/100
    option=input("Enter type of option C for call and P for put:").upper().strip()
    if option=='C':
        pr=function.call_price(S,K,T,r,V)
        print("Price of call option at:")
        print(f"Stock price (S): {S}")
        print(f"Strike price (K): {K}")
        print(f"Risk free interest rate (r): {r*100}")
        print(f"Time to expiry (in years) (T): {T:.4f}")
        print(f"Volatility (V) : {V*100}")
        print(f"Calculated price : {pr}")
        print()
        print("Call option Greeks:")
        print(f"Delta : {function.call_delta(S,K,T,r,V):.4f}")
        print(f"Gamma : {function.call_gamma(S,K,T,r,V):.4f}")
        print(f"Vega : {function.call_vega(S,K,T,r,V)}")
        print(f"Theta : {function.call_theta(S,K,T,r,V)}")
        print(f"Rho : {function.call_rho(S,K,T,r,V)}")
    elif option=='P':
        pr=function.put_price(S,K,T,r,V)
        print("Price of put option at:")
        print(f"Stock price (S): {S}")
        print(f"Strike price (K): {K}")
        print(f"Risk free interest rate (r): {r}")
        print(f"Time to expiry (in years) (T): {T:.4f}")
        print(f"Volatility (V) : {V*100}")
        print(f"Calculated price : {pr*100}")
        print()
        print("Put option Greeks:")
        print(f"Delta : {function.put_delta(S,K,T,r,V):.4f}")
        print(f"Gamma : {function.put_gamma(S,K,T,r,V):.4f}")
        print(f"Vega : {function.put_vega(S,K,T,r,V)}")
        print(f"Theta : {function.put_theta(S,K,T,r,V)}")
        print(f"Rho : {function.put_rho(S,K,T,r,V)}")
    else:
        print("enter valid inputs")
else:
    print("enter valid inputs")


