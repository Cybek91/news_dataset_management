## News Dataset Management

## Project structure

```
├── dataset                   // datasets store
│   └── some_dataset.json
├── search_engine
│   └── __init__.py           // for loading modules
│   └── search_engine.py      // core module for searching purposes
├── main_cli.py               // application source
├── requirements.txt
```

##  Setup

Install dependencies:
- [`pip`](https://github.com/pypa/pip)
- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv)

Create virtualenv

```
pyenv virtualenv 3.6.8 news_dataset_management
```

Activate virtualenv (every time you start new shell session)

```
pyenv activate news_dataset_management
```

Install project requirements

```
pip install -r requirements.txt
```

## Usage

```
python main_cli.py [-h] [-v] [-vv] {module_name} [opts]
```

Example for checking if phrase "will smith" in included in the dataset:
```
python main_cli.py -vv search_engine "News_Category_Dataset_v2.json" -p "will smith"
```

#### Things which could be added/improved:
* tests (pytest, unitest)
* linter (ex. pylint)
* code formater (ex. black)
* datasets can take a lot of space and they could be stored as zip files and unpacked/proccesed in application
but it's depends on requirements)

