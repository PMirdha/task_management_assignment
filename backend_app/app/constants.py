from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"
