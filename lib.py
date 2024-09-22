"""file for modules"""


def summary(dataframe):
    """provides summary statistics"""
    summary_stats = dataframe.describe()
    print(summary_stats)
