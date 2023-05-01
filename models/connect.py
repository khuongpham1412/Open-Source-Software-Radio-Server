import sqlite3


class Store:
    # def __init__(self, name, image, path):
    #     self.name = name

    def sql_database(seft):
        conn = sqlite3.connect('Radio.db')
        conn.execute(
            'CREATE TABLE IF NOT EXISTS tbl_music (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, image TEXT, path TEXT NOT NULL );')
        conn.commit()
        conn.close()

    def delete_table(seft, name):
        conn = sqlite3.connect('Radio.db')
        conn.execute('DROP TABLE tbl_music;')
        conn.commit()
        conn.close()

    def add_music(seft, name, image, path):
        conn = sqlite3.connect('Radio.db')
        cursor = conn.cursor()
        params = (name, image, path)
        cursor.execute(
            "INSERT INTO tbl_music (name, image, path) VALUES " + str(params) + ";")

        conn.commit()
        print('Add Music Success !!!')
        conn.close()

    def delete_music(seft, id):
        conn = sqlite3.connect('Radio.db')
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tbl_music WHERE id=" + str(id) + ";")
        conn.commit()
        print('Delete Music Success !!!')
        conn.close()

    def getAll(seft):
        conn = sqlite3.connect('Radio.db')
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM tbl_music")
        return data

    # def data_retrieval(name):
    #     conn = sqlite3.connect('Client_data.db')
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM Client_db1 WHERE NAME =:NAME",
    #                 {'NAME': username})
    #     if cur.fetchone()[1] == password:
    #         print('LogIn Successful')


# sql_database()
# delete_table("djekn")
# add_music("name test 1", "image test 1", "path test 1")
# add_music("name test 2", "image test 2", "path test 2")
# delete_music(2)
# test = Store()
# test.delete_music(10)
# test.add_music("name test 12", "image test 1", "path test 2")
# data = test.getAll()
# for item in data:
#     print(item)
