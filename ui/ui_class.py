from kivy.uix.boxlayout import BoxLayout
class OneLineTextDialog(BoxLayout):
    
    def input_text(self):
        return self.ids.dialog_text.text
