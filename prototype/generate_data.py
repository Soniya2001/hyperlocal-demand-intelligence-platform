import pandas as pd
import numpy as np
import random

# -----------------------------
# Configuration
# -----------------------------
NUM_ROWS = 500

regions = [
    "Madurai", "Trichy", "Salem",
    "Coimbatore", "Villupuram",
    "Tirunelveli", "Erode"
]

categories = {
    "Accessories": ["Earrings", "Necklace", "Bangles", "Bracelet"],
    "Footwear": ["Running Shoes", "Sandals", "Slippers"],
    "Bags": ["Handbag", "Backpack", "Travel Bag"],
    "Textiles": ["Saree", "Shirt", "Kurti"],
    "Home Goods": ["Water Bottle", "Lunch Box", "Storage Box"]
}

data = []

for i in range(NUM_ROWS):
    seller_id = random.randint(1000, 1100)
    
    category = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])
    
    region = random.choice(regions)
    
    # Create realistic demand imbalance
    if region in ["Madurai", "Coimbatore"]:
        monthly_sales = np.random.randint(40, 100)
        stock_quantity = np.random.randint(20, 80)
    elif region in ["Villupuram", "Tirunelveli"]:
        monthly_sales = np.random.randint(5, 30)
        stock_quantity = np.random.randint(100, 300)
    else:
        monthly_sales = np.random.randint(15, 60)
        stock_quantity = np.random.randint(50, 150)

    product_id = random.randint(100, 999)

    data.append([
        seller_id,
        product_id,
        product_name,
        category,
        region,
        stock_quantity,
        monthly_sales
    ])

columns = [
    "seller_id",
    "product_id",
    "product_name",
    "category",
    "region",
    "stock_quantity",
    "monthly_sales"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("hyperlocal_inventory_data.csv", index=False)

print("Dataset generated successfully: hyperlocal_inventory_data.csv")