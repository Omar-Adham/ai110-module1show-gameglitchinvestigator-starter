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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

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
