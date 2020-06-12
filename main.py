# Fixed Screen size as android screen
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')
# remove both line when build App

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

class Tabs(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab on home screen'''


class MessageApp(MDApp):
    def change_screen(self,name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("ui//login.kv"))
        screen_manager.add_widget(Builder.load_file("ui//signup.kv"))
        screen_manager.add_widget(Builder.load_file("ui//forgot.kv"))
        screen_manager.add_widget(Builder.load_file("ui//verification.kv"))
        screen_manager.add_widget(Builder.load_file("ui//home.kv"))
        self.theme_cls.theme_style="Light"
        
        return screen_manager

if __name__ == "__main__":
    MessageApp().run()
