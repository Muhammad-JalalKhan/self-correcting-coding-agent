import subprocess
import sys

try:
    import numpy as np
    print("NumPy is already installed.")
except ImportError:
    print("NumPy is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("3x3 Matrix created:")
print(matrix)