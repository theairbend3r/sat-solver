import math


class Sudoku:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = self.file_path.split("/")[-1].split(".")[0]
        # self.all_sudoku_list = self.read_all_sudoku()

    def read_all_sudoku(self) -> list:
        with open(self.file_path, "r") as f:
            all_sudoku_list = f.readlines()

        return all_sudoku_list

    def encode_sudoku(self, sudoku: list) -> list:
        sudoku = sudoku[:-1]
        print(len(sudoku))
        print(sudoku)

        if int(math.sqrt(len(sudoku))) ** 2 != len(sudoku):
            raise ValueError("Incorrect sudoku length. It is not a perfect square.")

        sudoku_length = math.isqrt(len(sudoku))
        encoded_sudoku = []

        # [(1, 1, 5, 0), (1, 2, 9, 0)]
        return encoded_sudoku

    def encode_all_sudoku(self, all_sudoku_list: list):
        return [self.encode_sudoku(sudoku) for sudoku in all_sudoku_list]

    def save_soduko(self, encoded_sudoku: list):
        with open(f"./../../data/sudoku_dimacs/{self.file_name}_sudoku.cnf", "w") as f:
            f.write("p cnf 999 \n")
            for val in encoded_sudoku:
                f.write(f"{val[0]}{val[1]}{val[2]} {val[3]} \n")

    def save_all_suduko(self, all_encoded_sudoku_list: list):
        for encoded_sudoku in all_encoded_sudoku_list:
            self.save_soduko(encoded_sudoku=encoded_sudoku)


if __name__ == "__main__":
    sudoku = Sudoku(file_path="./../../data/sudoku_raw/top91.sdk.txt")
    all_sudoku_list = sudoku.read_all_sudoku()
    all_encoded_sudoku_list = sudoku.encode_all_sudoku(all_sudoku_list=all_sudoku_list)

    # save sudoku
    # sudoku.save_soduko(encoded_sudoku=[(1, 1, 5, 0), (1, 2, 9, 0)])
    sudoku.save_all_suduko(all_encoded_sudoku_list=all_encoded_sudoku_list)
