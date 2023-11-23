import pytest
from gameLogic import GameLogic


def test_initialise_board():
    game = GameLogic()
    assert game._board == [[0] * 4 for _ in range(4)]
    assert game._score == 0
    assert game._won is False
    assert game._over is False


def test_move_left1():
    game = GameLogic()
    game.set_board([
        [2, 0, 0, 0],
        [2, 2, 0, 0],
        [2, 0, 0, 0],
        [2, 2, 0, 0]
    ])
    game.only_move_left()
    assert game._board == [
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0]
    ]
    assert game._score == 4
    assert game._won is False
    assert game._over is False


def test_move_left():
    game = GameLogic()
    game.set_board([
        [4, 4, 2, 2],
        [2, 2, 0, 2],
        [0, 2, 4, 4],
        [512, 128, 128, 32]
    ])
    game.only_move_left()
    assert game._board == [
        [8, 4, 0, 0],
        [4, 2, 0, 0],
        [2, 8, 0, 0],
        [512, 256, 32, 0]
    ]
    assert game._score == 128 + 4 + 4 + 2 + 2
    assert game._won is False
    assert game._over is False


def test_move_left3():
    game = GameLogic()
    game.set_board([
        [4, 0, 0, 2],
        [2, 2, 0, 2],
        [0, 2, 4, 4],
        [128, 128, 128, 32]
    ])
    game.only_move_left()
    assert game._board == [
        [4, 2, 0, 0],
        [4, 2, 0, 0],
        [2, 8, 0, 0],
        [256, 128, 32, 0]
    ]
    assert game._score == 128 + 4 + 2
    assert game._won is False
    assert game._over is False


def test_move_left4():
    game = GameLogic()
    game.set_board([
        [4, 0, 2, 0],
        [8, 4, 2, 0],
        [0, 2, 4, 16],
        [128, 256, 512, 1024]
    ])
    game.only_move_left()
    assert game._board == [
        [4, 2, 0, 0],
        [8, 4, 2, 0],
        [2, 4, 16, 0],
        [128, 256, 512, 1024]
    ]
    assert game._score == 0
    assert game._won is False
    assert game._over is False


def test_move_right():
    game = GameLogic()
    game.set_board([
        [4, 4, 2, 2],
        [2, 2, 0, 2],
        [0, 2, 4, 4],
        [512, 128, 128, 32]
    ])
    game.only_move_right()
    assert game._board == [
        [0, 0, 8, 4],
        [0, 0, 2, 4],
        [0, 0, 2, 8],
        [0, 512, 256, 32]
    ]
    assert game._score == 128 + 4 + 4 + 2 + 2
    assert game._won is False
    assert game._over is False


def test_move_right1():
    game = GameLogic()
    game.set_board([
        [4, 0, 0, 2],
        [2, 2, 0, 2],
        [0, 2, 4, 4],
        [128, 128, 128, 32]
    ])
    game.only_move_right()
    assert game._board == [
        [0, 0, 4, 2],
        [0, 0, 2, 4],
        [0, 0, 2, 8],
        [0, 128, 256, 32]
    ]
    assert game._score == 128 + 4 + 2
    assert game._won is False
    assert game._over is False


def test_move_up():
    game = GameLogic()
    game.set_board([
        [4, 4, 2, 2],
        [2, 2, 0, 2],
        [0, 2, 4, 4],
        [512, 128, 128, 32]
    ])
    game.only_move_up()
    assert game._board == [
        [4, 4, 2, 4],
        [2, 4, 4, 4],
        [512, 128, 128, 32],
        [0, 0, 0, 0]
    ]
    assert game._score == 4
    assert game._won is False
    assert game._over is False


def test_move_up1():
    game = GameLogic()
    game.set_board([
        [4, 0, 0, 2],
        [4, 2, 0, 2],
        [128, 2, 4, 2],
        [128, 128, 4, 2]
    ])
    game.only_move_up()
    assert game._board == [
        [8, 4, 8, 4],
        [256, 128, 0, 4],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert game._score == 128 + 4 + 2 + 4 + 2 + 2
    assert game._won is False
    assert game._over is False


def move_down():
    game = GameLogic()
    game.set_board([
        [4, 4, 2, 2],
        [2, 2, 0, 2],
        [0, 2, 4, 4],
        [2, 2, 4, 8]
    ])
    game.only_move_down()
    assert game._board == [
        [0, 0, 0, 0],
        [0, 4, 0, 4],
        [4, 2, 2, 4],
        [4, 4, 8, 8]
    ]
    assert game._score == 4
    assert game._won is False
    assert game._over is False
