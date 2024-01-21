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

- `https://leetcode-stats-api.onrender.com/<your_leetcode_username>`

### [Test with the API Documentation](https://leetcode-stats-api.onrender.com/docs)
