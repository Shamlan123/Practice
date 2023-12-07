import pandas as pd

def read_orders_csv(file_path):
    try:
        # Read CSV file into a DataFrame
        orders_df = pd.read_csv(file_path)
        return orders_df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def compute_monthly_revenue(orders_df):
    try:
        # Convert 'order_date' column to datetime format
        orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])

        # Extract month and year from the 'order_date' column
        orders_df['month_year'] = orders_df['order_date'].dt.to_period('M')

        # Compute total revenue for each month
        monthly_revenue = orders_df.groupby('month_year')['product_price'].sum()
        return monthly_revenue
    except Exception as e:
        print(f"Error computing monthly revenue: {e}")
        return None

def compute_product_revenue(orders_df):
    try:
        # Compute total revenue for each product
        product_revenue = orders_df.groupby('product_id')['product_price'].sum()
        return product_revenue
    except Exception as e:
        print(f"Error computing product revenue: {e}")
        return None

def compute_customer_revenue(orders_df):
    try:
        # Compute total revenue for each customer
        customer_revenue = orders_df.groupby('customer_id')['product_price'].sum()
        return customer_revenue
    except Exception as e:
        print(f"Error computing customer revenue: {e}")
        return None

def identify_top_customers(customer_revenue):
    try:
        # Identify top 10 customers by revenue
        top_customers = customer_revenue.sort_values(ascending=False).head(10)
        return top_customers
    except Exception as e:
        print(f"Error identifying top customers: {e}")
        return None
