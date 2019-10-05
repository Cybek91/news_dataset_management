"""
Setup connection to sqlite3 via Dataset library
"""
import dataset
DB_URL = "sqlite:///mydatabase.db"
DB = dataset.connect(DB_URL)
