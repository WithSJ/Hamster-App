import re
import json

class User:
    def __init__(self,user,userInfo):
        self.localId = user["localId"]
        self.email = user["email"]
        self.displayName = user["displayName"]
        self.idToken = user["idToken"]
        self.registered = user["registered"]
        self.refreshToken = user["refreshToken"]
        self.expiresIn = user["expiresIn"]
        
        self.passwordHash = userInfo["users"][0]["passwordHash"]
        self.emailVerified = userInfo["users"][0]["emailVerified"]
        self.passwordUpdatedAt = userInfo["users"][0]["passwordUpdatedAt"]
        self.providerUserInfo = userInfo["users"][0]["providerUserInfo"]
        self.validSince = userInfo["users"][0]["validSince"]
        self.lastLoginAt = userInfo["users"][0]["lastLoginAt"]
        self.createdAt = userInfo["users"][0]["createdAt"]
        self.lastRefreshAt = userInfo["users"][0]["lastRefreshAt"]


class Validator:
    @classmethod
    def isValidEmail(cls,email):

        if len(email) > 7:
        
            if re.match(
                "^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,5}$",
                email) != None:
                return True
        
        return False
    
    @classmethod
    def isValidPassword(cls,password):

        if len(password) > 8:
        
            if re.match(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$",
                password) != None:
                return True
        
        return False

    @classmethod
    def isValidUsername(cls,username):

        if len(username) > 5:
        
            if re.match(
                "^[A-Za-z]\\w{5,29}$",
                username) != None:
                return True
        
        return False

    