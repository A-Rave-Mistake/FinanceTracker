# ==================================
# Hint to compiler to import modules from current 'GUI' directory
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
# ==================================