import logging
import pandas as pd
from typing import Dict, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
DEFAULT_OUTPUT_FORMAT = "summary"


def detectNullCounts(dataframe: pd.DataFrame) -> Dict[str, int]:
    """
    Count the number of null values in each column.

    Args:
        dataframe: Input pandas DataFrame

    Returns:
        Dictionary with column names as keys and null counts as values

    Raises:
        TypeError: If input is not a pandas DataFrame
    """
    logger.info("Starting null count detection")

    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame")

        nullCounts = dataframe.isnull().sum().to_dict()
        logger.info(f"Null count detection completed. Columns processed: {len(nullCounts)}")

        return nullCounts

    except Exception as e:
        logger.error(f"Error detecting null counts: {str(e)}", exc_info=True)
        raise


def detectNullPercentage(dataframe: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate the percentage of null values in each column.

    Args:
        dataframe: Input pandas DataFrame

    Returns:
        Dictionary with column names as keys and null percentages as values

    Raises:
        TypeError: If input is not a pandas DataFrame
        ValueError: If DataFrame is empty
    """
    logger.info("Starting null percentage detection")

    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame")

        if dataframe.empty:
            raise ValueError("DataFrame is empty")

        totalRows = len(dataframe)
        nullCounts = dataframe.isnull().sum()
        nullPercentages = (nullCounts / totalRows * 100).to_dict()

        logger.info(f"Null percentage detection completed. Total rows: {totalRows}")

        return nullPercentages

    except Exception as e:
        logger.error(f"Error detecting null percentages: {str(e)}", exc_info=True)
        raise


def detectNullRows(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Identify rows that contain at least one null value.

    Args:
        dataframe: Input pandas DataFrame

    Returns:
        DataFrame containing only rows with null values

    Raises:
        TypeError: If input is not a pandas DataFrame
    """
    logger.info("Starting null row detection")

    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame")

        nullRows = dataframe[dataframe.isnull().any(axis=1)]
        logger.info(f"Null row detection completed. Rows with nulls: {len(nullRows)}")

        return nullRows

    except Exception as e:
        logger.error(f"Error detecting null rows: {str(e)}", exc_info=True)
        raise


def generateNullReport(dataframe: pd.DataFrame) -> Tuple[Dict, Dict, pd.DataFrame]:
    """
    Generate a comprehensive null value report.

    Args:
        dataframe: Input pandas DataFrame

    Returns:
        Tuple containing (null_counts, null_percentages, rows_with_nulls)

    Raises:
        TypeError: If input is not a pandas DataFrame
    """
    logger.info("Starting comprehensive null value report generation")

    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame")

        nullCounts = detectNullCounts(dataframe)
        nullPercentages = detectNullPercentage(dataframe)
        rowsWithNulls = detectNullRows(dataframe)

        logger.info(f"Null report generation completed successfully")

        return nullCounts, nullPercentages, rowsWithNulls

    except Exception as e:
        logger.error(f"Error generating null report: {str(e)}", exc_info=True)
        raise


def printNullReport(nullCounts: Dict[str, int], nullPercentages: Dict[str, float]) -> None:
    """
    Print null value report in a formatted manner.

    Args:
        nullCounts: Dictionary with null counts per column
        nullPercentages: Dictionary with null percentages per column
    """
    logger.info("Printing null value report")

    try:
        print("\n" + "="*60)
        print("NULL VALUE DETECTION REPORT")
        print("="*60)

        print("\nColumn-wise Null Analysis:")
        print("-" * 60)
        print(f"{'Column':<30} {'Null Count':<15} {'Null %':<15}")
        print("-" * 60)

        for column in nullCounts.keys():
            count = nullCounts[column]
            percentage = nullPercentages[column]
            print(f"{column:<30} {count:<15} {percentage:>6.2f}%")

        print("="*60 + "\n")

    except Exception as e:
        logger.error(f"Error printing null report: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    logger.info("Pipeline started")

    try:
        # Sample data with null values
        sampleData = {
            'employee_id': [1001, 1002, 1003, 1004, 1005],
            'name': ['Alice Johnson', None, 'Carol Williams', 'David Brown', 'Eve Davis'],
            'department': ['Sales', 'Engineering', None, 'Engineering', 'Finance'],
            'salary': [65000, 85000, 55000, None, 72000],
            'email': ['alice@company.com', 'bob@company.com', None, 'david@company.com', None]
        }

        df = pd.DataFrame(sampleData)
        logger.info(f"Sample DataFrame created with {len(df)} rows and {len(df.columns)} columns")

        # Generate comprehensive report
        nullCounts, nullPercentages, rowsWithNulls = generateNullReport(df)

        # Print report
        printNullReport(nullCounts, nullPercentages)

        # Display rows with nulls
        print("Rows containing null values:")
        print("-" * 60)
        print(rowsWithNulls)
        print()

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}", exc_info=True)
        raise
