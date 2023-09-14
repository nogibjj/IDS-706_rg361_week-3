"""Test file to verify main function"""

import pandas as pd
from main import descriptive_stats


def test_stat():
    # initialize list elements

    fname = "./resources/blood_pressure.csv"
    # Create the pandas DataFrame
    df = pd.read_csv(fname)

    # Test case 1: col number specified
    col = 3
    assert [
        df.iloc[:, col].mean(),
        df.iloc[:, col].median(),
        df.iloc[:, col].std(),
    ] == descriptive_stats(fname, 4)

    # Test case 2: col number not specified, shoudl use last column
    col = 4
    assert [
        df.iloc[:, col].mean(),
        df.iloc[:, col].median(),
        df.iloc[:, col].std(),
    ] == descriptive_stats(fname)


test_stat()
