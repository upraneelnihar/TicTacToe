'''
This script consists the python implementation 
for the tic tac toe game.
'''


class TicTacToe:
    '''API for TicTacToe game.
    '''
    def __init__(self):
        self.display_rules()
        self.reset_game()
    
    def display_rules(self):
        '''Displays all positions indices.
        '''
        print('################################ Welcome to TicTacToe Game ######################################')
        print()
        print('Rules:')
        print('------')
        print('1. The game is played between two players(player 1 and player2) in 3*3 box.')
        print('2. Each player is asked to choose a marker and enter that in a free position one after the other.')
        print('3. The player who manages to place a marker in 3 positions consecutively wins the game.') 
        print('4. The 3 consecutive positions can be any one of the 4 edges or 2 diagonals. ')
        print('  | 0 | 1 | 2 |')
        print('---------------')
        pos = 1
        for row in range(3):
            print(row, end=' |')
            for col in range(3):
                print('', pos, end=' |')
                pos+=1
            print()
        print()
    
    def reset_game(self):
        self.game_positions = self.generate_all_positions()
        self.winning_choices = self.generate_winning_combinations()
    
    def generate_all_positions(self):
        '''Generates a dictionary with key as (row,col) index and
           value as position number shown below.
           1|2|3
           4|5|6
           7|8|9
        '''
        positions = {}
        pos = 1
        for row in range(3):
            for col in range(3):
                positions[pos] = (row, col)
                pos+=1
        return positions
    
    def generate_winning_combinations(self):
        '''Generates all winning choices as per rules of tic tac toe.
           and returns a list.
        '''
        winning_choices = []

        for row in range(3):
            win_set = set()
            for col in range(3):
                win_set.add((row,col))
            winning_choices.append(win_set)

        for col in range(3):
            win_set = set()
            for row in range(3):
                win_set.add((row,col))
            winning_choices.append(win_set)

        winning_choices.append(set([(0,0), (1,1), (2,2)]))
        winning_choices.append(set([(0,2), (1,1), (2,0)]))
        return winning_choices
        
    def check_player_game_status(self, player):
        '''Checks if the player has won or not based on the winning choices.
        '''
        for win_set in self.winning_choices:
            if win_set.issubset(player['choices']):
                return True
        return False

    def display_current_positions(self, player1, player2):
        '''Returns None.  Prints the current Positions'''
        print('  | 0 | 1 | 2 |')
        print('---------------')
        for row in range(3):
            print(row, end=' |')
            for col in range(3):
                if (row, col) in player1['choices']:
                    print('', player1['marker'], end=' |')
                elif (row, col) in player2['choices']:
                    print('', player2['marker'], end=' |')
                else:
                    print('   ', end='|')
            print()