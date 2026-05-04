# Weather CLI

Консольное приложение для получения текущей погоды в Москве через REST API (Open-Meteo).

## Что реализовано
* Консольный клиент на Python для получения погодных данных.
* Настроен CI пайплайн через GitHub Actions для автоматической сборки.
* Проект упакован в Docker-образ и опубликован в Docker Hub.

## Инструкция по закпуску проекта
Локально (без Docker):
1. `pip install -r requirements.txt`
2. `python main.py`

Через Docker (у кого он установлен):
`docker run твой_логин/weather-cli:latest`

## Как проверять результат
1. При локальном запуске в консоль выводится текущая температура и скорость ветра в Москве.
2. Ссылка на выполненный job сборки в GitHub Actions: https://github.com/LexaKurilovi4/TpWeatherCli/actions
3. Ссылка на образ в Docker Hub: https://hub.docker.com/repository/docker/lexakurilovi4/weather-cli