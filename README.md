# Yatube API
API for social network YaTube
### How to launch:

```
git clone https://github.com/VaSeWS/api_final_yatube
```

```
cd api_final_yatube
```

Create virtual environment:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

Migrate:

```
python3 yatube_api/manage.py migrate
```

Launch the project:

```
python3 yatube_api/manage.py runserver
```
### Requests exapmles:
1. `GET: api/v1/posts/`
Responce:
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
Responce:
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
Full requests documentation avaliable at `http://127.0.0.1:8000/redoc/` after launching.
