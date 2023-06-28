import pytest

from main import minion_game_score_counter

def test_minion_game_score_counter():
    sample_text = "KBVKDJVBXKJVVDVDSK"
    response = minion_game_score_counter(sample_text)
    assert response == "Stuart wins with score  of 171"