from main import KrestikiNoliki
import time

class TestKrestikiNoliki:

    def setup(self):
        self.krestitinoliki1 = KrestikiNoliki(3)

    def test_board(self):
        assert len(self.krestitinoliki1.board_) == 3

    def test_make_move(self):
        self.krestitinoliki1.make_move(1, 2, "0")
        assert self.krestitinoliki1.board_[0][1] == "0"

    def test_minimax(self):
        self.krestitinoliki1.board_ = [[" ", " ", " "], [" ", " ", " "], ["X", " ", " "]]
        tmp = self.krestitinoliki1.find_move()
        self.krestitinoliki1.make_move(tmp[0], tmp[1], "0")
        assert self.krestitinoliki1.board_[1][1] == " "

    def test_minimax2(self):
        self.krestitinoliki1.board_ = [["X", "0", " "], [" ", "X", " "], [" ", " ", " "]]
        tmp = self.krestitinoliki1.find_move()
        self.krestitinoliki1.make_move(tmp[0] + 1, tmp[1] + 1, "0")
        assert self.krestitinoliki1.board_[2][2] == "0"

    def test_minimax3(self):
        self.krestitinoliki1.board_ = [["X", "0", " "], ["X", " ", " "], [" ", " ", " "]]
        tmp = self.krestitinoliki1.find_move()
        assert self.krestitinoliki1.find_move() == [2, 0]

    def test_time(self):
        start = time.time()
        self.krestitinoliki1.board_ = [["X", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        tmp = self.krestitinoliki1.find_move()
        end = time.time()
        assert end - start < 1

    def test_check(self):
        self.krestitinoliki1.board_ = [["X", "0", "X"], ["X", "0", " "], [" ", "0", " "]]
        assert self.krestitinoliki1.check("0") == True
        self.krestitinoliki1.board_ = [["X", "0", " "], ["X", "0", " "], ["X", " ", " "]]
        assert self.krestitinoliki1.check("X") == True

    def test_game_over(self):
        self.krestitinoliki1.board_ = [["X", "0", "X"], ["X", "0", "X"], ["0", "X", "0"]]
        assert self.krestitinoliki1.game_over() == True

    def test_find_available_points(self):
        self.krestitinoliki1.board_ = [["X", "0", "X"], ["X", " ", " "], [" ", "X", "0"]]
        assert len(self.krestitinoliki1.find_available_points()) == 3