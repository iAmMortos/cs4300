
import sys, os

this_file_dir = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(this_file_dir)

sys.path.insert(0, parent)
os.chdir(parent)

def reset():
  sys.path.insert(0, this_file_dir)
  os.chdir(this_file_dir)
