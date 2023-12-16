<a name="readme-top"></a>
<br>
<div align="center">
  <a href="https://github.com/h1lton/url-shortener">
    <img src="https://img.icons8.com/?size=100&id=u9koQ5FSNMjC&format=png" alt="Logo">
  </a>
  <h3>URL Shortener</h3>
  <p>
    Тестовое задание на FastAPI
    <br>
    <a href="https://github.com/h1lton/url-shortener"><strong>Explore the docs »</strong></a>
    <br>
    <br>
  </p>

  <img src="https://skillicons.dev/icons?i=py,fastapi,mysql,docker,githubactions&theme=light" alt="Tech">

  <p>
    <br>
    <a href="https://github.com/h1lton/url-shortener">View Demo</a>
    ·
    <a href="https://github.com/h1lton/url-shortener/issues">Report Bug</a>
    ·
    <a href="https://github.com/h1lton/url-shortener/issues">Request Feature</a>
  </p>
</div>


<details>
  <summary>Оглавление</summary>
  <ol>
    <li><a href="#задание">Задание</a></li>
    <li><a href="#стек-технологий">Стек технологий</a></li>
    <li><a href="#установка">Установка</a></li>
    <li><a href="#тестирование">Тестирование</a></li>
  </ol>
</details>

## Задание

### Тестовое задание на позицию стажера/junior бекенд разработчика в юнит Авто
[Источник](https://github.com/avito-tech/auto-backend-trainee-assignment)

Нужно сделать HTTP сервис для сокращения URL наподобие [Bitly](https://bitly.com/) и других сервисов.

UI не нужен, достаточно сделать JSON API сервис.
Должна быть возможность:
- сохранить короткое представление заданного URL
- перейти по сохраненному ранее короткому представлению и получить redirect на соответствующий исходный URL

#### Требования:

- Язык программирования: Go/Python/PHP/Java/JavaScript
- Предоставить инструкцию по запуску приложения. В идеале (но не обязательно) – использовать контейнеризацию с возможностью запустить проект командой [`docker-compose up`](https://docs.docker.com/compose/)
- Требований к используемым технологиям нет - можно использовать любую БД для персистентности
- Код нужно выложить на github (просьба не делать форк этого репозитория, чтобы не плодить плагиат)

#### Усложнения:

- Написаны тесты (постарайтесь достичь покрытия в 70% и больше)
- Добавлена валидация URL с проверкой корректности ссылки
- Добавлена возможность задавать кастомные ссылки, чтобы пользователь мог сделать их человекочитаемыми - [http://bit.ly/avito-auto-be](http://bit.ly/avito-auto-be)
- Проведено нагрузочное тестирование с целью понять, какую нагрузку на чтение может выдержать наш сервис
- Если вдруг будет желание, можно слепить простой UI и выложить сервис на бесплатный хостинг - Google Cloud, AWS и подобные.

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Стек технологий

- <img src="https://skillicons.dev/icons?i=py&theme=light" alt="icon" style="width: 25px"> Python 3.9
- <img src="https://skillicons.dev/icons?i=fastapi&theme=light" alt="icon" style="width: 25px"> FastAPI
- <img src="https://skillicons.dev/icons?i=mysql&theme=light" alt="icon" style="width: 25px"> MySQL
- <img src="https://skillicons.dev/icons?i=docker&theme=light" alt="icon" style="width: 25px"> Docker & Docker Compose
- <img src="https://skillicons.dev/icons?i=py&theme=light" alt="icon" style="width: 25px"> SQLAlchemy & Alembic
- <img src="https://skillicons.dev/icons?i=py&theme=light" alt="icon" style="width: 25px"> PyTest & HTTPX
- <img src="https://skillicons.dev/icons?i=githubactions&theme=light" alt="icon" style="width: 25px"> GitHub Actions

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Установка

1. Клонируйте репозиторий
   ```sh
   git clone https://github.com/h1lton/url-shortener.git
   cd url-shortener
   ```
2. Создайте файл .env
   ```sh
   cp .env.template .env
   ```
3. Запустите контейнеры
   ```sh
   docker-compose up
   ```
   _примечание: если будите запускать в первый раз, это займёт продолжительный промежуток времени._
4. Когда увидите в консоли что uvicorn запущен, можете открывать [документацию](http://localhost:8000/docs).

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Тестирование

Что бы запустить тесты:

```sh
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit --exit-code-from tests
```

или

```sh
docker-compose up
docker-compose exec app pytest
```

Тесты так же запускаются при пуше в ветку main.

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>