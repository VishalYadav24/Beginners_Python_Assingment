import pytest
from main import find_probability

def test_find_probability():
    list_of_alphabets = ["a","b","a","g"]
    indices =2
    response = find_probability(list_of_alphabets,indices)
    assert response == 'probability of finding "a" in  6 combinations is : 0.833'
