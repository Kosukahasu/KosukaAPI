from utils.log import logs as log
import json
import requests
def osuRequest(request, params, getFirst=True):
	# maybe taken from ripple 😳 (flush emoji, why does it look so fucking cursed jesus christ)
	resp = None
	try:
		finalURL = "https://osu.ppy.sh/api/{}?k=5c16373f59f4f3f490511ec016e9270596439022&{}".format(request, params)
		log.debug(finalURL)
		resp = requests.get(finalURL, timeout=5).text
		data = json.loads(resp)
		if getFirst:
			if len(data) >= 1:
				resp = data[0]
			else:
				resp = None
		else:
			resp = data
	finally:
		log.debug(str(resp).encode("utf-8"))
		return resp

def ainuRequest(request, getFirst=True):
	# maybe taken from ripple 😳 (flush emoji, why does it look so fucking cursed jesus christ)
	resp = None
	try:
		finalURL = "https://ainu.pw/api/kurai/{}".format(request)
		log.debug(finalURL)
		resp = requests.get(finalURL, timeout=5).text
		data = json.loads(resp)
		if getFirst:
			if len(data) >= 1:
				resp = data[0]
			else:
				resp = None
		else:
			resp = data
	finally:
		log.debug(str(resp).encode("utf-8"))
		return resp
