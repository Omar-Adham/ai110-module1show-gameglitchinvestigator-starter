import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logic_utils import check_guess


def test_guess_too_high():
    secret = 50
    guess = 60
    result = check_guess(secret, guess)
    assert result == "lower"