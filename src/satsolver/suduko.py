import math


class Sudoku:
    def __init__(self, raw_sudoku_filepath: str, rules_filepath: str):
        # filepaths
        self.rules_filepath = rules_filepath
        self.raw_sudoku_filepath = raw_sudoku_filepath
        # ?? probably should convert the logic below to use regex
        self.raw_sudoku_filename = self.raw_sudoku_filepath.split("/")[-1].split(".")[0]

        # load rules and sudoku
        self.rules = self.read_rules()
        self.sudoku = self.read_sudoku()
        self.encoded_sudoku = self.encode_sudoku()

        # combine rules and sudoku into clauses
        self.clauses = self.combine_sudoku_with_rules(
            encoded_sudoku=self.encoded_sudoku, encoded_rules=self.rules
        )

    def read_rules(self) -> list:
        """Read encoded sudoku rules.

        Returns
        -------
        list
            sudoku rules.

        """
        with open(self.rules_filepath, "r") as f:
            rules = f.readlines()

        return rules

    def read_sudoku(self) -> list:
        """Read raw sudoku .txt file.

        Returns
        -------
        list
            single sudoku

        """
        with open(self.raw_sudoku_filepath, "r") as f:
            sudoku_list = f.readlines()

        return sudoku_list

    def _encode_single_sudoku(self, sudoku: list) -> list:
        """Encode a single sudoku list.

        Parameters
        ----------
        sudoku : list
            Single sudoku as a list which
            contains numbers and dots (for blank spaces).

        Returns
        -------
        list
            single encoded sudoku

        """
        # sudoku = sudoku[:-1]
        # print(len(sudoku))
        # print(sudoku)
        #
        # if int(math.sqrt(len(sudoku))) ** 2 != len(sudoku):
        #     raise ValueError("Incorrect sudoku length (not a perfect square.)")
        #
        # sudoku_length = math.isqrt(len(sudoku))
        encoded_sudoku = []

        # [(1, 1, 5, 0), (1, 2, 9, 0)]
        return encoded_sudoku

    def encode_sudoku(self) -> list:
        """Encode multiple sudokus by calling
        `self._encode_single_sudoku` on each sudoku.

        Returns
        -------
        list
            multiple encoded sudokus.

        """
        return [self._encode_single_sudoku(sudoku) for sudoku in self.sudoku]

    def combine_sudoku_with_rules(
        self, encoded_sudoku: list, encoded_rules: list
    ) -> list:
        """Combine encoded sudoku and rules into a single clause list.

        Parameters
        ----------
        encoded_sudoku : list

        encoded_rules : list


        Returns
        -------
        list
            Combined sudoku and rules.

        """
        return encoded_sudoku + encoded_rules

    def _save_single_soduko(self, encoded_sudoku: list, filename: str = ""):
        """Save a single sudoku list as a .txt file.

        Parameters
        ----------
        encoded_sudoku : list

        filename : str

        """
        with open(
            f"./../../data/sudoku_dimacs/{self.raw_sudoku_filename}_sudoku_{filename}.cnf",
            "w",
        ) as f:
            f.write("p cnf 999 \n")
            for val in encoded_sudoku:
                f.write(f"{val[0]}{val[1]}{val[2]} {val[3]} \n")

    def save_suduko(self, all_encoded_sudoku_list: list):
        """Save multiple sudokus in a .txt file.

        Parameters
        ----------
        all_encoded_sudoku_list : list

        """
        for i, encoded_sudoku in enumerate(all_encoded_sudoku_list):
            self._save_single_soduko(encoded_sudoku=encoded_sudoku, filename=str(i))


if __name__ == "__main__":
    sudoku = Sudoku(
        raw_sudoku_filepath="./../../data/sudoku_raw/top91.sdk.txt",
        rules_filepath="./../../data/sudoku_rules/sudoku-rules-9x9.txt",
    )
    print(sudoku.rules)
    print(sudoku.sudoku)
