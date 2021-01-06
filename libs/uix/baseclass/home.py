from main_imports import ImageLeftWidget, MDScreen, TwoLineAvatarListItem
from libs.applibs import utils

utils.load_kv("home.kv")

class Home_Screen(MDScreen):
    
    def search_account(self,search_field):
        """
        this method use when search button pressed search_field
        contain data in string that you want to search on hamster server
        """

        # for dummy search item [------
        
        twolineW= TwoLineAvatarListItem(text=f"{search_field}",
            secondary_text=f"@{search_field}")

        twolineW.add_widget(ImageLeftWidget(source="assets//img//hamster_icon.png"))
        
        self.ids.search_items.add_widget(twolineW)
        # #  ----- ] end dummy search
    
    