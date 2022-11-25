from operator import index
import pandas as pd
import scipy.stats as stats
from itertools import combinations


class HypothesisTest:
    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        self.df = pd.read_csv(self.csv_file_path)

    def t_test():
        pass


if __name__ == "__main__":
    hyp_test = HypothesisTest(csv_file_path="./data/output/complete_stats_freek.csv")
    df = hyp_test.df
    df_baseline = df[df["algorithm"] == "Baseline"]["backtracks"]
    df_heuristic_1 = df[df["algorithm"] == "Heuristic 1"]["backtracks"]
    df_heuristic_2 = df[df["algorithm"] == "Heuristic 2"]["backtracks"]

    labels = ["baseline", "heuristic 1", "heuristic 2"]
    data = [df_baseline, df_heuristic_1, df_heuristic_2]

    labels_combo = combinations(labels, 2)
    data_combo = combinations(data, 2)

    results_df = pd.DataFrame(columns=["Data 1", "Data 2", "Statistic", "P-Value"])
    results_list = []
    for lbl, d in zip(labels_combo, data_combo):
        print(lbl)
        statistic, pvalue = stats.ttest_ind(a=d[0], b=d[1], equal_var=False)
        print(statistic, pvalue)
        results_list.append([lbl[0], lbl[1], statistic, pvalue])

    results_df = pd.DataFrame(
        results_list, columns=["Data 1", "Data 2", "Statistic", "P-Value"]
    )

    results_df.to_csv("./data/output/t-test.csv", index=False)
    print(results_df)
