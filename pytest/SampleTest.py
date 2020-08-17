import _pytest

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    print(func(3) == 5)