import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
sns.set_style("whitegrid")
sns.set(font_scale=1.5, rc={"text.usetex": True})


class Visualisation:
    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        self.df = pd.read_csv(self.csv_file_path)
        self.df["prefilled_boxes"] = (
            self.df["sudoku_file"].str.split(".").str[0].str.split("_").str[-1]
        )  # .astype(int)

    def histogram_num_backtracks(self):
        bins = [0, 1, 10, 50, 100, 200, np.inf]
        labels = ["0", "1-10", "11-50", "51-99", "99-200", "200+"]

        self.df["freq"] = pd.cut(self.df["backtracks"], bins, labels=labels)

        sns.barplot(data=self.df, x="freq", y="backtracks", hue="algorithm").set(
            title="Backtracks Per Algorithm",
            xlabel="Algorithm",
            ylabel="Number of Backtracks",
        )
        plt.savefig("./plots/histogram_num_backtracks.png")
        # plt.show()

    def compare_algo_across_prefilled_boxes(self):

        # create data
        mean_time_df = (
            self.df.groupby(["algorithm", "prefilled_boxes"])
            .agg({"time_elapsed": "mean"})
            .reset_index()
        )

        mean_backtracks_df = (
            self.df.groupby(["algorithm", "prefilled_boxes"])
            .agg({"backtracks": "mean"})
            .reset_index()
        )

        # plot figure
        fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True, sharey=True)
        fig.suptitle("Time and Backtracks for each Algorithm")

        # time elapsed
        sns.lineplot(
            data=mean_time_df,
            x="prefilled_boxes",
            y="time_elapsed",
            hue="algorithm",
            ax=axes[0],
        ).set(
            title="Average Runtime vs Number of Prefilled Cells",
            xlabel="Number of Prefilled Cells",
            ylabel="Time Elapsed (seconds)",
        )
        # backtracks
        sns.lineplot(
            data=mean_backtracks_df,
            x="prefilled_boxes",
            y="backtracks",
            hue="algorithm",
            ax=axes[1],
        ).set(
            title="Average Number of Backtracks vs Number of Prefilled Cells",
            xlabel="Number of Prefilled Cells",
            ylabel="Number of Backtracks",
        )

        fig.savefig("./plots/compare_algo_across_prefilled_boxes.png")
        # plt.show()


if __name__ == "__main__":
    visualisation = Visualisation(
        csv_file_path="./data/output/experiment_stats_2022_11_22_20_59.csv"
    )
    # visualisation.histogram_num_backtracks()
    visualisation.compare_algo_across_prefilled_boxes()
