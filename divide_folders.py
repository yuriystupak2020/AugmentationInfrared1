# Для выполнения этой задачи вам потребуется использовать библиотеку OpenCV, которая позволяет работать
# с видеопотоками. Также для создания папок и сохранения видеофайлов можно использовать библиотеку os.

# Вот пример кода на Python, который разбивает входной видеопоток на 1-минутные фрагменты и сохраняет их в
# отдельные папки:


import cv2
import os
import time

# Определить имя файла для чтения
file_name = 'input_video.mp4'

# Определить папку для сохранения файлов
output_folder = 'output'

# Создать папку, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Создать объект VideoCapture
cap = cv2.VideoCapture(file_name)

# Получить частоту кадров и количество кадров
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Определить продолжительность каждой папки (в секундах)
folder_duration = 60  #  1 минута

# Определить количество кадров в каждой папке
frames_per_folder = int(folder_duration * fps)

# Инициализировать переменные для отслеживания текущего времени и номера папки
current_time = 0
folder_num = 1

# Читать кадры и сохранять их в папки
while cap.isOpened():
    # Определить имя файла для записи
    file_prefix = 'folder{}_'.format(folder_num)
    file_name = os.path.join(output_folder, file_prefix + time.strftime("%Y%m%d-%H%M%S") + '.avi')

    # Создать объект VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(file_name, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

    # Считать кадры и записать их в папку
    for i in range(frames_per_folder):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

    # Закрыть объект VideoWriter
    out.release()

    # Обновить текущее время и номер папки
    current_time += folder_duration
    folder_num += 1

    # Остановить цикл, если конец видеопотока
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == total_frames:
        break

# Освободить ресурсы
cap.release()
cv2.destroyAllWindows()












# Код читает входной видеопоток, определяет продолжительность каждой папки и количество кадров в каждой папке,
# затем сохраняет кадры в соответствующие папки. В каждой папке сохраняются файлы
# с именами вида "folder1_20220422-135025.avi", где "folder1" - номер папки,
# а "20220422-135025" - текущее время. Обратите внимание, что код