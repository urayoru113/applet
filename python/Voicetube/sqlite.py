import sqlite3


class Database:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.__table = None

    def create(self, table, **columns):
        if not table:
            raise AttributeError("Must specify table name")
        if not columns:
            raise AttributeError("Table must specify column and datatype")
        command = f"CREATE TABLE IF NOT EXISTS {table} ( " +\
            ",".join(f"{key} {columns[key]}" for key in columns) + ")"
        self(command)

    def insert(self, *data):
        assert data != None, "No insert data"
        command = f"INSERT INTO {self.table} VALUES (" +\
            ",".join(f"'{value}'" for value in data) + ")"
        self(command)

    def select(self, columns='*', exprs=[]):
        columns = ",".join(columns) if isinstance(columns, list) else columns
        command = f"SELECT {columns} FROM {self.table} "
        if exprs:
            command += "where "
            if isinstance(exprs, list):
                command += (",".join(f"{expr}" for expr in exprs))
            elif isinstance(exprs, str):
                command +=  exprs
            else:
                raise TypeError(f"'{exprs}' must be list or str, but got {type(exprs).__name__}'")
        self(command)

    def delete(self, exprs):
        command = f"DELETE FROM {self.table} "
        if exprs:
            command += "where "
            if isinstance(exprs, list):
                command += (",".join(f"{expr}" for expr in exprs))
            elif isinstance(exprs, str):
                command +=  exprs
            else:
                raise TypeError(f"'{exprs}' must be list or str, but got {type(exprs).__name__}'")
        self(command)

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, table):
        self.__table = table

    def __call__(self, command):
        return self.cursor.execute(command)

