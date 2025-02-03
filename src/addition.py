# app.py
# This is a test commit
# 3 unit test cases
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(10,2) == 12
