import matplotlib.pyplot as plt
import pandas as pd

data = {'Age': [34, 40, 37, 30, 44, 36, 32, 26, 32, 36], 'Income': [350, 450, 169, 189, 183, 80, 166, 120, 75, 40],
        'Sales': [123, 114, 135, 139, 117, 121, 133, 140, 133, 133]}
df = pd.DataFrame(data)  # convert the dictionary into data-frame

sort_data = df.sort_values(by=['Age'])  # sort the data-frame by age

print(sort_data)  # print the data-frame

list_of_Age = sort_data['Age'].to_list()  # creating a list of Age
list_of_Income = sort_data['Income'].to_list()  # creating a list of Income
list_of_Sales = sort_data['Sales'].to_list()  # creating a list of Sales

# printing all the lists
print(list_of_Age)
print(list_of_Income)
print(list_of_Sales)

plt.plot(list_of_Age, list_of_Income, label='Age_vs_Income')  # age v income graph
plt.plot(list_of_Age, list_of_Sales, label='Age_vs_Sales')  # age v sales graph

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Market Data')

plt.legend()
plt.show()
