# Для получения видеопотока с камеры можно использовать библиотеку OpenCV. Вот пример кода на Python, который будет
# складывать по папочка потоки видео с камеры и сохранять их в отдельные папки по 1 минуте видео в каждой:


import cv2
import os
import time

# Определить номер камеры (0 для встроенной камеры на ноутбуке)
camera_number = 0

# Определить папку для сохранения файлов
output_folder = 'output_online'

# Создать папку, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Создать объект VideoCapture
cap = cv2.VideoCapture(camera_number)

# Получить частоту кадров
fps = cap.get(cv2.CAP_PROP_FPS)

# Определить продолжительность каждой папки (в секундах)
folder_duration = 60  # 1 минута

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
    if not ret:
        break

    # Остановить цикл, если продолжительность записи достигла заданного значения
    if current_time >= 3600:  # 1 час
        break

# Освободить ресурсы
cap.release()
cv2.destroyAllWindows()

# Код получает видеопоток с камеры, определяет продолжительность каждой папки и количество кадров в каждой папке,
# затем сохраняет кадры в соответствующие папки.
# В каждой папке сохраняются файлы с именами вида "folder1_20220422-135025.avi", где "folder1" - номер папки,
# а "20220422-135025" - текущее время. Обратите внимание, что код останавливается после 1 час
