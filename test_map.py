import pytest

#Test for map.py
#Decorator
@pytest.mark.parametrize("coord1, coord2, x, y", [
    ((0, 10), (0, 1), 5, 0.5)])
def test_map(coord1, coord2, x, y):
    import map
    solution = map.calculate(coord1, coord2, x)
    assert y == solution
    
    
