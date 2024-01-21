# LeetCode Stats

API to fetch your LeetCode profile stats

Setup:

- Clone the repository
- `cd` to root
- Create a virtual environment: `python3 -m venv {ENV_NAME}`
- Install dependencies: `pip install -r requirements.txt`
- Run server: `uvicorn main:app --reload --host {HOST} --port {PORT}`
- Hit the endpoint to get stats: `http://{HOST}:{PORT}/{USERNAME}`
