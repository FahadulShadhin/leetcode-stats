# LeetCode Stats

API to fetch your LeetCode profile stats

[![python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)

## Setup:

- Clone the repository
- `cd` to root folder
- Create a virtual environment: `python3 -m venv {ENV_NAME}`
- Activate the virtual environment:
  - Windows: `.\{ENV_NAME}\Scripts\activate`
  - Unix: `source /{ENV_NAME}/bin/activate`
- Install dependencies: `pip3 install -r requirements.txt`
- Run dev server:

```console
$ uvicorn main:app --reload --host 127.0.0.1 --port 8000

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [24808] using WatchFiles
INFO:     Started server process [27200]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

- Hit the endpoint to get stats: `http://127.0.0.1:8000/{USERNAME}`

## How to use:

- URL: `https://leetcode-stats-api.onrender.com/<your_leetcode_username>`
- [Test with API Docs](https://leetcode-stats-api.onrender.com/docs)

### Example:

- python3

```python
import requests

response = requests.get('https://leetcode-stats-api.onrender.com/shadhin17')
stats = response.json()
print(stats['data'])
```

- js

```js
fetch('https://leetcode-stats-api.onrender.com/shadhin17')
	.then((response) => response.json())
	.then((stats) => console.log(stats.data))
	.catch((error) => console.error(error));
```

- curl

```bash
curl https://leetcode-stats-api.onrender.com/shadhin17
```
