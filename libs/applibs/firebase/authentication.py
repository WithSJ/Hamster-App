from libs.applibs.firebase.config import firebase
from libs.applibs.firebase.utils import Validator,User
from libs.applibs.firebase.database import CreateNewUser

Auth = firebase.auth()

def SignUp(email,password,username,fullname):
    email = email.lower()

    if not Validator.isValidEmail(email):
        return {"message":"Not a valid email."}

    if not Validator.isValidPassword(password):
        return {"message":"Not a valid password."}

    try:
        user=Auth.create_user_with_email_and_password(email,password)
        Auth.send_email_verification(user["idToken"])
        CreateNewUser(user["localId"],fullname=fullname,username=username)
        
        return {"message":"Account created. Check your email for verification."}
    except:
        return {"message":"EMAIL EXISTS"}
    
def Login(email,password):
    email = email.lower()

    if not Validator.isValidEmail(email):
        return {"message":"Not a valid email."}

    if not Validator.isValidPassword(password):
        return {"message":"Not a valid password."}

    try:
        login_user = Auth.sign_in_with_email_and_password(email,password)
        login_userInfo = Auth.get_account_info(login_user["idToken"])

        user = User(login_user,login_userInfo)

        if user.emailVerified != True:
            Auth.send_email_verification(user.idToken)
            return {"message":"Email not verified. Check your email."}

        return {"message":"Login Successfull",
                "userData":user}
    except:
        return {"message":"INVALID EMAIL or PASSWORD "}
    
def PasswordReset(email):
    email = email.lower()
    
    if not Validator.isValidEmail(email):
        return {"message":"Not a valid email."}

    try:
        Auth.send_password_reset_email(email)
        return {"message":"Check email for reset password."}
    except:
        return {"message":"EMAIL NOT FOUND"}