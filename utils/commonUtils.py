def getMods(mod):
	r = ""
	if mod == 0:
		return "NOMOD"
	if mod & mods.NOFAIL > 0:
		r += "NF"
	if mod & mods.EASY > 0:
		r += "EZ"
	if mod & mods.HIDDEN > 0:
		r += "HD"
	if mod & mods.HARDROCK > 0:
		r += "HR"
	if mod & mods.DOUBLETIME > 0:
		r += "DT"
	if mod & mods.HALFTIME > 0:
		r += "HT"
	if mod & mods.FLASHLIGHT > 0:
		r += "FL"
	if mod & mods.SPUNOUT > 0:
		r += "SO"
	if mod & mods.TOUCHSCREEN > 0:
		r += "TD"
	return r
<<<<<<< HEAD
=======

>>>>>>> 2ababc43f24177ac50cf88d75cd5b3f4e8786b9a
