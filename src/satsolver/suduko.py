class Sudoku:
    def __init__(self, file_path: str):
        self.file_path = file_path
        # self.all_sudoku_list = self.read_all_sudoku()
        # self.all_sudoku_list = self.read_all_sudoku()

    def read_all_sudoku(self) -> list:
        with open(self.file_path, "r") as f:
            all_sudoku_list = f.readlines()

        return all_sudoku_list

    def encode_sudoku(self, sudoku):
        return sudoku

    def encode_all_sudoku(self):
        pass

    def save_soduko(self):
        pass

    def save_all_suduko(self):
        pass


if __name__ == "__main__":
    sudoku = Sudoku(file_path="./../../data/sudoku_raw/top91.sdk.txt")
