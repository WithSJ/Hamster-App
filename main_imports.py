"""
IMPORT all modules here that use in this app.

"""


#--[Start UI Imports]
"""All imports for UI here Kivy,KivyMD or etc that help in UI"""
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ImageLeftWidget, TwoLineAvatarListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField

from libs.uix.baseclass.ui_class import OneLineTextDialog

#--[End UI Imports]


#--[Start Non UI Imports]
"""All imports that use in application """

#--[End Non UI Imports]