import pymysql

MYSQL_HOST = 'us-cdbr-east-04.cleardb.com'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='b34616311e0a2b',
    passwd='fd4ae79f',
    db='heroku_0633f9f5776814d',
    charset='utf8'
)

# MYSQL_HOST = 'localhost'
# MYSQL_CONN = pymysql.connect(
#     host=MYSQL_HOST,
#     port=3306,
#     user='root',
#     passwd='chanwookim',
#     db='cargodb',
#     charset='utf8'
# )

def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN