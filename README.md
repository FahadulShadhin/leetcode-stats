# LeetCode Stats

API to fetch your LeetCode profile stats

### Setup:

- Built with `Python 3.10.7`
- Clone the repository
- `cd` to root folder
- Create a virtual environment: `python3 -m venv {ENV_NAME}`
- Activate the virtual environment:
  - Windows: `.\{ENV_NAME}\Scripts\activate`
  - Unix: `source /{ENV_NAME}/bin/activate`
- Install dependencies: `pip3 install -r requirements.txt`
- Run dev server: `uvicorn main:app --reload --host {HOST} --port {PORT}`
- Hit the endpoint to get stats: `http://{HOST}:{PORT}/{USERNAME}`

### How to use:

- URL: `https://leetcode-stats-api.onrender.com/<your_leetcode_username>`
- [Test with API Docs](https://leetcode-stats-api.onrender.com/docs)

#### Example:

- Python

```python
import requests

response = requests.get('https://leetcode-stats-api.onrender.com/shadhin17')
stats = response.json()
print(stats['data'])
```

- JavaSceipt

```js
fetch('https://leetcode-stats-api.onrender.com/shadhin17')
	.then((response) => response.json())
	.then((stats) => console.log(stats.data))
	.catch((error) => console.error(error));
```
