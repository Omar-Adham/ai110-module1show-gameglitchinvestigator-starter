# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Bug 1: The secret number kept changing

Expected: The secret number should stay the same while the player keeps guessing until they either win or run out of attempts.

Actual: Every time I clicked Submit, the app reran and a new secret number was generated. This made it almost impossible to win because the answer kept changing.

Bug 2: The higher/lower hints were wrong

Expected: If my guess was smaller than the secret number, the game should say “Higher”, and if it was bigger it should say “Lower.”

Actual: Sometimes the hint given was incorrect, which made the game confusing and misleading.

Bug 3: The game didn’t properly handle invalid input

Expected: The game should only accept valid numbers from the player.

Actual: Some invalid inputs (like decimals or unexpected values) could cause issues or behave strangely.

---

## 2. How did you use AI as a teammate?

One correct suggestion the AI gave me was to move the core game logic out of app.py and into logic_utils.py. It suggested separating functions like parse_guess() and check_guess() from the Streamlit UI so the code would be easier to test and debug. This suggestion was correct because it made the project cleaner and helped me write a pytest test for the logic directly. I verified it by running the game and confirming that the app still worked after importing the functions from logic_utils.py.

One incorrect or misleading suggestion the AI gave me was assuming the bug was mainly about decimal guesses and attempt counting before fully focusing on the original project instructions. That suggestion was not completely wrong, but it was misleading because the main required bug in the assignment was the changing secret number and the incorrect higher/lower hint behavior. I verified what actually mattered by reading the README, checking the reflection instructions, and testing the game directly to see which bugs matched the assignment goals.
---

## 3. Debugging and testing your fixes

I verified my fixes in two ways. First, I tested the game manually by running streamlit run app.py and checking whether the game behaved correctly during play. I made sure the hints now matched the guesses and that the game logic worked normally.

Second, I added an automated pytest test in test/test_game_logic.py to verify the guess-checking logic. For example, I tested that a guess of 60 against a secret number of 50 returns "lower". After that, I ran python -m pytest and confirmed that the test passed. This helped me verify that the fix worked both in the code and in the live game.

---

## 4. What did you learn about Streamlit and state?
The secret number kept changing in the original app because Streamlit reruns the entire script every time the user interacts with the interface. Since the secret number was generated directly in the script, it was recreated on every rerun. This caused the game to change the answer every time the player submitted a guess.

Streamlit reruns mean that the whole Python script runs again whenever the user interacts with the app, like pressing a button or entering input. Session state allows the program to store values so they persist between these reruns. I would explain it to a friend as a way for Streamlit to "remember" important variables while the app keeps refreshing.

The change that fixed the problem was storing the secret number inside Streamlit's session state instead of generating it every time the app ran. This allowed the game to keep the same secret number throughout a round until the player won or the game reset.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is writing small tests to verify that functions behave correctly. Using pytest helped me confirm that the game logic worked as expected and made debugging easier.

Next time I work with AI on a coding task, I would verify the suggestions earlier by testing the code and comparing it with the project instructions. This would help me avoid following suggestions that are not directly related to the main problem.

This project changed the way I think about AI-generated code because I realized that AI suggestions should always be reviewed and tested carefully. AI can help with ideas and debugging, but the developer still needs to understand the code and verify that the solution actually solves the problem.
After you paste these
