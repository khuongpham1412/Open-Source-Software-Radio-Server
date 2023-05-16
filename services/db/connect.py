import sqlite3
import psycopg2


class Store:
    def connect(self):
        #postgres://db_radio_app_8bxp_user:sVZhC8jFkHoq1C6GwMlJ0NpqLAPfx2ko@dpg-chho6ngrddl9a74f1pe0-a.oregon-postgres.render.com/db_radio_app_8bxp
        conn = psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = "123456",
            host = "localhost",
            port = 5432
        )
        return conn

    def add_music(self, name, image, path):
        conn = Store.connect(self)
        cursor = conn.cursor()
        params = (name, image, path)
        cursor.execute(
           "INSERT INTO tbl_radio (name, image, path) VALUES " + str(params) + ";")

        conn.commit()
        print('Add Music Success !!!')
        conn.close()

    def delete_music(self, id):
        conn = Store.connect(self)
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tbl_radio WHERE id=" + str(id) + ";")
        conn.commit()
        print('Delete Music Success !!!')
        conn.close()

    def getAll(self):
        conn = Store.connect(self)
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM tbl_radio;")
        return cur.fetchall()
        # columns = [id]
        # for row in data:
        #     # print(row)
        #     keys = tuple(row[c] for c in columns)
        #     print(keys)
        #     print(f'{row["name"]} data inserted Succefully')

    def getMusicById(self, id):
        conn = Store.connect(self)
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM tbl_radio WHERE id=" + str(id) + "")
        data = cur.fetchall()
        return data

    def getMusicLast(self):
        conn = Store.connect(self)
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_radio ORDER BY id DESC LIMIT 1")
        result = cur.fetchone()
        return result

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

# def sql_database(self):
    #     conn = sqlite3.connect('Radio.db')#SERIAL
    #     conn.execute(
    #         'CREATE TABLE IF NOT EXISTS tbl_radio (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, image TEXT, path TEXT NOT NULL );')
    #     conn.commit()
    #     conn.close()

    # def delete_table(self, name):
    #     conn = sqlite3.connect('Radio.db')
    #     conn.execute('DROP TABLE tbl_radio;')
    #     conn.commit()
    #     conn.close()
