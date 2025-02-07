
import context
import task1


def test_print_hello_world(capfd):
  # capfd is a fixture from pytest that allows us to get information from the
  #   stdout and stderr

  task1.hello_world()  # Should write to stdout
  out, err = capfd.readouterr()  # get output from stdout
  # The output from print() is naturally terminated with a newline character.
  # We can strip that off.
  assert out.strip() == 'Hello, World!'
