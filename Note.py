import datetime
from itertools import count


class Note:
    """Класс заметок"""
    noteIdCounter = count(1)
    noteId = 0
    title = ''
    body = ''
    updateTime = 0

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.noteId = next(self.noteIdCounter)
        self.updateTime = datetime.datetime.now()

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_noteId(self):
        return self.noteId

    def get_updateTime(self):
        return self.updateTime

    def set_id(self, id):
        self.noteId = id

    def set_updateTime(self, updateTime):
        self.updateTime = updateTime

    def set_title(self, title):
        self.title = title
        self.updateTime = datetime.datetime.now()

    def set_body(self, body):
        self.body = body
        self.updateTime = datetime.datetime.now()

    def to_string(self):
        return ("id: " + str(self.noteId) + "; title: " + str(self.title) + "; body:" + str(self.body)
                + "; last update: " + str(self.updateTime) + ";")
