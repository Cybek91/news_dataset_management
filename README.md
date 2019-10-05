## News Dataset Management

## Project structure

```
├── dataset                   // place where datasets will be imported
│   └── some_dataset.json
├── import_dataset
│   └── __init__.py
│   └── import_dataset.py      // core module for importing and saving dataset to db
├── search_engine
│   └── __init__.py
│   └── search_engine.py      // core module for searching purposes
├── main_cli.py               // application source
├── project_config            // File where we store project settings
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
python main_cli.py [-h] [-v] [-vv] {search_engine,import_dataset} [opts]
```

Example of importing dataset from Dataset folder and save it to the "foobar" table:
```bash
python main_cli.py -vv import_dataset "News_Category_Dataset_v2.json" --table_name "foobar"  
```

Example of checking if phrase "will smith" is included in the dataset stored in `"foobar"` table:
```
python main_cli.py -vv search_engine --phrase "will smith" --table_name "foobar"
```
* Important thing -> if `--table_name` is not provided in the params, application will use `"news"` as a default table
#### Things which could be added/improved:
* tests (pytest, unitest)
* linter (ex. pylint)
* code formater (ex. black)

