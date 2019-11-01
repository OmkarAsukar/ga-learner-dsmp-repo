# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
loan_status = data.Loan_Status.value_counts()
print(loan_status)

loan_status.plot(kind='bar')


# --------------
#Code starts here




property_and_loan =data.groupby(['Property_Area','Loan_Status'])
#print(property_and_loan.head())
property_and_loan = property_and_loan.size().unstack()
print(property_and_loan.head())

property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
print(education_and_loan)
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here
from pandas import Series
graduate = data[data['Education']=='Graduate']

not_graduate = data[data['Education']=='Not Graduate']

graduate['LoanAmount'].plot(kind='density',label='Graduate')

not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')





#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(10,10))

ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.plot(data['ApplicantIncome'],data['LoanAmount'],'r')
ax_1.set_title('Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.plot(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

ax_3.scatter(data['TotalIncome'],data['LoanAmount'])

ax_3.plot(data['TotalIncome'],data['LoanAmount'])
ax_3.set_title('Total Income')



