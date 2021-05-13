import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect(host='multicampus.clhnj2zwdisk.eu-west-2.rds.amazonaws.com',
                                  user='admin',
                                  passwd='master123',
                                  db='multicampus',
                                  port=3306,
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
