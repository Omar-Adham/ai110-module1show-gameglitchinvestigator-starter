def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 50
    elif difficulty == "Medium":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 200


def parse_guess(raw: str):
    raw = raw.strip()

    if raw == "":
        return None

    try:
        # only accept whole numbers
        if "." in raw:
            return None

        return int(raw)
    except ValueError:
        return None


def check_guess(secret: int, guess: int):
    if guess < secret:
        return "higher"
    elif guess > secret:
        return "lower"
    else:
        return "correct"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "correct":
        return current_score + max(0, 10 - attempt_number)
    else:
        return current_score