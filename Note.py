import datetime


class Note:
    """Класс заметок"""
    noteId = 0
    title = ''
    body = ''
    updateTime = 0

    def __init__(self, title, body):
        self.title = title
        self.body = body
        Note.noteId += 1
        self.updateTime = datetime.datetime.now()

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_noteId(self):
        return self.noteId

    def get_updateTime(self):
        return self.updateTime

    def set_title(self):
        self.title = input("Пишите заголовок:\n")
        self.updateTime = datetime.datetime.now()

    def set_body(self):
        self.body = input("Пишите текст заметки:\n")
        self.updateTime = datetime.datetime.now()

    def to_string(self):
        return str(self.noteId) + str(self.title) + str(self.body) + str(self.updateTime)
