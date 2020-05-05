# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000
data = pd.read_csv(path)
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
data_sample = data.sample(sample_size , random_state = 0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
margin_of_error = z_critical*(sample_std/math.sqrt(sample_size))
confidence_interval =( (sample_mean - margin_of_error),(sample_mean + margin_of_error))
print(confidence_interval)
true_mean = data['installment'].mean()
print(true_mean == confidence_interval)

# path        [File location variable]

#Code starts here



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig , axes = plt.subplots(3,1)
for i in range(0,len(sample_size)):
    m = []
    for j in range(1000):
        data['installment'].sample(n=sample_size[i])
        m.append(data['installment'].mean())
    mean_series = pd.Series(m)



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = [x.strip('%') for x in data['int.rate']]
data['int.rate'] = data['int.rate'].astype('float')
data['int.rate'] = data['int.rate']/100
#print(data['int.rate'])
z_statistic , p_value = ztest(data[data['purpose']=='small_business']['int.rate'] ,value = data['int.rate'].mean() ,alternative='larger' )
print(z_statistic)
print(p_value)
if p_value<0.05:
    print('reject')
else:
    print('accept')



# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic ,p_value = ztest(x1= data[data['paid.back.loan']=='No']['installment'],
x2 = data[data['paid.back.loan']=='Yes']['installment'] )
print(p_value)
if p_value < 0.05:
    print('reject')
else:
    print('accept')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = (data[data['paid.back.loan'] == 'Yes']['purpose']).value_counts()
print(yes)
no = (data[data['paid.back.loan'] == 'No']['purpose']).value_counts()
print(no)
observed = pd.concat([yes.T,no.T ], axis = 1, keys = ['Yes','No'])
chi2, p, dof, ex = chi2_contingency(observed)
chi2 == critical_value
if chi2 > critical_value:
    print('reject')
else:
    print('accept')


