
import io


def count_words(file):
  # open the file with utf-8 encoding to handle special characters
  with io.open(file, encoding="utf-8") as file:
    return len(file.read().split())
    
    
def generate_test_function_names():
  pass
  

if __name__ == '__main__':
  print(f"There are {count_words('rsc/task6_read_me.txt')} words in the file.")

'''
Here are three short text files with engaging anecdotes or factoids.

File 1: Moon Museum.txt

In 1969, during the Apollo 12 mission, a tiny piece of art was secretly smuggled onto the Moon. Known as the Moon Museum, it was a small ceramic wafer featuring miniature sketches from six prominent artists, including Andy Warhol and Robert Rauschenberg. The artwork was covertly attached to the lunar lander’s leg by a NASA engineer without official approval. If true, it means the first art gallery on the Moon was an unsanctioned act of creative rebellion—one that still sits on the lunar surface today.

File 2: The Great Emu War.txt

In 1932, Australia found itself at war with... emus. After World War I, struggling farmers in Western Australia were overrun by tens of thousands of the flightless birds, which ravaged crops. The government responded by deploying soldiers armed with machine guns. The emus, however, proved unexpectedly resilient—outrunning vehicles, scattering under fire, and absorbing bullets like feathery tanks. After weeks of fruitless battle, the humans admitted defeat. The emus had won. To this day, the Great Emu War remains one of history’s most bizarre military failures.

File 3: The Monty Hall Paradox.txt

Imagine you’re on a game show. There are three doors: behind one is a car, behind the other two, goats. You pick a door. The host, knowing what’s behind them, opens another door to reveal a goat. Now, he asks if you’d like to switch. Should you?

Mathematically, yes! If you stay, your odds remain 1/3. If you switch, they rise to 2/3. Why? Because your initial pick had a low chance of being right, and the host’s action effectively transfers that probability to the remaining door. It’s counterintuitive, but true—switching gives you the best shot at the prize.

Would you like any adjustments or different topics?
'''
