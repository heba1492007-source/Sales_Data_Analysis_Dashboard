import pandas as pd
import matplotlib.pyplot as plt

# Read Data

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Data Cleaning
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df = df.drop_duplicates()

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

#KPIS
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

# Data for Charts

category_sales = df.groupby("Category")["Sales"].sum()

region_sales = df.groupby("Region")["Sales"].sum()

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_sales = (
    df.groupby("Month Name")["Sales"]
      .sum()
      .reindex(month_order)
)

# Dashboard
fig = plt.figure(figsize=(16,10))

fig.suptitle("Sales Data Analysis Dashboard",
             fontsize=20,
             fontweight="bold")

#KPIS

plt.figtext(
    0.02,
    0.92,
    f"Total Sales: ${total_sales:,.2f}\n"
    f"Total Profit: ${total_profit:,.2f}\n"
    f"Total Orders: {total_orders}\n"
    f"Total Customers: {total_customers}",
    fontsize=12,
    bbox=dict(facecolor="lightyellow")
)

# Chart 1
ax1 = plt.subplot(2,2,1)
category_sales.plot(kind="bar", ax=ax1)
ax1.set_title("Sales by Category")

# Chart 2
ax2 = plt.subplot(2,2,2)
region_sales.plot(kind="bar", ax=ax2)
ax2.set_title("Sales by Region")

# Chart 3
ax3 = plt.subplot(2,1,2)
monthly_sales.plot(kind="line", marker="o", ax=ax3)
ax3.set_title("Monthly Sales")

plt.tight_layout(rect=[0,0,1,0.90])

plt.savefig("charts/dashboard.png")

plt.show()