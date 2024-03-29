# StockPilot

### [Video Demo](https://www.youtube.com/watch?v=7Xej3eWsAy4&ab_channel=StockPilot)

### Python Virtual Environment Setup
Make sure you have python 3.6 or higher installed.

```bash
python -m venv env
```

Next to activate the environment

On Unix,Mac
```bash
source env/bin/activate
```
On windows
```bash
.\env\Scripts\activate.bat
```

Next, install the necessary dependencies using the [requirements.txt](requirements.txt) file.

```bash
pip install -r requirements.txt 
```
Set environment varible to run flask app

On Unix,Mac
```bash
export FLASK_APP=app.py
```
On windows
```bash
set FLASK_APP=app.py
```

Set Debug mode ON
```bash
set FLASK_ENV=development
```

### Run The Project
```bash
flask run
```


