## Не конечная версия продукта, репозиторий заполняется.

## Концепт

Из-за затратности постоянной отправки видеопотока на анализ и сетевых/вычислительных ограничений в кейсе, предполагаются локальный сервер с камерой, который определяет факт наличия брака и отправляет лишь фрагменты с дефектами на полноценный анализ на сервер, где происходит уже поиск брака на изображении и расчёт его процентной меры, ущерба и пр. 

## Реализовано

1) Легкая модель, определяющая факт наличия брака поиском нехарактерных для груза оттенков в пикселях (RGB). <br>Если таких пикселей достаточно много (>~1%), то фрагмент отмечается обладающим браком, поскольку нормальный груз в среднем достаточно однороден. <br>
(возможно вычислительно более простое решение при однотонном фоне по энтропии/распределению)

2) CV-модель по полноценному анализу фрагментов видеопотока с браком

3) API-сервер Bottle + Sqlite3 (Backend)

4) Фронтенд-сервер

## Структура проекта

[Backend](app.py) - веб-сервер на bottle + sqlite3 + легкая модель (факт брака)

[CV Algorithm](mid/main.py) - CV-модель (полноценный анализ фрагментов потока)

[Frontend](https://github.com/TeamBolognese/Name-LeadersOfDigital-Final/tree/front) - Фронтенд-сервер

[getter.py](getter.py) - Извлечение пикселей из фото

## Инструкции по запуску

Для запуска проекта необходимы:
```
sudo apt install python3.9
sudo apt install python3-pip
pip3 install bottle
pip3 install matplotlib
pip3 install numpy
pip3 install opencv-python
pip3 install sqlite3
pip3 install Pillow
python3 app.py
```

Также проект уже развернут и готов к использованию по адресу:<br> https://final.teambolognese.ru/ (backend) <br> https://accenture-defector.vercel.app/suppliers-overview (frontend)
