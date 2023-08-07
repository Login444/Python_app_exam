# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.
from Note import Note

note1 = Note("Title", "Body")


print(note1.get_title())
print(note1.get_body())
print(note1.get_noteId())
print(note1.get_updateTime())



note1.set_title()
note1.set_body()
note1.set_updateTime()

print(note1.get_title())
print(note1.get_body())
print(note1.get_noteId())
print(note1.get_updateTime())

note2 = Note("Title2", "Body2")

print(note2.get_title())
print(note2.get_noteId())
print(note2.get_updateTime())
