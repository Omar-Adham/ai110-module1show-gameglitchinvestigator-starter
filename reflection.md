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

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
