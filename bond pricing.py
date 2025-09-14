import numpy as np
import pandas as pd
from datetime import date
from datetime import datetime

data = pd.read_csv('/content/Bond-data-for-project.csv')

data.columns

data.columns = data.columns.str.replace('\n', '', regex=False)
display(data.head())###we do this to drop the annoying  \n thing 


today = date.today()##i added this as to help in bond pricing 

data['MATURITY DATE '] = pd.to_datetime(data['MATURITY DATE '], errors='coerce')
today = pd.Timestamp.today()
# Calculate days till maturity
data['time till maturity'] = (data['MATURITY DATE '] - today).dt.days#### for the time period between days 

data.dropna()

data['COUPON RATE '] = data['COUPON RATE '].apply(lambda x: 0 if x=='-' else x)##to detect zcbs 

def bond_pricing(maturity,fv,couponrate):
  bond_val = 0
  maturity_years = maturity/365
  if couponrate == 0:####ZCB
    bond_val = fv*np.exp(-couponrate*(maturity_years))
  else:
    coupon_payment = fv*couponrate
    for t in range(1,int(np.floor(maturity_years))+1):
      bond_val += coupon_payment*np.exp(-couponrate*(t-1))
    bond_val += fv*np.exp(-couponrate*maturity_years)
  return bond_val
##this involves zcbs and cbs(in the else statement we add 1 to +1 to show that the coupons are paid annually 

type(data['FACE VALUE '].iloc[1])
data['FACE VALUE '] = data['FACE VALUE '].str.replace(',', '').astype(float)

type(data['COUPON RATE '].iloc[1])
data['COUPON RATE '] = data['COUPON RATE '].str.replace(',', '').astype(float)

type(data['time till maturity'].iloc[1])
data['time till maturity'] = data['time till maturity'].astype(float)


data['bond Price'] = data.apply(
    lambda row: bond_pricing(row['time till maturity'],row['FACE VALUE '],row['COUPON RATE ']),
    axis=1
)