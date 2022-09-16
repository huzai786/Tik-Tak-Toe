##################################################
############## TIK TAK TOE BOARD #################
##################################################
import random
from typing import Union

# TODO: Handle check winner algorithm


POSITIONS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MOVES = ('x', 'o')
PLAYER = {}

def _check_xo(player, pos1, pos2, pos3):
    x = [pos1, pos2, pos3]
    if len(set(x)) == 1 and x[0] in ['x', 'o']:
        return [i for i in player.keys() if player[i] == pos1][0]
    return None


def checkWinner(board, player: dict) -> Union[None, str]:
    """checks which combination matches and returns the player with respect to the symbols matched"""
    if winner := _check_xo(player, board.get(1), board.get(2), board.get(3)):
        return winner
    if winner := _check_xo(player, board.get(4), board.get(5), board.get(6)):
        return winner
    if winner := _check_xo(player, board.get(7), board.get(8), board.get(9)):
        return winner
    if winner := _check_xo(player, board.get(1), board.get(4), board.get(7)):
        return winner
    if winner := _check_xo(player, board.get(2), board.get(5), board.get(8)):
        return winner
    if winner := _check_xo(player, board.get(3), board.get(6), board.get(9)):
        return winner
    if winner := _check_xo(player, board.get(1), board.get(5), board.get(9)):
        return winner
    if winner := _check_xo(player, board.get(3), board.get(5), board.get(7)):
        return winner

    return winner


def displayBoard(board: dict) -> None:
    board_str = f"""\tBoard         Positions
      {board.get(1)} | {board.get(2)} | {board.get(3)}        1|2|3
    ------------      -------
      {board.get(4)} | {board.get(5)} | {board.get(6)}        4|5|6
    ------------      -------
      {board.get(7)} | {board.get(8)} | {board.get(9)}        7|8|9
    """
    print(board_str)


def userInput():
    print('Select your symbol (x, o)')
    while True:
        x = input('> ')
        if x.lower() not in ['x', 'o']:
            print('Please select from "x" or "o"')
            continue
        return x.lower()


def get_user_move(current_player, moves: list, players: dict) -> int:
    print(f'{current_player}("{players.get(current_player)}"), Enter your move: \nAvailable position: {moves}')
    while True:
        try:
            move = int(input('> '))
            if move not in moves:
                print(f'Enter a valid move, position available: {moves}')
                continue
        except ValueError:
            print(f'plz enter from {moves}')
            continue

        return move


def free_moves(board: dict) -> list:
    available_moves = []
    for i, v in board.items():
        if v == ' ':
            available_moves.append(i)

    return available_moves


def switch_turn(current_player, players: dict) -> str:
    player_keys = list(players.keys())
    switched_turn = [i for i in player_keys if i != current_player][0]

    return switched_turn


def main() -> None:
    print('Welcome to Tic-Tac-Toe!')
    board = {i: ' ' for i in POSITIONS}                                      # INITIAL A EMPTY BOARD
    player_one = userInput()                                                 # ASK PLAYER FOR THEIR SYMBOL
    player_two = [i for i in MOVES if i != player_one][0]

    PLAYER['player1'] = player_one                                           # SAVE PLAYER MARKS
    PLAYER['player2'] = player_two

    print(f'player 1 symbol: {player_one}\nplayer 2 symbol: {player_two}')

    displayBoard(board)                                                      # DISPLAY THE EMPTY BOARD
    winner = None
    players = list(PLAYER.keys())
    turn = random.choice(players)                                            # RANDOMIZE TURNS

    while winner is None:
        available_moves = free_moves(board)                                  # ALL AVAILABLE MOVES
        if not available_moves:
            print('its a tie')
            break
        current_player_move = get_user_move(turn, available_moves, PLAYER)   # GET POSITION OF PLAYERS MOVE
        board[current_player_move] = PLAYER[turn]                            # UPDATE THE BOARD WITH PLAYER MOVE MARKED
        displayBoard(board)                                                  # DISPLAY THE BOARD
        winner = checkWinner(board, PLAYER)                                  # CHECK FOR WINNER
        if winner:
            print(f'{winner} ("{PLAYER[winner]}") won!')
            break
        turn = switch_turn(turn, PLAYER)                                     # SWITCH TURNS


if __name__ == '__main__':
    main()
