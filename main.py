"""This code to detect it's Android or not 
if it's not android than app window size change in android phone size"""
from kivy.utils import platform
if platform != 'android':
    from kivy.config import Config
    Config.set("graphics","width",360)
    Config.set("graphics","height",740)
#--[End platform specific code]

"""code for android keyboard. when in android keyboard show textbox 
automatic go to top of keyboard so user can see when he type msg"""
from kivy.core.window import Window
Window.keyboard_anim_args = {"d":.2,"t":"in_out_expo"}
Window.softinput_mode = "below_target"
#--[End Msg Box code ]

"""All imports for UI here Kivy,KivyMD or etc that help in UI"""
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarListItem,ImageLeftWidget
# from kivymd.uix.label import MDLabel
# from kivymd.uix.card import MDCard
# from kivymd.uix.button import MDRoundFlatButton

#--[End UI Imports]


class HamsterApp(MDApp):
    """
    Hamster App start from here this class is root of app.
    in kivy (.kv) file when use app.method_name app is start from here
    """

    def change_screen(self,name):
        """
        Switch Screen using screen name
        """
        screen_manager.current = name 

        if name == "home":            
            # MDBottomNavigation not resize there tabs when app stat in android 
            # to resize when switch to home screen 
            screen_manager.get_screen(name).ids.android_tabs.on_resize()
        
        
    def chat_textbox(self):
        """
            MDCard size change when MSGbox use multilines.
            MDCard y axis size incress when MSGbox y axis size incress
        """
        fixed_Y_size = screen_manager.get_screen("chat_room").ids.root_chatroom.size[1]/2
        msg_textbox=screen_manager.get_screen("chat_room").ids.msg_textbox.size
        if msg_textbox[1] <= fixed_Y_size:
            screen_manager.get_screen("chat_room").ids.send_card.size[1]=msg_textbox[1]
            print(msg_textbox)
        else:
            screen_manager.get_screen("chat_room").ids.send_card.size[1]=fixed_Y_size

    def send_msg(self,msg_data):
        """
            When send button use to send msg this function call
            and clear MSGbox 
        """
        # text_msg = MDLabel(text=msg_data,halign="right")
        # new_msg = text_msg
        # screen_manager.get_screen("chat_room").ids.all_msgs.add_widget(new_msg)
        print(msg_data)
        screen_manager.get_screen("chat_room").ids.msg_textbox.text=""


    def chat_room(self,touch,a):
        """Switch to Chatroom. but username and chatroom username 
        change according to which one you touch in chat list"""
        
        name = touch.text
        screen_manager.get_screen("chat_room").ids.profile_bar.title = name
        self.change_screen("chat_room")
    
    def all_chats(self):
        """
        All Chat that show in home chat tab. all chat are added by 
        this method. it will use in differe t in future.
        """
        # for dummy chats [------
        # self.change_screen("profile")
        twolineW= TwoLineAvatarListItem(text=f"Hamster",
            secondary_text="@username",
            on_touch_up=self.chat_room)

        twolineW.add_widget(ImageLeftWidget(source="hamster_icon.png"))
        
        screen_manager.get_screen("home").ids.chat_tab.add_widget(twolineW)
        #  ----- ] end dummy chats

    def search_account(self,search_field):
        """
        this method use when search button pressed search_field
        contain data in string that you want to search on hamster server
        """

        # for dummy search item [------
        
        twolineW= TwoLineAvatarListItem(text=f"{search_field}",
            secondary_text=f"@{search_field}")

        twolineW.add_widget(ImageLeftWidget(source="hamster_icon.png"))
        
        screen_manager.get_screen("home").ids.search_items.add_widget(twolineW)
        # #  ----- ] end dummy search

    
    def change_profile_img(self):
        """
        method call when image click on profile_view page.
        if it's user own profile than show options of change.
        """
        print("hello")

    def build(self):
        """
        This method call before on_start() method so anything
        that need before start application all other method and code 
        write here.
        """
        self.theme_cls.theme_style="Light"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("ui//login.kv"))
        screen_manager.add_widget(Builder.load_file("ui//signup.kv"))
        screen_manager.add_widget(Builder.load_file("ui//forgot.kv"))
        screen_manager.add_widget(Builder.load_file("ui//verification.kv"))
        screen_manager.add_widget(Builder.load_file("ui//home.kv")) 
        screen_manager.add_widget(Builder.load_file("ui//profile.kv"))
        screen_manager.add_widget(Builder.load_file("ui//chat_room.kv"))
        
        return screen_manager
    
    def on_start(self):
        """
        Anything we want to run when start application that code is here.
        """
        self.all_chats()

if __name__ == "__main__":
    # Start application from here.
    HamsterApp().run() 
