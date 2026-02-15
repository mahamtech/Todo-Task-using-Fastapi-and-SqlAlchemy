from enum import Enum as PyEnum

class TodoStatus(str,PyEnum):
    pending="pending"
    progess="progres"
    completed="completed"

