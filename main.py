from logic import play_game
from decouple import config

if __name__ == "__main__":
    min_number = config('MIN_NUMBER', cast=int)
    max_number = config('MAX_NUMBER', cast=int)
    max_attempts = config('MAX_ATTEMPTS', cast=int)
    initial_capital = config('INITIAL_CAPITAL', cast=int)

    play_game(min_number, max_number, max_attempts, initial_capital)