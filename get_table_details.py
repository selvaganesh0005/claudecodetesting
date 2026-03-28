"""
Script to retrieve and display table details from Test_DB database.
Connects to SQL Server and fetches information about all tables and their columns.
"""

import pyodbc
import logging
from typing import List, Dict, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database connection constants
SERVER = "SELVA\\SQLEXPRESS"
USERNAME = "claude_user"
PASSWORD = "YourPassword@123"
DATABASE = "Test_DB"
DRIVER = "{ODBC Driver 17 for SQL Server}"


def getConnectionString() -> str:
    """
    Build and return the ODBC connection string.

    Returns:
        str: ODBC connection string for SQL Server
    """
    connectionString = (
        f"DRIVER={DRIVER};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD}"
    )
    return connectionString


def connectToDatabase() -> pyodbc.Connection:
    """
    Establish connection to the SQL Server database.

    Returns:
        pyodbc.Connection: Database connection object

    Raises:
        Exception: If connection fails
    """
    try:
        logger.info(f"Connecting to {SERVER} database: {DATABASE}")
        connectionString = getConnectionString()
        connection = pyodbc.connect(connectionString)
        logger.info("Database connection successful")
        return connection
    except Exception as error:
        logger.error(f"Failed to connect to database: {str(error)}")
        raise


def getTables(connection: pyodbc.Connection) -> List[str]:
    """
    Retrieve list of all user-defined tables in the database.

    Args:
        connection: Active database connection

    Returns:
        List[str]: List of table names

    Raises:
        Exception: If query fails
    """
    try:
        logger.info("Fetching table names from database")
        cursor = connection.cursor()
        query = """
            SELECT TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_TYPE = 'BASE TABLE'
            ORDER BY TABLE_NAME
        """
        cursor.execute(query)
        tables = [row[0] for row in cursor.fetchall()]
        logger.info(f"Found {len(tables)} tables in {DATABASE}")
        return tables
    except Exception as error:
        logger.error(f"Failed to fetch tables: {str(error)}")
        raise


def getTableColumns(connection: pyodbc.Connection, tableName: str) -> List[Dict]:
    """
    Retrieve column details for a specific table.

    Args:
        connection: Active database connection
        tableName: Name of the table

    Returns:
        List[Dict]: List of column information dictionaries

    Raises:
        Exception: If query fails
    """
    try:
        logger.info(f"Fetching column details for table: {tableName}")
        cursor = connection.cursor()
        query = f"""
            SELECT
                COLUMN_NAME,
                DATA_TYPE,
                IS_NULLABLE,
                CHARACTER_MAXIMUM_LENGTH
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{tableName}'
            ORDER BY ORDINAL_POSITION
        """
        cursor.execute(query)
        columns = []
        for row in cursor.fetchall():
            columnDict = {
                'name': row[0],
                'dataType': row[1],
                'isNullable': row[2],
                'maxLength': row[3]
            }
            columns.append(columnDict)
        logger.info(f"Found {len(columns)} columns in {tableName}")
        return columns
    except Exception as error:
        logger.error(f"Failed to fetch columns for {tableName}: {str(error)}")
        raise


def getTableRowCount(connection: pyodbc.Connection, tableName: str) -> int:
    """
    Get the number of rows in a table.

    Args:
        connection: Active database connection
        tableName: Name of the table

    Returns:
        int: Number of rows in the table

    Raises:
        Exception: If query fails
    """
    try:
        cursor = connection.cursor()
        query = f"SELECT COUNT(*) FROM {tableName}"
        cursor.execute(query)
        rowCount = cursor.fetchone()[0]
        return rowCount
    except Exception as error:
        logger.error(f"Failed to fetch row count for {tableName}: {str(error)}")
        raise


def displayTableDetails(connection: pyodbc.Connection, tables: List[str]) -> None:
    """
    Display detailed information for all tables.

    Args:
        connection: Active database connection
        tables: List of table names
    """
    try:
        logger.info("Displaying table details")
        print("\n" + "="*80)
        print(f"TABLE DETAILS FOR DATABASE: {DATABASE}")
        print("="*80 + "\n")

        for tableName in tables:
            columns = getTableColumns(connection, tableName)
            rowCount = getTableRowCount(connection, tableName)

            print(f"TABLE: {tableName}")
            print(f"Row Count: {rowCount}")
            print(f"Columns: {len(columns)}")
            print("-" * 80)
            print(f"{'Column Name':<30} {'Data Type':<20} {'Nullable':<15} {'Max Length':<15}")
            print("-" * 80)

            for column in columns:
                maxLength = column['maxLength'] if column['maxLength'] else "N/A"
                isNullable = "YES" if column['isNullable'] == "YES" else "NO"
                print(f"{column['name']:<30} {column['dataType']:<20} {isNullable:<15} {str(maxLength):<15}")

            print("\n")

        logger.info("Table details display completed")
    except Exception as error:
        logger.error(f"Failed to display table details: {str(error)}")
        raise


def main() -> None:
    """
    Main function to orchestrate the script execution.
    Connects to database, fetches table details, and displays the information.
    """
    connection = None
    try:
        logger.info("Starting table details retrieval script")

        # Connect to database
        connection = connectToDatabase()

        # Get all tables
        tables = getTables(connection)

        if not tables:
            logger.warning("No tables found in the database")
            print("No tables found in the database")
            return

        # Display table details
        displayTableDetails(connection, tables)

        logger.info("Script execution completed successfully")
        print("\n" + "="*80)
        print("SUMMARY")
        print("="*80)
        print(f"Database: {DATABASE}")
        print(f"Total Tables: {len(tables)}")
        print(f"Tables: {', '.join(tables)}")
        print("="*80 + "\n")

    except Exception as error:
        logger.error(f"Script execution failed: {str(error)}")
        print(f"Error: {str(error)}")
    finally:
        if connection:
            connection.close()
            logger.info("Database connection closed")


if __name__ == "__main__":
    main()
