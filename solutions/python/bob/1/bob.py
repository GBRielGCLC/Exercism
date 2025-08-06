def isQuestion(string):
    return string.strip()[-1] == "?"

def isYelling(string):
    return string.isupper()

def response(hey_bob):
    if (hey_bob == None or hey_bob.strip() == ""):
        return 'Fine. Be that way!'
    elif (isQuestion(hey_bob) and isYelling(hey_bob)):
        return "Calm down, I know what I'm doing!"
    elif (isQuestion(hey_bob)):
        return 'Sure.'
    elif (isYelling(hey_bob)):
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'