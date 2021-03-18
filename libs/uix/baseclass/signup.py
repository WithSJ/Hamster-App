from main_imports import MDScreen
from libs.applibs import utils
from libs.applibs.firebase import authentication
utils.load_kv("signup.kv")

class Signup_Screen(MDScreen):
    def signup(self,email,fullname,username,password):
        print(email,fullname,username,password)
        print(
                authentication.SignUp(
                email= email, fullname= fullname,
                username= username, password= password)
            )
        