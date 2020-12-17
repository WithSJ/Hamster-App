
from kivy.utils import platform
if platform != 'android':
    from kivy.config import Config
    Config.set("graphics","width",360)
    Config.set("graphics","height",740)

from kivy.core.window import Window
Window.keyboard_anim_args = {"d":.2,"t":"in_out_expo"}
Window.softinput_mode = "below_target"

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarListItem,ImageLeftWidget

class HamsterApp(MDApp):

    def change_screen(self,name):
        """
        Switch Screen using screen name
        """
        screen_manager.current = name 

        if name == "home":            
            # MDBottomNavigation not resize there tabs when app stat in android 
            # to resize when switch to home screen 
            screen_manager.get_screen(name).ids.android_tabs.on_resize()
        
        

    def chat_room(self,touch,a):
        self.change_screen("chat_room")
    
    def all_chats(self):
        """
        Add all chats in chat tab
        """
        # for dummy chats [------
        # self.change_screen("profile")
        twolineW= TwoLineAvatarListItem(text=f"Hamster",
            secondary_text="Hamster is Chatting app",
            on_touch_up=self.chat_room)

        twolineW.add_widget(ImageLeftWidget(source="hamster_icon.png"))
        
        screen_manager.get_screen("home").ids.chat_tab.add_widget(twolineW)
        #  ----- ] end dummy chats

    def search_account(self,search_field):
        # for dummy search item [------
        
        twolineW= TwoLineAvatarListItem(text=f"{search_field}",
            secondary_text=f"Hamster text for {search_field}")

        twolineW.add_widget(ImageLeftWidget(source="hamster_icon.png"))
        
        screen_manager.get_screen("home").ids.search_items.add_widget(twolineW)
        # #  ----- ] end dummy search

    
    def change_profile_img(self):
        print("hello")
    def build(self):
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
        self.all_chats()
if __name__ == "__main__":
    HamsterApp().run()
