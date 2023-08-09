import csv
import json

from Note import Note


class Application:
    """Класс модуля приложения"""

    noteList = list()

    def create_note(self):
        title = input('Введите заголовок заметки:\n')
        body = input('Введите текст заметки:\n')
        note = Note(title, body)
        self.noteList.append(note)
        return self.noteList

    def redact_note(self):
        for note in self.noteList:
            print(note)
        id = input("Укажите id заметки, которую хотите редактировать:\n")
        for note in self.noteList:
            if note.get_noteId() == id:
                choice = input("Укажите что хотите изменить:\n 1.Заголовок\n 2.Текст заметки\n")
                match choice:
                    case 1:
                        note.set_title()
                    case 2:
                        note.set_body()
                    case _:
                        print("Попробуйте еще раз!")

    def delete_note(self):
        for note in self.noteList:
            print(note)
        id = input("Укажите id заметки, которую хотите удалить:\n")
        for note in self.noteList:
            if note.get_noteId() == id:
                self.noteList.remove(note)

    def save_csv(self):
        file_name = input('Введите название файла\n')
        with open(f'{file_name}.csv', 'w', encoding="utf-8", newline="") as file_w:
            fieldnames = ["id", "title", "body", "last update"]
            writer = csv.DictWriter(file_w, fieldnames=fieldnames)
            for note in self.noteList:
                writer.writeheader()
                writer.writerows(note.to_string())
            print(f"{file_name}.csv file saved\n")

    def save_json(self):
        file_name = input('Введите название файла\n')
        with open(f'{file_name}.json', 'w', encoding="utf-8", newline="") as file_w:
            for note in self.noteList:
                file_w.write(json.dumps(note.to_string()))
            print(f"{file_name}.json file saved\n")
