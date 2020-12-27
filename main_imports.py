"""
IMPORT all modules here that use in this app.

"""


#--[Start UI Imports]
"""All imports for UI here Kivy,KivyMD or etc that help in UI"""
from kivymd.app import MDApp 
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarListItem,ImageLeftWidget
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard,MDSeparator
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from ui.ui_class import OneLineTextDialog
from kivymd.uix.bottomsheet import MDGridBottomSheet
#--[End UI Imports]


#--[Start Non UI Imports]
"""All imports that use in application """

#--[End Non UI Imports]