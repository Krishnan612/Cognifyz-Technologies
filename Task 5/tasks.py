from dataclasses import dataclass
from typing import List, Optional
@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
class TaskManager:
    """Simple in-memory task manager with essential CRUD operations."""

    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self._next_id: int = 1
    def create_task(self, title: str, description: str = "") -> Task:
        title = (title or "").strip()
        if not title:
            raise ValueError("Title cannot be empty")
        task = Task(id=self._next_id, title=title, description=(description or "").strip())
        self.tasks.append(task)
        self._next_id += 1
        return task
    def list_tasks(self) -> List[Task]:
        return self.tasks.copy()
    def get_task(self, task_id: int) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> Task:
        task = self.get_task(task_id)
        if task is None:
            raise KeyError("Task not found")
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Title cannot be empty")
            task.title = title
        if description is not None:
            task.description = description.strip()
        if completed is not None:
            task.completed = bool(completed)
        return task
    def delete_task(self, task_id: int) -> Task:
        task = self.get_task(task_id)
        if task is None:
            raise KeyError("Task not found")
        self.tasks.remove(task)
        return task