from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def filter_active_customers(df, status_column='status', active_status='active'):
    """
    Filter a DataFrame to return only active customers.

    Args:
        df: Spark DataFrame containing customer data
        status_column: Name of the column indicating customer status (default: 'status')
        active_status: Value representing active status (default: 'active')

    Returns:
        Spark DataFrame containing only active customers
    """
    return df.filter(col(status_column) == active_status)


if __name__ == "__main__":
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("CustomerFilter") \
        .getOrCreate()

    # Sample customer data
    customers_data = [
        (1, "Alice Johnson", "active"),
        (2, "Bob Smith", "inactive"),
        (3, "Carol Williams", "active"),
        (4, "David Brown", "inactive"),
        (5, "Eve Davis", "active"),
        (6, "Frank Wilson", "active")
    ]

    # Create DataFrame
    columns = ["customer_id", "name", "status"]
    df_customers = spark.createDataFrame(customers_data, schema=columns)

    print("Original Customer Data:")
    df_customers.show()

    # Filter active customers
    df_active = filter_active_customers(df_customers)

    print("Active Customers:")
    df_active.show()

    print(f"Total customers: {df_customers.count()}")
    print(f"Active customers: {df_active.count()}")

    spark.stop()
