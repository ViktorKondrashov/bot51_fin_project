from bot.commands.command_color import ColorCommand
from PIL import Image


def test_color_command_execute():
    cmd = ColorCommand()
    result = cmd.execute("red", 1, 2)
    assert isinstance(result, Image.Image)

def test_color_command_execute_RGB():
    cmd = ColorCommand()
    result = cmd.execute("100 150 200", 1, 2)
    assert isinstance(result, Image.Image)

def test_color_command_execute_hexadecimal():
    cmd = ColorCommand()
    result = cmd.execute("#0000ff", 1, 2)
    assert isinstance(result, Image.Image)

def test_color_command_execute_negative():
    cmd = ColorCommand()
    result = cmd.execute("12345", 1, 2)
    assert result == "Unknown color"
