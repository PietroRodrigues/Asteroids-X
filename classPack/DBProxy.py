import sqlite3 as sql


class DBProxy:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conection = sql.connect(self.db_name)
        self.conection.execute('''CREATE TABLE IF NOT EXISTS dados(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                score TEXT NOT NULL,
                                date TEXT NOT NULL)
                               ''')
        
    def save(self, score_dict: dict):
        self.conection.execute("INSERT INTO dados(name, score, date) VALUES(:name, :score, :date)", score_dict)
        self.conection.commit()


    def relative_top10(self) -> list:
        return self.conection.execute("SELECT * FROM dados ORDER BY score DESC LIMIT 10").fetchall()

    def close(self):
        return  self.conection.close()