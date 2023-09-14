""" Function to return the descriptive statistics of a Pandas Dataframe"""
import pandas as pd

import matplotlib.pyplot as plt


def descriptive_stats(fname, col=None):
    df = pd.read_csv(fname)

    if col == None:
        col = len(df.axes[1]) - 1
    else:
        col = col - 1

    col_name = df.columns[col]

    # create Histogram and save as output.png in output folder
    plt.hist(df[col_name])
    plt.ylabel("Count of " + col_name)
    plt.xlabel(col_name)
    plt.title("Data Loaded from : " + fname)
    plt.savefig("./resources/output.png")  # change the filepath here in case reequired
    plt.clf()

    # Write the summary statistics to a summary.md in output folder
    with open("./resources/summary.md", "w", encoding="utf-8") as f:
        f.write("Mean: " + str(df.iloc[:, col].mean()) + "\n")
        f.write("\n")
        f.write("Median: " + str(df.iloc[:, col].median()) + "\n")
        f.write("\n")
        f.write("Standard Deviation: " + str(df.iloc[:, col].std()))

    return [df.iloc[:, col].mean(), df.iloc[:, col].median(), df.iloc[:, col].std()]
