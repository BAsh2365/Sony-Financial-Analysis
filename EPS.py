# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:34:54 2024

@author: bharg
"""

import requests
import matplotlib.pyplot as plt

# API setup
api_key = "X"
company = "Sony"
years = 5

# Fetch income statement data
response = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
income_statement = response.json()

# Extract EPS data
EPS = list(reversed([income_statement[i]['eps'] for i in range(len(income_statement))]))
years_labels = list(reversed([income_statement[i]['date'][:4] for i in range(len(income_statement))]))



# Plotting EPS and CAC on dual y-axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot EPS on the first y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('EPS (Earnings per Share in dollars)', color='blue')
ax1.plot(years_labels, EPS, color='blue', marker='o', label="EPS")
ax1.tick_params(axis='y', labelcolor='blue')


# Titles and Legends
plt.title("Sony Corporation: Earnings per share (2020-2024)")
fig.tight_layout()
ax1.legend(loc="upper left")
plt.show()
