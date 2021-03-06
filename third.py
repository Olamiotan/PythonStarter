#using numpy and deriving profit from lists of revenue and expenses
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]

a = np.array(revenue, int)
b = np.array(expenses, int)
profit = a - b

print("\nProfit made from January to December = ", profit)

#code extracting two lists into a dictionary
Fin_status = dict(zip(months,profit))
print ("\nFinancial status = ", Fin_status)

#using Pandas series 
import pandas as pd
new_series = pd.Series(Fin_status, name='Fin_status')
print ("\nFinancial status in panda series:\n", new_series)

#using matplotlib to plot a line graph
import matplotlib.pyplot as plt
new_series.plot.line()
plt.title('Profits made from January to December', fontsize=14)
plt.xlabel('Months', fontsize=14,)
plt.ylabel('Profits', fontsize=14)
plt.grid(True)
plt.show()
