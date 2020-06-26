import sys
import time

from json import dumps
from flask import Flask, g

from utils.log import errors as err

from handlers import getLeaderBoardOM

app = Flask(__name__)

app.register_blueprint(getLeaderBoardOM.handler)

@app.errorhandler(404)
def resource_not_found(e):
  return err.error(404, "not found!")

if __name__ == "__main__":
	print(f'''api made by simon the lazy guy''')
	# zzzzzzzzzz
	app.run(port=2222, debug=True)
