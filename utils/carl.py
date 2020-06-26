def switchAinu(method):
    switcher = {
        -2: "graveyard",
        -1: "not_submitted",
        0: "unranked",
        1: "needs_update",
        2: "ranked",
        3: "approved",
        4: "qualified",
        5: "loved"
    }
    return switcher.get(method, "error")

def switchOsu(argument):
    switch = {
        "-2": "graveyard",
        "-1": "not_submitted",
        "0": "unranked",
        "1": "ranked",
        "2": "approved",
        "3": "qualified",
        "4": "loved"
    }
    return switch.get(argument, "error")

def readableMode(mode):
    modes = {
        0: "std",
        1: "taiko",
        2: "ctb",
        3: "mania"
    }
    return modes.get(mode, "error")

def convertRelax(something, relaxstring, regularstring):
    if something == 1:
        result = relaxstring
    else:
        result = regularstring

    return result
