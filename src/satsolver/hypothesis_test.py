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
    hyp_test = HypothesisTest(csv_file_path="./data/output/results.csv")
    df = hyp_test.df
    df["prefilled_boxes"] = (
        df["sudoku_file"].str.split(".").str[0].str.split("_").str[-1]
    ).astype(int)

    # t-test between different algos
    # df_baseline = df[df["algorithm"] == "Baseline"]["backtracks"]
    # df_heuristic_1 = df[df["algorithm"] == "Heuristic 1"]["backtracks"]
    # df_heuristic_2 = df[df["algorithm"] == "Heuristic 2"]["backtracks"]

    algos = ["Baseline", "Heuristic 1", "Heuristic 2"]
    multi_solution_prefilled_vals = [4, 9, 15]
    single_solution_prefilled_vals = [18]

    results_list = []
    for a in algos:
        df_algo = df[df["algorithm"] == a]
        for s in single_solution_prefilled_vals:
            df_algo_backtracks_singlesol = df_algo[df_algo["prefilled_boxes"] == s][
                "backtracks"
            ]

            for m in multi_solution_prefilled_vals:
                df_algo_backtracks_multisol = df_algo[df_algo["prefilled_boxes"] == m][
                    "backtracks"
                ]

                print(a, s, m)
                statistic, pvalue = stats.ttest_ind(
                    a=df_algo_backtracks_singlesol,
                    b=df_algo_backtracks_multisol,
                    equal_var=False,
                )
                print(statistic, pvalue)
                results_list.append([a, s, m, statistic, pvalue])

    results_df = pd.DataFrame(
        results_list,
        columns=[
            "Algorithm",
            "Unique Solution Prefilled Values",
            "Multi Solution Prefilled Values",
            "T-Value",
            "P-Value",
        ],
    )

    results_df.to_csv("./data/output/t-test.csv", index=False)
    print(results_df)
