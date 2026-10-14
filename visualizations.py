import pandas as pd 
import matplotlib.pyplot as plt 
from pathlib import Path 

df=pd.read_csv("data/Superstore_clean.csv",encoding="latin1")

df["Order Date"]=pd.to_datetime(df["Order Date"])

Path("visualizations").mkdir(exist_ok=True)

sales_category=df.groupby("Category")["Sales"].sum().sort_values()
ax=sales_category.plot(kind="bar",title="Total Sales by Category",figsize=(8,5))
ax.set_ylabel("Sales")
ax.set_xlabel("Product Category")
ax.bar_label(ax.containers[0],fmt="$%.0f",padding=3)
plt.tight_layout()
plt.savefig("visualizations/sales_by_category.png",dpi=150)
plt.close()

profit_category=df.groupby("Category")["Profit"].sum().sort_values()
profit_category.plot(kind="bar", title="Total Profit by Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("visualizations/profit_by_category.png")
plt.close()

sales_region = df.groupby("Region")["Sales"].sum().sort_values()
sales_region.plot(kind="bar", title="Total Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_region.png")
plt.close()

monthly_sales=(
    df.set_index("Order Date")["Sales"].resample("MS").sum()
)
monthly_sales.plot(kind="line",title="Monthly Sales Trend",figsize=(10,5))
plt.ylabel("Sales")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png")
plt.close()

top_products=(
    df.groupby("Product Name")["Sales"].sum().nlargest(10).sort_values()
)
top_products.plot(kind="barh",title="Top 10 Products by Sales",figsize=(10,7))
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig("visualizations/top_10_products.png")
plt.close()