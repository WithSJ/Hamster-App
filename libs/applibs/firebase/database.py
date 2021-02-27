from libs.applibs.firebase.config import firebase

database = firebase.database()

def CreateNewUser(localId,fullname="",username=""):
    username = username.lower()
    database.child("Users").child(localId).set(
        {   "fullname":fullname,
            "username": username
        })


def Update_Fullname_Username(localId,newFullname=None,newUsername=None):
    newUsername = newUsername.lower()
    data = database.child("Users").child(localId).get()
    data = dict(data.val())
    
    if newFullname != None:
        data["fullname"]= newFullname
    if newUsername != None:
        data["username"] = newUsername
    
    database.child("Users").child(localId).update(data)

        