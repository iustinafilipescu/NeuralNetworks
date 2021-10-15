import numpy as np

from parsare import coeficienti

if __name__ == '__main__':
    A, B = coeficienti()
    print(np.linalg.solve(np.array(A), np.array(B)))