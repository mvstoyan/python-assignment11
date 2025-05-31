import plotly.express as px
import plotly.data as pldata
import pandas as pd

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('db/lesson.db')

# SQL query to calculate revenue by employee last name
query = """
SELECT last_name, 
       SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

# Load the result into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(employee_results['last_name'], employee_results['revenue'], color='teal')
plt.title('Revenue by Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Load wind dataset
df = pldata.wind(return_type='pandas')

# Check available columns
print("Available columns:", df.columns)
print(df.head())

# Strip column names to avoid issues
df.columns = df.columns.str.strip().str.lower()

# Confirm 'strength' is in there
if 'strength' not in df.columns:
    raise ValueError("Expected 'strength' column not found in the dataset.")

# Clean 'strength' column (convert range to upper value)
df['strength'] = df['strength'].str.extract(r'(\d+\.?\d*)$')
df['strength'] = df['strength'].astype(float)

# Create scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'}
)

# Save and show the HTML plot
fig.write_html("wind.html")
fig.show()
