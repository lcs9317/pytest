from app.calculator import Calculator

def test_add_positive():
    calc = Calculator()
    assert calc.add(1,2) == 3
    
def test_add_negative():
    calc = Calculator()
    assert calc.add(-1,-2) == -3
    
def test_add_mixed():
    calc = Calculator()
    assert calc.add(-1,2) == 1