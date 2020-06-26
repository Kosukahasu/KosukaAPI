from utils.json import jsonify2
from utils.log.errors import error
from utils.carl import *

from flask import Blueprint, request

from helpers import databaseConnector as db

handler = Blueprint('getLeaderBoardOM', __name__)

@handler.route("/kusoka/LeaderBoard")
def getLeaderBoardOM():
	db.SQLd.execute('''
		SELECT
		    id, team, point, win, lose, logo
		FROM leaderboard
		ORDER BY leaderboard.point DESC LIMIT 3
	    ''')
	data = db.SQLd.fetchall()

	return jsonify2(sort_keys=False, indent=8, code=200, data=data)
