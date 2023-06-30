import pytest
from main import get_max_share_price

def test_get_max_share_price():
    response = get_max_share_price("./company_share_data.csv")
    sample_response = "max share price for year 1990 and month Jan is of company Company A which is: 89"
    assert response == sample_response
    with pytest.raises(FileNotFoundError) as e:
        get_max_share_price("./false_path")
        assert str(e.value) == 'Please check file path'