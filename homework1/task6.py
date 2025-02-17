
import io


def count_words(file):
  """
  Very simple and naive word counter.
  Open a file, split by whitespace, then count what's left.
  Will differ from Microsoft Word's word count: Word will count "I'm Bond—James Bond" as 4 words,
    but this script will count it as 3.
  """
  # io.open allows encoding to be set to account for special characters
  with io.open(file, encoding="utf-8") as file:
    return len(file.read().split())
    
    
if __name__ == '__main__':
  file_path = 'rsc/task6_read_me.txt'
  print(f"There are {count_words(file_path)} words in the file [{file_path}].")

