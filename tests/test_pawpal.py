import pytest
from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_status():
    task = Task("Feed", "08:00")
    task.mark_complete()
    assert task.is_complete is True

def test_pet_addition():
    owner = Owner("Test")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)
    assert len(owner.pets) == 1

def test_sorting():
    t1 = Task("A", "10:00")
    t2 = Task("B", "08:00")
    tasks = [{"pet": "P", "task": t1}, {"pet": "P", "task": t2}]
    sorted_tasks = Scheduler.sort_tasks(tasks)
    assert sorted_tasks[0]['task'].time == "08:00"