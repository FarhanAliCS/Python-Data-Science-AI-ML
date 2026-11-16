import numpy as np


# ============================================================
#                  SALES DATA GENERATION
# ============================================================

np.random.seed(100)

# Generate sales data for four products (7 days)
product1 = np.random.randint(1, 51, size=7)
product2 = np.random.randint(1, 51, size=7)
product3 = np.random.randint(1, 51, size=7)
product4 = np.random.randint(1, 51, size=7)

# Create the sales dataset
sales_dataset = np.column_stack((
    product1,
    product2,
    product3,
    product4
))

# Product prices
price = np.array([100, 250, 150, 300])


# ============================================================
#                    REVENUE ANALYSIS
# ============================================================

# Calculate revenue for each product
revenue = sales_dataset * price

# Calculate total revenue for each day
daily_revenue = np.sum(revenue, axis=1)

# Calculate total revenue for each product
one_product_revenue = np.sum(revenue, axis=0)

# Identify highest and lowest revenue days
highest_revenue_day = np.argmax(daily_revenue)
lowest_revenue_day = np.argmin(daily_revenue)

# Sort revenue values
sorted_revenue = np.argsort(daily_revenue)


# ============================================================
#                    DATASET INFORMATION
# ============================================================

print("\n" + "=" * 50)
print("                 SALES DATASET")
print("=" * 50)

print(sales_dataset)

print("\nDataset Information:")
print("Shape       :", sales_dataset.shape)
print("Dimensions  :", sales_dataset.ndim)
print("Data Type   :", sales_dataset.dtype)


# ============================================================
#                    DAILY REVENUE
# ============================================================

print("\n" + "=" * 50)
print("                 REVENUE ANALYSIS")
print("=" * 50)

print("\nRevenue Per Product:\n", revenue)

print("\nTotal Revenue Per Day:", daily_revenue)

print("\nTotal Revenue Per Product:", one_product_revenue)


# ============================================================
#                 HIGHEST AND LOWEST REVENUE
# ============================================================

print("\nHighest Revenue Day:")
print(
    f"Day: {highest_revenue_day + 1} | "
    f"Revenue: {daily_revenue[highest_revenue_day]}"
)

print("\nLowest Revenue Day:")
print(
    f"Day: {lowest_revenue_day + 1} | "
    f"Revenue: {daily_revenue[lowest_revenue_day]}"
)


# ============================================================
#                 REVENUE FILTERING
# ============================================================

print("\nRevenue Greater Than 20,000:")

mask = daily_revenue > 20000

greater_revenue = daily_revenue[mask]

days = np.arange(1, 8)

print("Days    :", days[mask])
print("Revenue :", daily_revenue[mask])


# ============================================================
#                 SORTED DAILY REVENUE
# ============================================================

sorted_revenue = np.sort(daily_revenue)[::-1]

print("\nSorted Daily Revenue (Highest to Lowest):")
print(sorted_revenue)


# ============================================================
#                 REVENUE COMPARISON
# ============================================================

print("\n" + "=" * 50)
print("                 REVENUE COMPARISON")
print("=" * 50)

# Generate a second sales dataset
np.random.seed(66)
product5 = np.random.randint(1, 51, size=7)
product6 = np.random.randint(1, 51, size=7)
product7 = np.random.randint(1, 51, size=7)
product8 = np.random.randint(1, 51, size=7)

second_dataset = np.column_stack((
    product5,
    product6,
    product7,
    product8
))

# Calculate daily revenue for the second dataset
sum_product = np.sum(second_dataset * price, axis=1)

# Calculate total revenue for both datasets
total_revenue_1 = np.sum(daily_revenue)
total_revenue_2 = np.sum(sum_product)

print("First Dataset Revenue :", total_revenue_1)
print("Second Dataset Revenue:", total_revenue_2)

if total_revenue_1 > total_revenue_2:
    print("\nFirst dataset generated more revenue.")

elif total_revenue_2 > total_revenue_1:
    print("\nSecond dataset generated more revenue.")

else:
    print("\nBoth datasets generated equal revenue.")


# ============================================================
#                 BEST-SELLING PRODUCT
# ============================================================

print("\n" + "=" * 50)
print("                 BEST-SELLING PRODUCT")
print("=" * 50)

# Calculate total units sold for each product
product_units_sold = np.sum(sales_dataset, axis=0)

best_selling_product = np.argmax(product_units_sold)

print("Total Units Sold:", product_units_sold)
print("Best-Selling Product:", best_selling_product + 1)


# ============================================================
#                 REVENUE PERCENTAGE
# ============================================================

print("\n" + "=" * 50)
print("                 REVENUE PERCENTAGE")
print("=" * 50)

# Calculate total revenue across all products
total_revenue_all_products = np.sum(one_product_revenue)

# Calculate revenue percentage for each product
percentage = (
    one_product_revenue / total_revenue_all_products
) * 100

highest_percentage = np.argmax(percentage)

# Display revenue contribution of each product
for i, value in enumerate(percentage):
    print(f"Product {i + 1}: {value:.2f}%")

print("\nTotal Percentage:", np.sum(percentage))

print(
    "Highest Revenue Contribution: Product",
    highest_percentage + 1
)


# ============================================================
#                     END OF PROJECT
# ============================================================

print("\n" + "=" * 50)
print("          SALES ANALYSIS COMPLETED")
print("=" * 50)