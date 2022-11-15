# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import yfinance as yf
# import streamlit as st

# # importing Salary Data's
# dataset = pd.read_csv('Salary_Data.csv')
# x = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, -1].values

# # Training Model set and Testing.
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 1)

# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(x_train,y_train)

# plt.scatter(x_train,y_train, color = 'red')
# plt.plot(x_train,regressor.predict(x_train), color = 'blue')
# plt.title("Salary vs Experience (Training Set)")
# plt.xlabel("Year of Experience")
# plt.ylabel("Salary")
# plt.show()

# plt.scatter(x_test,y_test,color='red')
# plt.plot(x_train,regressor.predict(x_train),color='blue')
# plt.title("Salary vs Experience (Test Set)")
# plt.xlabel("Year of Experience")
# plt.ylabel("Salary")
# plt.show()

# print(x_train)

# st.write("""
# # Simple Linear Regression  **StreamLit**
# """)
# chart_data = pd.DataFrame(x,y)
# st.line_chart(chart_data)