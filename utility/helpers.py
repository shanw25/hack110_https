class todo:
    id: int
    title: str
    description: str
    time: str
    location: str
    number: int
    tag: str
    # study, exercise, food, travel, chat, date, gaming
    host: str # TODO: User()
    participants: list[str] # TODO: list[User]
    

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