import requests
from PIL import Image
from bot.base import BotCommand, CommandStrategy


class ColorStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Видаляємо команду `/temperature` і пробіли
        if text.startswith('/color'):
            text = text[len('/color'):].strip()

        # Значення за замовчуванням
        user_color = 'black'

        if text:
            parts = text.split()
            if len(parts) >= 3:
                user_color = (int(parts[0]), int(parts[1]), int(parts[2]))
            elif len(parts) >= 1:
                user_color = parts[0]

        try:
            img = Image.new('RGB', (100, 100), user_color)
        except:
            img = "Unknown color"

        return img

class ColorCommand(BotCommand):
    info = "Enter the desired color by name, hexadecimal representation, or in RGB format with three integers in the range 0 to 255"

    def __init__(self):
        self.strategy = ColorStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)

