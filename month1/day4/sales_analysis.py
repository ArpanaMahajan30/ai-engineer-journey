import pandas as pd

data = pd.read_csv(r"C:\Users\arpan\OneDrive\Desktop\AI-Engineer-Journey\month1\day4\sales.csv")

data["revenue"] = data["price"] * data["quantity"]  # Create a new column 'revenue' by multiplying 'price' and 'quantity'

total_revenue = data["revenue"].sum()  # Calculate the total revenue

# print(f"Total Revenue: {total_revenue}")  # Display the total revenue

# print(data.iloc[data["revenue"].idxmax()])  # Display the row with the maximum revenue

# print(data.iloc[data["price"].idxmax()])  # Display the row with the maximum price

# print(data["price"].mean())  # Display the average price

print(data)  # Display the DataFrame with the new 'revenue' column