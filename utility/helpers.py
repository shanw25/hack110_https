class todo:
    id: int
    title: str
    description: str
    time: str
    location: str
    number: int

    def __init__(self, id: int, title: str, description: str, time: str, location: str, number: int):
        self.id = id
        self.title = title
        self.description = description
        self.time = time
        self.location = location
        self.number = number