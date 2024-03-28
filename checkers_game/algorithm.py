from copy import deepcopy
from board import Board
from constants import WHITE,BLUE
import pygame

BLUE = (255,0,0)
WHITE = (255, 255, 255)

def minimax(board, depth, maximizing, alpha=float("-inf"), beta=float("inf")):
    if depth == 0 or board.winner() is not None:
        return board.evaluate(), None

    all_pieces = board.get_all_pieces(WHITE)
    if not all_pieces:
        return float("-inf") if maximizing else float("inf"), None

    best_move = None
    if maximizing:
        for piece in all_pieces:
            valid_moves = board.get_valid_moves(piece)
            for move,skip in valid_moves.items():
                temp_board = deepcopy(board)
                temp_piece = temp_board.get_piece(piece.row, piece.col)
                new_board = simulate_move(temp_piece, move, temp_board, skip)
                score, _ = minimax(new_board, depth-1, False, alpha, beta)
                if score > alpha:
                    alpha = score
                    best_move = new_board
                if beta <= alpha:
                    break
        return alpha, best_move
    else:
        
        for piece in all_pieces:
            valid_moves = board.get_valid_moves(piece)
            for move,skip in valid_moves.items():
                temp_board = deepcopy(board)
                temp_piece = temp_board.get_piece(piece.row, piece.col)
                new_board = simulate_move(temp_piece, move, temp_board, skip)
                score, _ = minimax(new_board, depth-1, True, alpha, beta)
                if score < beta:
                    beta = score
                    best_move = new_board
                if alpha>=beta:
                    break
        return beta, best_move

def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board