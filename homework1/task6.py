
import io


def count_words(file):
  with io.open(file, encoding="utf-8") as file:
    return len(file.read().split())
  

if __name__ == '__main__':
  main()
