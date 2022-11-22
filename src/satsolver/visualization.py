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

    def compare_average_algo_runtime(self):
        agg_df = (
            self.df.groupby(["algorithm"]).agg({"time_elapsed": "mean"}).reset_index()
        )
        sns.barplot(data=agg_df, x="algorithm", y="time_elapsed",).set(
            title="Average Runtime Per Algorithm",
            xlabel="DPLL Algorithms",
            ylabel="Time Elapsed (seconds)",
        )
        plt.savefig("./plots/average_algo_runtime.png")
        plt.show()


if __name__ == "__main__":
    visualisation = Visualisation(csv_file_path="./data/output/experiment_stats.csv")
    visualisation.compare_average_algo_runtime()
