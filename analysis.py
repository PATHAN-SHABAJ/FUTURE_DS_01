
import pandas as pd

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")


print("BUSINESS SALES PERFORMANCE ANALYSIS")


total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_sales / total_orders

print("\nKEY PERFORMANCE INDICATORS")
print("Total Sales: $", round(total_sales, 2))
print("Total Profit: $", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Average Order Value: $", round(average_order_value, 2))

print("\nSALES BY CATEGORY")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False).round(2))

print("\nPROFIT BY CATEGORY")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False).round(2))

print("\nSALES BY REGION")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False).round(2))

print("\nTOP 10 PRODUCTS BY SALES")
top_products = df.groupby("Product Name")["Sales"].sum()
print(top_products.sort_values(ascending=False).head(10).round(2))

print("\nMONTHLY SALES")
monthly_sales = (
    df.set_index("Order Date")["Sales"]
    .resample("MS")
    .sum()
)
print(monthly_sales.round(2))

print("\nAnalysis completed!")
