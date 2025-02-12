
import io


# Very simple and naive word counter.
# Open a file, split by whitespace, then count what's left.
def count_words(file):
  # open the file with utf-8 encoding to handle special characters
  with io.open(file, encoding="utf-8") as file:
    return len(file.read().split())
    
    
if __name__ == '__main__':
  file_path = 'rsc/task6_read_me.txt'
  print(f"There are {count_words(file_path)} words in the file [{file_path}].")
