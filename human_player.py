from six.moves import input

class HumanPlayer:

    def __init__(self, value):
        self.value = value
        # self.games_won = 0

    def get_move(self):
        print("Hello {}, please type your move (row, col)".format(self.value))
        # python 2 - raw_input
        # python 3 - input
        text = input()
        row, column = text.split(', ')

        return (int(row), int(column))