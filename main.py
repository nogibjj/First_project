"""main file with main functions"""

import pandas as pd
import matplotlib.pyplot as plt
import markdownify as md
import numpy as np
from ydata_profiling import ProfileReport


FILE_PATH = "NBA_24_stats.csv"
df = pd.read_csv(FILE_PATH)


def summary():
    """provides summary statistics"""
    summary_stats = df.describe()
    print(summary_stats)


def points_plot():
    """provides visualization"""
    accurate = df[df["3P%"] >= 0.5]
    player_rank = accurate["Player"].astype(str)
    plt.barh(player_rank, width=accurate["PTS"], color="green")
    plt.xlabel("PPG")
    plt.ylabel("Players")
    plt.title("PPG for Players with 50% or higher 3P%")
    plt.subplots_adjust(left=0.25)
    plt.savefig("NBA_pts_bar.png")
    plt.show()


def report():
    "generates report and converts to pdf"
    profile = ProfileReport(df, title="NBA Statistics")
    export = profile.to_html()
    markdown = md.markdownify(export)
    with open("NBA_report.md", "w", encoding="utf-8") as f_write:
        f_write.write(markdown)


points_plot()
# report()
