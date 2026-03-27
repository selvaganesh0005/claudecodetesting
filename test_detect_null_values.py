import pytest
import pandas as pd
from detect_null_values import (
    detectNullCounts,
    detectNullPercentage,
    detectNullRows,
    generateNullReport
)


class TestDetectNullCounts:
    """Test cases for detectNullCounts function"""

    def test_detectNullCounts_with_no_nulls(self):
        """Test null count detection with DataFrame containing no nulls"""
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })

        result = detectNullCounts(df)

        assert result['col1'] == 0
        assert result['col2'] == 0

    def test_detectNullCounts_with_nulls(self):
        """Test null count detection with DataFrame containing nulls"""
        df = pd.DataFrame({
            'col1': [1, None, 3],
            'col2': ['a', 'b', None]
        })

        result = detectNullCounts(df)

        assert result['col1'] == 1
        assert result['col2'] == 1

    def test_detectNullCounts_all_nulls(self):
        """Test null count detection when column is entirely null"""
        df = pd.DataFrame({
            'col1': [None, None, None],
            'col2': [1, 2, 3]
        })

        result = detectNullCounts(df)

        assert result['col1'] == 3
        assert result['col2'] == 0

    def test_detectNullCounts_invalid_input(self):
        """Test null count detection with invalid input type"""
        with pytest.raises(TypeError):
            detectNullCounts([1, 2, 3])

    def test_detectNullCounts_empty_dataframe(self):
        """Test null count detection with empty DataFrame"""
        df = pd.DataFrame()

        result = detectNullCounts(df)

        assert isinstance(result, dict)


class TestDetectNullPercentage:
    """Test cases for detectNullPercentage function"""

    def test_detectNullPercentage_no_nulls(self):
        """Test null percentage calculation with no nulls"""
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })

        result = detectNullPercentage(df)

        assert result['col1'] == 0.0
        assert result['col2'] == 0.0

    def test_detectNullPercentage_with_nulls(self):
        """Test null percentage calculation with nulls"""
        df = pd.DataFrame({
            'col1': [1, None, 3, 4],
            'col2': ['a', 'b', None, None]
        })

        result = detectNullPercentage(df)

        assert result['col1'] == 25.0
        assert result['col2'] == 50.0

    def test_detectNullPercentage_all_nulls(self):
        """Test null percentage when all values are null"""
        df = pd.DataFrame({
            'col1': [None, None, None],
            'col2': [1, 2, 3]
        })

        result = detectNullPercentage(df)

        assert result['col1'] == 100.0
        assert result['col2'] == 0.0

    def test_detectNullPercentage_invalid_input(self):
        """Test null percentage with invalid input type"""
        with pytest.raises(TypeError):
            detectNullPercentage({'key': 'value'})

    def test_detectNullPercentage_empty_dataframe(self):
        """Test null percentage with empty DataFrame"""
        df = pd.DataFrame()

        with pytest.raises(ValueError):
            detectNullPercentage(df)


class TestDetectNullRows:
    """Test cases for detectNullRows function"""

    def test_detectNullRows_no_nulls(self):
        """Test null row detection with no null values"""
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })

        result = detectNullRows(df)

        assert len(result) == 0

    def test_detectNullRows_with_nulls(self):
        """Test null row detection with null values"""
        df = pd.DataFrame({
            'col1': [1, None, 3],
            'col2': ['a', 'b', None]
        })

        result = detectNullRows(df)

        assert len(result) == 2

    def test_detectNullRows_single_null_row(self):
        """Test null row detection with single row containing null"""
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', None, 'c']
        })

        result = detectNullRows(df)

        assert len(result) == 1
        assert result.index[0] == 1

    def test_detectNullRows_invalid_input(self):
        """Test null row detection with invalid input"""
        with pytest.raises(TypeError):
            detectNullRows("not a dataframe")


class TestGenerateNullReport:
    """Test cases for generateNullReport function"""

    def test_generateNullReport_returns_tuple(self):
        """Test that generateNullReport returns a tuple"""
        df = pd.DataFrame({
            'col1': [1, None, 3],
            'col2': ['a', 'b', None]
        })

        result = generateNullReport(df)

        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_generateNullReport_content(self):
        """Test generateNullReport content"""
        df = pd.DataFrame({
            'col1': [1, None, 3],
            'col2': ['a', 'b', None]
        })

        nullCounts, nullPercentages, rowsWithNulls = generateNullReport(df)

        assert isinstance(nullCounts, dict)
        assert isinstance(nullPercentages, dict)
        assert isinstance(rowsWithNulls, pd.DataFrame)
        assert len(rowsWithNulls) == 2

    def test_generateNullReport_invalid_input(self):
        """Test generateNullReport with invalid input"""
        with pytest.raises(TypeError):
            generateNullReport([1, 2, 3])

    def test_generateNullReport_no_nulls(self):
        """Test generateNullReport with DataFrame containing no nulls"""
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })

        nullCounts, nullPercentages, rowsWithNulls = generateNullReport(df)

        assert all(count == 0 for count in nullCounts.values())
        assert len(rowsWithNulls) == 0
