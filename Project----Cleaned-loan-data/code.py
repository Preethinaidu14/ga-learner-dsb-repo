# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico']>700])/len(df['fico'])
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df['purpose'])
df1 = pd.DataFrame(df[df['purpose'] == 'debt_consolidation'])
p_a_b = (len(df[df['fico']>700]) - len(df[df['purpose'] == 'debt_consolidation']))/(p_a)
p_b_a = (len(df[df['fico']>700]) - len(df[df['purpose'] == 'debt_consolidation']))/len(df[df['purpose'] == 'debt_consolidation'])
result = p_b_a == p_a
print(result)

# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df['paid.back.loan'])
prob_cs = len(df[df['credit.policy']== 'Yes'])/len(df['credit.policy'])
new_df = df[df['paid.back.loan'] == 'Yes']


prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/ new_df.shape[0]
#print(prob_pd_cs)
bayes = (prob_pd_cs *prob_lp)/prob_cs
print(bayes)


# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind='bar')
df1 = df[df['paid.back.loan'] == 'No']
#a = df.groupby('purpose')['paid.back.loan' == 'No']


# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df['installment'].plot(kind= 'hist')
df['log.annual.inc'].plot(kind= 'hist')
# code ends here


