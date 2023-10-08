class KrestikiNoliki:
    def __init__(self, nn):
        self.n_ = nn
        self.board_ = [[" " for i in range(nn)] for j in range(nn)]

    def __str__(self):
        ans = ""
        for i in range(self.n_):
            for j in range(self.n_):
                if self.board_[i][j] == " ":
                    ans += " |_| "
                else:
                    ans += " |" + self.board_[i][j] + "| "
            ans += "\n"
        return ans

    def make_move(self, x, y, p):
        if 1 <= x <= self.n_ and 1 <= y <= self.n_:
            if self.board_[x - 1][y - 1] == " ":
                self.board_[x - 1][y - 1] = p
                print(self)
                return True
            print('This place are already holden')
            return False
        print('Bad x, y')
        return False

    def check(self, p):
        win_d = True
        win_d_r = True
        for i in range(self.n_):
            win_v = True
            win_g = True
            if self.board_[i][i] != p:
                win_d = False
            if self.board_[i][self.n_ - i - 1] != p:
                win_d_r = False
            for j in range(self.n_):
                if self.board_[i][j] != p:
                    win_v = False
                if self.board_[j][i] != p:
                    win_g = False
            if win_v or win_g:
                return True
        if win_d or win_d_r:
            return True
        return False

    def find_available_points(self):
        avaliable_points = []
        for i in range(self.n_):
            for j in range(self.n_):
                if self.board_[i][j] == " ":
                    avaliable_points.append([i, j])
        return avaliable_points

    def available_points(self):
        return self.find_available_points() != []

    def score(self, depth):
        if self.check("X"):
            return depth - 10
        elif self.check("0"):
            return 10 - depth
        return 0

    def game_over(self):
        if self.check("X") or self.check("0") or (not self.available_points()):
            return True
        return False

    def minimax(self, depth, ismax):
        if depth >= 5:
            return self.score(depth)
        if self.game_over():
            return self.score(depth)

        if ismax:
            result = -1000000
            for points in self.find_available_points():
                self.board_[points[0]][points[1]] = "0"
                result = max(result, self.minimax(depth + 1, not ismax))
                self.board_[points[0]][points[1]] = " "
            return result
        else:
            result = 1000000
            for points in self.find_available_points():
                self.board_[points[0]][points[1]] = "X"
                result = min(result, self.minimax(depth + 1, not ismax))
                self.board_[points[0]][points[1]] = " "
            return result

    def find_move(self):
        c = -1000000
        m = []
        for points in self.find_available_points():
            self.board_[points[0]][points[1]] = "0"
            res = self.minimax(0, False)
            self.board_[points[0]][points[1]] = " "
            if res > c:
                c = res
                m = points
        return m

def main():
    pl = "X"
    n = int(input('n: '))
    game = KrestikiNoliki(n)
    while True:
        while True:
            if pl == "X":
                xx, yy = map(int, input('x y:').split())
                if game.make_move(xx, yy, pl):
                    break
            else:
                f = game.find_move()
                game.make_move(f[0] + 1, f[1] + 1, pl)
                break

        if pl == "X":
            pl = "0"
        else:
            pl = "X"

        if game.check("X"):
            print('Game over. X win')
            break
        if game.check("0"):
            print('Game over. 0 win')
            break
        if game.game_over():
            print('Draw.')
            break

if __name__ == "__main__":
    main()