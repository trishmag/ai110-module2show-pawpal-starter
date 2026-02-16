🐾 PawPal+
Smart Pet Care Management System

PawPal+ is a modular pet care application designed to help owners maintain their pets' health and happiness. By combining Python’s Object-Oriented Programming (OOP) with a "CLI-first" development workflow, the system manages daily routines—feedings, walks, and medications—using smart scheduling logic.

🚀 Features
Modular OOP Design: Logic is separated into Owner, Pet, Task, and Scheduler classes for high maintainability.

Smart Scheduling: Automatically sorts tasks chronologically using 24-hour time logic.

Conflict Detection: Flags overlapping tasks at the same time across multiple pets to prevent scheduling errors.

Daily Recurrence: Automatically generates a new task instance when a "Daily" task is marked as complete.

Session-Managed UI: Built with Streamlit, utilizing session_state to persist pet and task data across browser refreshes.

🛠️ System Architecture
The system follows a modular architecture where the Scheduler acts as the operational brain, processing data stored within the Owner and Pet objects.

Code snippet
classDiagram
    Owner "1" o-- "many" Pet : manages
    Pet "1" o-- "many" Task : has
    Scheduler ..> Owner : processes
    class Owner { +name, +pets, +add_pet() }
    class Pet { +name, +species, +tasks, +add_task() }
    class Task { +description, +time, +frequency, +is_complete, +mark_complete() }
    class Scheduler { +sort_tasks(), +detect_conflicts(), +get_all_tasks() }
📦 Installation & Setup
Clone the Repository:

Bash
git clone <your-repo-link>
cd ai110-module2-pawpal
Install Dependencies:

Bash
pip install streamlit pytest
Run the Application:

Bash
streamlit run app.py
🧪 Testing
The backend logic is verified through an automated pytest suite. To run the tests and confirm system integrity:

Bash
python -m pytest
💡 Engineering Reflection
Tradeoffs: The conflict detection algorithm currently uses exact-time matching. While high-performance, it does not yet account for task durations (e.g., a 30-minute walk). This was a deliberate choice for the MVP to prioritize system stability.

AI Collaboration: GitHub Copilot was utilized to scaffold class skeletons and generate test cases for edge cases, such as empty task lists and recurring task generation logic.