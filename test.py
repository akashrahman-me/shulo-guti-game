import os
import sys

# Redirect stdout and stderr
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

# Your script here
print("This will not be shown in the terminal")
