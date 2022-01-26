from flaskext.mysql import MySQL
from source.api import app

mysql = MySQL()
mysql.init_app(app)        

class UserOps():
    def create(self):
        pass