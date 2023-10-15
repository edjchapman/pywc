from click.testing import CliRunner

from pywc import cli


def test_hello_default():
    runner = CliRunner()
    result = runner.invoke(cli, ["hello"])
    assert result.exit_code == 0
    assert result.output == "Hello World\n"


def test_hello_with_name_option():
    runner = CliRunner()
    result = runner.invoke(cli, ["hello", "--name", "Alice"])
    assert result.exit_code == 0
    assert result.output == "Hello Alice\n"


def test_hello_with_name_option_short():
    runner = CliRunner()
    result = runner.invoke(cli, ["hello", "-n", "Bob"])
    assert result.exit_code == 0
    assert result.output == "Hello Bob\n"
