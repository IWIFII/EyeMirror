import pymysql


class toDoList:
    @staticmethod
    def getToDoList():
        connection = pymysql.connect(host='localhost',
                                     user='mirror',
                                     password='imirror',
                                     database='mirror',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `api_todolist` order by id ASC limit 3"
            cursor.execute(sql)
            rows = cursor.fetchall()
            text = '<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">\u5f85\u529e\uff1a</span></p>';
            i = 0
            for row in rows:
                i += 1
                text += '<p><span style=\" font-size:16pt; color:#ffffff;\">' + str(i) + '.' + row[
                    'content'] + '</span></p>'

            text += '</body></html>'
            return text
            # encodedjson = json.dump(result)
            # style =u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">\u5f85\u529e\uff1a</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">1.\u7761\u89c9</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">2.\u6478\u9c7c</span></p></body></html>"


pass

print(toDoList.getToDoList())
