import pytest
from main import group_similar_audience 
def test_group_similar_audience():
    sample_text = 'GGGHSSHHRRSS'
    response = group_similar_audience(sample_text)
    assert response == [('G', 3), ('H', 1), ('S', 2), ('H', 2), ('R', 2), ('S', 2)]
