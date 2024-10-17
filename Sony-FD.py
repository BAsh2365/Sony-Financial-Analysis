# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:56:10 2024

@author: bharg
"""

import requests
import matplotlib.pyplot as plt

# API key and parameters
api_key = "My-API Key"
company = "Sony"
years = 5

# Fetch data
response = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
income_statement = response.json()

# Extract data for plotting
revenues = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
profits = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))
years_labels = list(reversed([income_statement[i]['date'][:5] for i in range(len(income_statement))]))  

# Convert values to billions
revenues = [rev / 1e9 for rev in revenues]  # Convert revenue to billions
profits = [prof / 1e9 for prof in profits]  # Convert profits to billions

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years_labels, revenues, label="Revenue of Sony (in billions)", marker='o')
plt.plot(years_labels, profits, label="Profits of Sony (in billions)", marker='o')

# Customize graph
plt.title("Revenues and Profits for Sony Corporation")
plt.xlabel("Year")
plt.ylabel("Amount (in billions)")
plt.legend(loc="upper right")

# Display the plot
plt.show()



