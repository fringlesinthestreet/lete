import oracledb
import os


def getConnection():
    username = os.getenv("BD_USER")
    password = os.getenv("BD_PASS")
    host = os.getenv("BD_HOST")
    port = os.getenv("BD_PORT")
    sid = os.getenv("BD_SID")
    return oracledb.connect(
        user=username,
        password=password,
        dsn=f"{host}:{port}/{sid}"
    )


class DBClient:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection is not None:
            self.connection.close()

    def insertDataIntoTable(self, fileName, fileData):
        if self.connection is None:
            return
        cursor = None
        try:
            cursor = self.connection.cursor()
            insertSQL = """
            INSERT INTO ADM_FONASA_HIST.TB_XML (ARCHIVO, DATA_XML)
            VALUES (:archivo, :data_xml)
            """
            cursor.execute(insertSQL, [fileName, fileData])
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred uploading {fileName}: {e}")
        else:
            print(f"Successfully uploaded {fileName}")
        finally:
            if cursor is not None:
                cursor.close()

    def callStoreProcedure(self):
        prName = "ADM_FONASA_HIST.PR_"
        if self.connection is None:
            return
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.callproc(prName)
        except Exception as e:
            print(f"An error occurred calling PR {prName}: {e}")
        else:
            print(f"Successfully called {prName}")
        finally:
            if cursor is not None:
                cursor.close()

    def cleanTable(self):
        if self.connection is None:
            return
        cursor = None
        try:
            cursor = self.connection.cursor()
            truncateSQL = """
            TRUNCATE TABLE ADM_FONASA_HIST.TB_XML CASCADE
            """
            cursor.execute(truncateSQL)
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred uploading {fileName}: {e}")
        else:
            print(f"Successfully uploaded {fileName}")
        finally:
            if cursor is not None:
                cursor.close()


if __name__ == '__main__':
    pass
