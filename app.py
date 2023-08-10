import csv
import json

from Note import Note


class Application:
    """Класс модуля приложения"""

    noteList = []

    def create_note(self):
        title = input('Введите заголовок заметки:\n')
        body = input('Введите текст заметки:\n')
        note = Note(title, body)
        self.noteList.append(note)
        return self.noteList

    # методы редактирования и удаления работают не корректно, найди причину
    def redact_note(self):
        i = input("Укажите id заметки, которую хотите редактировать:\n")
        for note in self.noteList:
            if note.get_noteId() == i:
                choice = input("Укажите что хотите изменить:\n"
                               "1.Заголовок\n"
                               "2.Текст заметки\n")
                match choice:
                    case "1":
                        note.set_title(input("Введите новый заголовок\n"))
                    case "2":
                        note.set_body(input("Введите новый текст заметки\n"))
                    case _:
                        print("Попробуйте еще раз!")

    # возможно стоит делать не список а словарь, где id ,будет ключом, а остальное значением
    def delete_note(self):
        for note in self.noteList:
            print(note)
        id = input("Укажите id заметки, которую хотите удалить:\n")
        for note in self.noteList:
            if note.get_noteId() == id:
                self.noteList.pop()

    def show_noteList(self):
        for note in self.noteList:
            print(note.to_string())


    def read_file(self):
        newNoteList = list()
        file_name = input("Введите имя файла\n")
        choice = input("Выберите расширение файла:\n"
                       "1. JSON\n"
                       "2. CSV\n")
        match choice:
            case "1":
                with open (f'{file_name}.json', 'r', encoding="utf-8") as file_r:
                    for line in file_r:
                        newNoteList.append(line)
                for note in newNoteList:
                    newNote = Note("","")
                    splitedString = note.split(';')
                    for string in splitedString:
                        if string.startswith("id"):
                            newNote.set_id(string.strip("id: "))
                        if string.startswith("title"):
                            newNote.set_title(string[5:len(string)])
                        if string.startswith("body"):
                            newNote.set_body(string[4:len(string)])
                        if string.startswith("last update"):
                            newNote.set_updateTime(string.strip("last update: "))
                    self.noteList.append(newNote)
            case "2":
                with open(f'{file_name}.csv', 'r', encoding="utf-8") as file_r:
                    file_reader = csv.reader(file_r, delimiter=";")
                    for row in file_reader:
                        newNote = Note("", "")
                        newNote.set_id(row[0])
                        newNote.set_title(row[1])
                        newNote.set_body(row[2])
                        newNote.set_updateTime(row[3])
                        self.noteList.append(newNote)







    def save_csv(self):
        file_name = input('Введите название файла\n')
        with open(f'{file_name}.csv', 'w', encoding="utf-8", newline="") as file_w:
            fieldnames = ["id", "title", "body", "last update"]
            writer = csv.DictWriter(file_w, delimiter=";", fieldnames=fieldnames)
            writer.writeheader()
            for note in self.noteList:
                writer.writerow({"id" : note.get_noteId(), "title" : note.get_title(), "body" : note.get_body(),
                                 "last update" : note.get_updateTime()})
            print(f"{file_name}.csv file saved\n")

    def save_json(self):
        file_name = input('Введите название файла\n')
        with open(f'{file_name}.json', 'w', encoding="utf-8", newline="") as file_w:
            for note in self.noteList:
                file_w.write(json.dumps(note.to_string()))
            print(f"{file_name}.json file saved\n")
