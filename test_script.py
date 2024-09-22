""" file for testing code"""

from script import summary, points_plot


def test_summary():
    """test descriptive statistics function"""
    summary()


def test_plot():
    """test plot function"""
    points_plot()


if __name__ == "__main__":
    test_summary()
    test_plot()
