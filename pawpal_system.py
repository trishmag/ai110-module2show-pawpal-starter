from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Task:
    description: str
    time: str
    frequency: str = "Once"
    is_complete: bool = False

    def mark_complete(self):
        self.is_complete = True
        if self.frequency == "Daily":
            return Task(self.description, self.time, self.frequency)
        return None

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

class Scheduler:
    @staticmethod
    def get_all_tasks(owner: Owner):
        all_tasks = []
        for pet in owner.pets:
            for task in pet.tasks:
                all_tasks.append({"pet": pet.name, "task": task})
        return all_tasks

    @staticmethod
    def sort_tasks(task_list: List[dict]):
        return sorted(task_list, key=lambda x: datetime.strptime(x['task'].time, "%H:%M"))

    @staticmethod
    def detect_conflicts(task_list: List[dict]):
        seen_times = {}
        warnings = []
        for item in task_list:
            t = item['task'].time
            if t in seen_times:
                warnings.append(f"Conflict: {item['pet']} and {seen_times[t]} at {t}")
            seen_times[t] = item['pet']
        return warnings