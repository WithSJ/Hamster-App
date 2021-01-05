from libs.applibs import utils
from main_imports import BoxLayout

utils.load_kv("ui_class.kv")

class OneLineTextDialog(BoxLayout):
    
    def input_text(self):
        return self.ids.dialog_text.text
