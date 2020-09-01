import model
import bottle

matquiz = model.Matquiz()

LOGO = """
.___  ___.      ___   .___________. __    __    ______      __    __   __   ________  
|   \/   |     /   \  |           ||  |  |  |  /  __  \    |  |  |  | |  | |       /  
|  \  /  |    /  ^  \ `---|  |----`|  |__|  | |  |  |  |   |  |  |  | |  | `---/  /   
|  |\/|  |   /  /_\  \    |  |     |   __   | |  |  |  |   |  |  |  | |  |    /  /    
|  |  |  |  /  _____  \   |  |     |  |  |  | |  `--'  '--.|  `--'  | |  |   /  /----.
|__|  |__| /__/     \__\  |__|     |__|  |__|  \_____\_____\\______/  |__|  /________|
                                                                                      
                                                                                      
"""

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = matquiz.nova_igra()
    bottle.response.set_cookie("idigre", "idigre{0}".format(id_igre), path="/")
    bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie("idigre").split("e")[1])
    #razbili smo tako, da dobimo ["idigr", "3"] in pokličemo 2. element
    igra, poskus = matquiz.igre[id_igre]
    return bottle.template("igra.tpl", igra=igra, poskus=poskus)    

@bottle.post("/igra/")
def ugibaj():
    id_igre = int(bottle.request.get_cookie("idigre").split("e")[1])
    odgovor = bottle.request.forms.getunicode("odgovor")
    matquiz.ugibaj(id_igre, odgovor)
    bottle.redirect("/igra/")

bottle.run(reloader=True, debug=True)