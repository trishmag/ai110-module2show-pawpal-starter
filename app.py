import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# Initialize the "Vault" (Session State)
if 'owner' not in st.session_state:
    st.session_state.owner = Owner(name="User")

owner = st.session_state.owner

st.title("🐾 PawPal+ Dashboard")

# --- SIDEBAR: ADDING PETS ---
with st.sidebar:
    st.header("Add a Pet")
    pet_name = st.text_input("Pet Name")
    pet_type = st.selectbox("Type", ["Dog", "Cat", "Other"])
    
    if st.button("Register Pet"):
        if pet_name:
            new_pet = Pet(pet_name, pet_type)
            owner.add_pet(new_pet)
            st.success(f"Added {pet_name}!")
            st.rerun()
        else:
            st.error("Please enter a name.")

# --- MAIN UI: ADDING TASKS ---
if owner.pets:
    with st.expander("📅 Schedule a New Task"):
        target_pet_name = st.selectbox("Select Pet", [p.name for p in owner.pets])
        task_desc = st.text_input("Task Description (e.g., Feeding)")
        task_time = st.text_input("Time (HH:MM, e.g., 08:30)")
        
        if st.button("Add Task"):
            target_pet = next(p for p in owner.pets if p.name == target_pet_name)
            target_pet.add_task(Task(task_desc, task_time))
            st.rerun()

# --- DISPLAY: TODAY'S SCHEDULE ---
st.header("Today's Schedule")
all_tasks = Scheduler.get_all_tasks(owner)
sorted_tasks = Scheduler.sort_tasks(all_tasks)
conflicts = Scheduler.detect_conflicts(sorted_tasks)

for warning in conflicts:
    st.warning(warning)

if not sorted_tasks:
    st.info("No tasks yet. Use the sidebar to add a pet and the expander to schedule tasks.")
else:
    for item in sorted_tasks:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.write(f"**{item['task'].time}**")
        with col2:
            status = "✅" if item['task'].is_complete else "⏳"
            st.write(f"{status} {item['pet']}: {item['task'].description}")
        with col3:
            if not item['task'].is_complete:
                if st.button("Done", key=f"{item['pet']}_{item['task'].time}_{item['task'].description}"):
                    item['task'].mark_complete()
                    st.rerun()
                    