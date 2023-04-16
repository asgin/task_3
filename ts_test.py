import pytest
from ts_3 import unique
def test_1():
    assert unique('abbbccdf') == 3
def test_2():
    assert unique('clg') == 3
def test_3():
    assert unique(3) == 'TypeError'
if __name__ == '__main__':
    pytest.main()