import pytest

#Decorator
@pytest.mark.parametrize("HDL_value, expected", [
    (65, "Normal"), 
    (45, "Borderline Low"), 
    (15, "Low")]) 
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected

if __name__ == "__main__":
    print("Testing HDL analysis")
    test_hdl_analysis()
