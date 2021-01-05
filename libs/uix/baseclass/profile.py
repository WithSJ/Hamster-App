from main_imports import (MDDialog, MDFlatButton, MDGridBottomSheet, MDScreen,
                          OneLineTextDialog)

from libs.applibs import utils

utils.load_kv("profile.kv")

class Profile_Screen(MDScreen):
    
    def change_profile_data(self,widget):
        """Change text data using Dialog box.
        [widget] change this widget text"""
        dialogObj =None
        Dialog=OneLineTextDialog()
        def cancel_btn(btn):
            # use function when CANCEL btn click
            dialogObj.dismiss(force=True)
        def ok_btn(btn):
            # use function when OK btn click
            widget.text = Dialog.ids.dialog_text.text
            cancel_btn(btn)
            
            
        if not dialogObj:
            dialogObj=MDDialog(
                auto_dismiss=True,
                title= widget.secondary_text,
                type="custom",
                content_cls=Dialog,
                buttons=[
                    MDFlatButton(
                        text="CANCEL", 
                        # text_color=self.theme_cls.primary_color,
                        on_release=cancel_btn,
                    ),
                    MDFlatButton(
                        text="OK", 
                        # text_color=self.theme_cls.primary_color,
                        on_release=ok_btn,
                    ),
                ],
            )
        dialogObj.open()
        
    
    def change_profile_img(self):
        """
        method call when image click on profile_view page.
        if it's user own profile than show options of change.
        """
        bottom_sheet_menu = MDGridBottomSheet(
            animation=True,
        )
        data = {
            "Upload": "cloud-upload",
            "Camera": "camera",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: print("hello",x,y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()