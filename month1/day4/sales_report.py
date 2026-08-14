import pandas as pd

data = pd.read_csv("sales.csv")

data["revenue"] = data["price"] * data["quantity"]
total_revenue = data["revenue"].sum()
average_price = data["price"].mean()
most_expensive_product = data.iloc[data["price"].idxmax()]
highest_revenue_product = data.iloc[data["revenue"].idxmax()]

print(f"""===== SALES REPORT =====

Total Revenue: {total_revenue}

Average Price: {average_price}

Most Expensive Product: {most_expensive_product['product']}

Highest Revenue Product: {highest_revenue_product['product']}""")
 