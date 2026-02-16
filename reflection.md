# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I designed the system using four primary classes: Owner, Pet, Task, and Scheduler. Owner and Pet serve as data containers, maintaining the relationships between users and their animals. Task handles the state of individual activities. Scheduler was designed as a static utility class. I chose this "Service Pattern" so that the scheduling logic (sorting and conflicts) remains independent of the data storage, making the code more modular and easier to test.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

During implementation, I moved the get_all_tasks logic into the Scheduler. Originally, I thought the Owner should return all tasks, but I realized that as the app grows, the Scheduler might need to filter tasks by priority or category across different pets. Centralizing this in the Scheduler prevented "fat classes" and kept the Owner class focused solely on management.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
I used a lambda function within Python’s sorted() method to parse "HH:MM" strings into datetime objects. This ensures chronological accuracy. 
I implemented a dictionary-based lookup. As the system iterates through tasks, it stores times in a hash map. This allows the system to identify duplicates in O(n) time.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

This is highly efficient and prevents simple scheduling errors. However, it does not account for the duration of tasks (e.g., a 15-minute feeding vs. a 60-minute walk). I prioritized a lightweight, bug-free implementation for the MVP over a complex interval-math solution that might introduce UI lag.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

This was essential for debugging the st.session_state disconnect. It helped me identify that the UI was "forgetting" pets because the Owner instance was being recreated on every rerun.

Copilot was used to generate pytest cases for edge cases, such as marking a task complete when no recurrence is set.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

The AI initially suggested using a complex database connector like SQLAlchemy. I rejected this in favor of Streamlit Session State. This kept the project focused on Python OOP principles rather than database administration, keeping the "CLI-first" spirit of the assignment intact.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
 I focused on testing state changes (ensuring mark_complete() toggles the boolean and triggers recurrence) and algorithmic accuracy (verifying that the Scheduler correctly identifies time conflicts and sorts tasks out of order).

These tests were important because they verify the "intelligence" of the app. Without automated tests, a small change in how time strings are handled could break the entire schedule without the user noticing until a pet's meal is missed.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am pretty confident that the scheduler works correctly. 

If given more time, I would test invalid time formats (e.g., "25:00" or "noon") to ensure the system doesn't crash, and duplicate pet names to ensure the Owner class handles unique IDs correctly.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The decoupling of the logic layer from the UIis the partt I am most satisfied with. By building pawpal_system.py as a standalone module, I was able to verify the "brain" of the app through a CLI and unit tests before ever touching Streamlit. This made debugging the UI much faster because I knew the backend was already reliable.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

In the next iteration, I would redesign the Task class to use Python’s datetime.time objects natively rather than strings. While strings are easier for a quick CLI demo, using actual time objects would allow for duration-based conflict detection (e.g., knowing that a 30-minute walk starting at 8:45 AM overlaps with a 9:00 AM feeding).

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

The most important thing I learned is that AI is a powerful "scaffolder," but the human must be the "validator." While Copilot was excellent at generating the boilerplate code for my classes, I had to be the one to ensure the session_state in Streamlit was correctly wired to my OOP logic. Working with AI is most effective when you treat it as a highly skilled intern who needs clear architectural direction.