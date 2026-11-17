import re

scorers = {
    "chess": [
        # game name
        (lambda chat: len(re.findall("chess", chat))),
        # pieces
        (lambda chat: len(re.findall("pawn|rook|bishop|knight|queen|king", chat)) * .75),
        # moves
        (lambda chat: len(re.findall("captures?|castl(e|ing)|promot(e|ing)|en passant", chat)) * .75),
        # openings
        (lambda chat: len(re.findall("sicilian|gambit|defence|opening", chat)) * .5),
    ],
    "fortnite": [
        # game name
        (lambda chat: len(re.findall("fortnite", chat))),
        # skins
        (lambda chat: len(re.findall("skull trooper|black knight|dark voyager|omega", chat)) * 2),
        # weapons
        (lambda chat: len(re.findall("assault rifle|pistol|shotguns|submachine guns|sniper rifles", chat)) * 0.5),
        # gear
        (lambda chat: len(re.findall("gliders?|wraps?|(jam )?tracks?", chat)) * .75),
        
    ],
    "gtaiv": [
        # game name
        (lambda chat: len(re.findall("gtaiv", chat))),

    ],
    "leagueoflegends": [
        # game name
        (lambda chat: len(re.findall("league", chat))),
        # popular champions
        (lambda chat: len(re.findall("(miss ?)?fortune|kai'?sa|jhin|caitlyn|zaahen|nami|ezreal|thresh|jinx|viego", chat))),
        # gameplay components
        (lambda chat: len(re.findall("(bot ?)?lane|jungle|nexus|tower", chat)) * .5),
        # classes
        (lambda chat: len(re.findall("marksm[ae]n|fighter|mage]tank", chat)) * .25),
    ],
    "minecraft": [
        # game name
        (lambda chat: len(re.findall("minecraft", chat))),
        # blocks
        (lambda chat: len(re.findall("blocks?", chat)) * .25),
        # mobs
        (lambda chat: len(re.findall("mobs?|creepers?|ender[ae]n", chat))),
        # dimensions
        (lambda chat: len(re.findall("nether|overworld", chat))),
        # gamemodes
        (lambda chat: len(re.findall("survival|creative", chat)) * .25),
        # activities
        (lambda chat: len(re.findall("parkour|redstone|min(e|ing)|craft(ing)?", chat)) * .33),
    ],
    "unclear": [
        (lambda chat: 0.5),
    ]
}

# Resposes are scored against the scorer for the guessed category to see
# how well it fits. This is not determined by the case itself.
def score(case, category: str) -> float:

    scorer = scorers.get(category)
    if scorer == None: return 0

    file = open("eval/cases/"+case["input"])
    data = file.read()
    file.close()

    # more occurrences means that test scores closer to 1, asymtotically
    return sum([1 - 2**-test(data.lower()) for test in scorer])/len(scorer)
