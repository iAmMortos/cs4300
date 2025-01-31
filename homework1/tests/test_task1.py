
import __init__
import task1


def test_print_hello_world(capfd):
  task1.hello_world()
  out, err = capfd.readouterr()
  assert out.strip() == 'Hello, World!'
