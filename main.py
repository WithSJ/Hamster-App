
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
        

    
    def all_chats(self):
        """
        Add all chats in chat tab
        """
        # for dummy chats [------
        for i in range(10):
            twolineW= TwoLineAvatarListItem(text=f"Hamster",
                secondary_text="Hamster is Chatting app")

            twolineW.add_widget(ImageLeftWidget(source="hamster_icon.png"))
            
            screen_manager.get_screen("home").ids.chat_tab.add_widget(twolineW)
        #  ----- ] end dummy chats

    def build(self):
        self.theme_cls.theme_style="Light"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("ui//login.kv"))
        screen_manager.add_widget(Builder.load_file("ui//signup.kv"))
        screen_manager.add_widget(Builder.load_file("ui//forgot.kv"))
        screen_manager.add_widget(Builder.load_file("ui//verification.kv"))
        screen_manager.add_widget(Builder.load_file("ui//home.kv"))        
        return screen_manager

if __name__ == "__main__":
    HamsterApp().run()
