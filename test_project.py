import pytest
from project import check_users_guess, compare_words, compare_words_emoji


def test_check_users_guess():
    assert check_users_guess("lemon") == "lemon"
    assert check_users_guess("claim") == "claim"


def test_compare_words():
    letters = [[{"   ": "default"} for i in range(5)] for j in range(6)]
    assert compare_words("chain", "drink", letters, 0) == [[{' d ': 'unable'}, {' r ': 'unable'}, {' i ': 'wrong'}, {' n ': 'wrong'}, {' k ': 'unable'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}]]
    assert compare_words("dream", "drama", letters, 0) == [[{' d ': 'correct'}, {' r ': 'correct'}, {' a ': 'wrong'}, {' m ': 'wrong'}, {' a ': 'wrong'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}], [{'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}, {'   ': 'default'}]]


def test_compare_words_emoji():
    emoji = [["⬜", "⬜", "⬜", "⬜", "⬜"] for _ in range(6)]
    assert compare_words_emoji("theme", "taste", emoji, 0) == [['🟩', '⬜', '⬜', '⬜', '🟩'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜']]
    assert compare_words_emoji("voice", "issue", emoji, 0) == [['🟨', '⬜', '⬜', '⬜', '🟩'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜', '⬜', '⬜']]
