from dbclient import DBClient, getConnection
from dotenv import load_dotenv
import glob
import os

FILES_DIR_PATH = './files'


def getXMLFilePaths():
    filePattern = os.path.join(FILES_DIR_PATH, '*.xml')
    for filePath in glob.glob(filePattern):
        yield filePath


if __name__ == '__main__':
    load_dotenv()
    with DBClient(getConnection()) as dbclient:
        for filePath in getXMLFilePaths():
            with open(filePath, 'rb') as file:
                fileData = file.read()
            dbclient.insertDataIntoTable(filePath, fileData)
            dbclient.callStoreProcedure()
            dbclient.cleanTable()
