'''
This page consists the python implementaion for 
playing  the game.
'''

#!/usr/bin/python
from tictactoe import TicTacToe

class InvalidMoveError(Exception):
    """Exception Raised when a invalid move is made by a player.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Game:
    '''Class for playing the game
    '''
    def __init__(self):
        self.game_status = ''
    
    def create_player(self, player_id):
        '''Creates and returns a dictionary to store the data of a player.
        '''
        player = {}
        player['Id'] = player_id
        player['Name'] = input(f'Player {player_id} -> Please Enter your name: ')
        player['marker'] = input(f'Player {player_id} -> Please Enter your marker: ')
        player['choices'] = set()
        return player
    
    def record_player_move(self, player):
        '''Records player moves and checks if he wins with move.
        '''
        try:
            # Step1:  Record players move
            player_id = player['Id']
            move = int(input(f'Player {player_id} -> Please choose a valid position: '))

            # Step2: Check if entered move is valid
            if move not in self.available_choices:
                raise InvalidMoveError('The Entered move is invalid.')

            # Step3: Add the move to players data
            row,col = self.game_positions[move]
            player['choices'].add((row, col))
            
            # Step4: Remove the value from available choices.
            self.available_choices.remove(move)
        except InvalidMoveError as e:
            print(e.message)
            self.record_player_move(player)
        return player
        
    
    def play_game(self):
        '''Main function to play the game.
        '''
        self.game_status = 'In-Progress'
        game = TicTacToe()
        player1 = self.create_player(player_id=1)
        player2 = self.create_player(player_id=2)
        
        self.game_positions = game.generate_all_positions()
        self.available_choices = list(self.game_positions.keys())
        
        round_count = 0
        while len(self.available_choices) > 1:
            round_count+=1
            print('\n')
            print(f'Round {round_count}:')
            print('---------')
            
            player1 = self.record_player_move(player1)
            player2 = self.record_player_move(player2)
                        
            for player in [player1, player2]:
                if game.check_player_game_status(player):
                    player_name = player['Name']
                    self.game_status = f'Player {player_name} has Won'
                    break

            if self.game_status != 'In-Progress':
                game.display_current_positions(player1, player2)
                print('Game status:', self.game_status)
                return 
            if self.game_status == 'In-Progress' and len(self.available_choices) >=3:
                game.display_current_positions(player1, player2)
                print('Game status:', self.game_status)
        
        game.display_current_positions(player1, player2)
        self.game_status = 'Draw'
        print('Game status:', self.game_status)
        return

if __name__ == '__main__':
    game = Game()
    game.play_game()