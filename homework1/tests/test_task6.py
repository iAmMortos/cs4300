
import os
import io
import context
import task6
import pytest


# metaprogramming function to generate one function per 
def generate_test_function(file_name):
  def test_function():
    file_path = os.path.join(TEST_FILES_DIR, file_name)
    with io.open(file_path, "r", encoding="utf-8") as f:
      content = f.read()
    assert content.strip(), f"File {file_name} should not be empty"
  return test_function


context.reset()
TEST_FILES_DIR = "./rsc/"

# Generate test functions for counting the words of each of the task*.py files.
# Running the pytests will reveal the extra entries in the pytest list.
# But this test function only tests for non-emptyness.
for file_name in os.listdir(TEST_FILES_DIR):
  if file_name.endswith(".txt"):
    test_name = f"test_{file_name.replace(',', '_')}"
    globals()[test_name] = generate_test_function(file_name)

