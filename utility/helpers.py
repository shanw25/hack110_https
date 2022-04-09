class User:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class todo:
    id: int
    title: str
    description: str
    time: str
    location: str
    number: int
    tag: str
    # study, exercise, food, travel, chat, date, gaming
    host: User
    participants: list[User]
    participant_count: int
    

    def __init__(self, id: int, title: str, description: str, time: str, location: str, number: int, tag: str = "#study", host: str = "", participants: list[str] = []):
        self.id = id
        self.title = title
        self.description = description
        self.time = time
        self.location = location
        self.number = number
        self.tag = tag
        self.host = host
        self.participants = participants
        self.participant_count = len(participants)