from libs.applibs.firebase.config import firebase
from libs.applibs.firebase.utils import Validator,User
from libs.applibs.firebase.database import CreateNewUser

Auth = firebase.auth()

def SignUp(email,password,username,fullname):
    email = email.lower()

    if not Validator.isValidEmail(email):
        return {"ERROR": True,
            "MESSAGE":"Not a valid email."
            }

    if not Validator.isValidPassword(password):
        return {"ERROR": True,
            "MESSAGE":"Not a valid password."}

    try:
        user=Auth.create_user_with_email_and_password(email,password)
        Auth.send_email_verification(user["idToken"])
        CreateNewUser(user["localId"],fullname=fullname,username=username)
        
        return {"ERROR": False,
            "MESSAGE":"Account created. Check your email for verification."}
    except:
        return {"ERROR": True,
            "MESSAGE":"Email exist."}
    
def Login(email,password):
    email = email.lower()

    if not Validator.isValidEmail(email):
        return {"ERROR": True,
            "MESSAGE":"Not a valid email."}

    if not Validator.isValidPassword(password):
        return {"ERROR": True,
            "MESSAGE":"Not a valid password."
            }

    try:
        login_user = Auth.sign_in_with_email_and_password(email,password)
        login_userInfo = Auth.get_account_info(login_user["idToken"])

        user = User(login_user,login_userInfo)

        if user.emailVerified != True:
            Auth.send_email_verification(user.idToken)
            return {"ERROR": True,
                "MESSAGE":"Email not verified. Check your email."}

        return {"ERROR": False,
            "MESSAGE":"Login Successfull",
            "USERDATA":user}
    except:
        return {"ERROR": True,
            "MESSAGE":"Invalid email or password. "
            }
    
def PasswordReset(email):
    email = email.lower()
    
    if not Validator.isValidEmail(email):
        return {"ERROR": True,
            "MESSAGE":"Not a valid email."
            }

    try:
        Auth.send_password_reset_email(email)
        return {"ERROR": False,
            "MESSAGE":"Check email for reset password."}
    except:
        return {"ERROR": True,
            "MESSAGE":"Email not found."
            }