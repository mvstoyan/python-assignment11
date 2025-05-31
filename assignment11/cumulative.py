import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('db/lesson.db')

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

df = pd.read_sql(query, conn)

df['cumulative'] = df['total_price'].cumsum()

df.plot(x='order_id', y='cumulative', kind='line', marker='o', color='green')
plt.title('Cumulative Revenue by Order')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()
