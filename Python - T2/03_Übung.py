SERVER_LIST = ["server_1", "server_2"]
OPEN_PORTS = [8532, 8654, 6959, 4969]
USERS = [
    {"name":"admin", "pw":"m4in"}, 
    {"name":"hans", "pw":"abc123"}
]

def connect(user_name: str, user_pw: str, **config):
    if "server" not in config:
        server = SERVER_LIST[0]
    else:
        if config["server"] in SERVER_LIST:
            server = config["server"]
        else:
            raise Exception("Unbekannter Server: " + config["server"])
            
    if "port" not in config:
        port = OPEN_PORTS[0]
    else:
        if config["port"] in OPEN_PORTS:
            port = config["port"]
        else:
            raise Exception("Geschlossener/Unbekannter Port: ", config["port"])
            
    for user in USERS:
        if user_name == user["name"]:
            if user_pw == user["pw"]:
                print("Erfolgreich eingeloggt!")
                print("Server:", server)
                print("Port:", port)
                return True
            else:
                raise Exception("Passwort falsch!")
    
    raise Exception("User nicht gefunden!")
    
    
connect("admin", "m4in")            
connect("admin", "m4in", server="server_2", port=6959)
connect("admin", "m4in", server="server_3", port=6959)