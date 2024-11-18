# Distance to aruco markers 

---

### generate_aruco.py

Скрипт для генерации маркеров

Маркеры сохраняются в папку markers

---

### distance_to_aruco.py

Скрипт открывает камеру и определяет положения маркеров относительно камеры

Скрипт берет откалиброванные данные камеры из MultiMatrix.npz

Расстояния указаны в сантиметрах

В переменную MARKER_SIZE указать размер определяемого маркера в сантиметрах

Нажатие "q" завершает скрипт

---

###  calibration_chessboard.jpg

Шахматная доска для калибровки камеры

---

### capture_calibration_images.py

Скрипт для захвата изображений шахматной доски для последующей калибровки 

Открывает два окна камеры, одно из них распознает шахматную доску 

Нажатие "s" сохраняет изображения если распознана доска

Нажатие "q" завершает скрипт

Все изображения сохраняются в папку calibration_images

Лучше делать от 20 до 50 фотографий

---

### calibration_script.py

Скрипт для калибровки камеры по сделанным изображениям

Создает MultiMatrix.npz

---

### MultiMatrix.npz

Сжатый архив данных калибровки камеры

---

### read_MultiMatrix.py

Скрипт для просмотра данных MultiMatrix.npz






