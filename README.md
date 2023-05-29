# Модель для детектирования позы руки

## Часть 1. Обучение модели.
В качестве датасета для обучения был взят набор данных [FreiHAND](https://lmb.informatik.uni-freiburg.de/resources/datasets/FreihandDataset.en.html)
Обучение происходило с помощью fine-tune-инга модели efficient-net, предобученной на COCO

Результат можно найти в ноутбуке. Зависимости conda-среды в yaml-файле

## Часть 2. Сравнение с mediapipe
В том же ноутбуке есть сравнение с mediapipe по метрике MSE

MSE обученной модели: 3486.441162109375

MSE mediapipe: 0.003327881874557315

## Часть 3. Приложение "Виртуальная доска" для рисования
Для запуска установите mediapipe и open-cv:
`pip install opencv-python mediapipe`
И запустите приложение
`python app.py`

![Демо](demo.gif)