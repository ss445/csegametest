import bottle
#import json
#import user


@bottle.route('/')
def webFront():
    return bottle.static_file('game.html', root="")


@bottle.route('/userData.js')
@bottle.route('/static/userData.js')
def userdatajs():
    return bottle.static_file('userData.js', root="")












"""""
@bottle.route('/user.js')
def static():
    return bottle.static_file("user.js", root="")



#hosting image example
@bottle.route('/sprite3')
@bottle.route('/static/sprites/dog.PNG')
def static():
    return bottle.static_file("dog.PNG", root="../sprites")
#


@bottle.route('/getNameList')
def getNameList():
    return json.dumps(user.getNameList())


@bottle.post('/addName')
def addName():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    user.addName(content['message'])
    return json.dumps(user.getNameList())
    

@bottle.post('/removeName')
def do_chat():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    user.removeName(content['message'])
    return json.dumps(user.getNameList())

"""""
bottle.run(host="localhost", port=8080, debug=True)
