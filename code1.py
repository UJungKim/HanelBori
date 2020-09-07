import numpy as np


def test(a):
    assert isinstance(a, np.ndarray)
    m = a.max()
    return 0 if m > 10 else 1


print('Hello World')
print(f'{test(np.array([1, 2, 3])) = }')
