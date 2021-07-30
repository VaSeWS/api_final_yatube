#Yatube API
API для социальной сети YaTube
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VaSeWS/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 yatube_api/manage.py migrate
```

Запустить проект:

```
python3 yatube_api/manage.py runserver
```
###Примеры запросов:
1. `GET: api/v1/posts/`
Ответ:
```json
[
	{
		"id": 0,
		"author": "string",
		"text": "string",
		"pub_date": "2019-08-24T14:15:22Z",
		"image": "string",
		"group": 0
	}
]
```

2. `POST: api/v1/posts/`
Payload:
```json
{
	"text": "string",
	"image": "string",
	"group": 0
}
```
Ответ:
```json
{
	"id": 0,
	"author": "string",
	"text": "string",
	"pub_date": "2019-08-24T14:15:22Z",
	"image": "string",
	"group": 0
}
```
Полная документация по запросам доступна по адресу `http://127.0.0.1:8000/redoc/`
