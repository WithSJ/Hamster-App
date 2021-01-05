from main_imports import MDCard, MDLabel, MDScreen, MDSeparator
from libs.applibs import utils
utils.load_kv("chat_room.kv")

class Chat_Room_Screen(MDScreen):

    def chat_textbox(self):
        """
            MDCard size change when MSGbox use multilines.
            MDCard y axis size incress when MSGbox y axis size incress
        """
        fixed_Y_size = self.ids.root_chatroom.size[1]/3
        msg_textbox=self.ids.msg_textbox.size
        
        if msg_textbox[1] <= fixed_Y_size:
            
            self.ids.send_card.size[1]=msg_textbox[1]
            print(msg_textbox)
        else:
            self.ids.send_card.size[1]=fixed_Y_size
    
    def send_msg(self,msg_data):
        """
            When send button use to send msg this function call
            and clear MSGbox 
        """
        
        text_msg = MDLabel(text=msg_data,halign="left")
        
        sizeX = self.ids.msg_textbox.size[0]    

        sizeY = self.ids.msg_textbox.size[1]+60
        # ->> sizeY is equal to msg_textbox sizeY because text_msg sizeY not work 
        # that's why i use msg_textbox is called 'Jugaad'
        
        
        msg_card= MDCard(
            orientation= "vertical",
            size_hint=[None,None],
            size=[sizeX,sizeY],
            spacing=8,
            padding=20,
            elevation=9,
            ripple_behavior= True,
            radius= [25,25,25,0 ]

        )
        msg_card.add_widget(MDLabel(
            text= f"Hamster {' '*8} |1:00 PM|",
            theme_text_color= "Secondary",
            size_hint_y= None,
            height= 50
        ))
        msg_card.add_widget(MDSeparator(
            height= "1dp"
        ))

        msg_card.add_widget(text_msg)
        self.ids.all_msgs.add_widget(msg_card)
        print(msg_data)
        self.ids.msg_scroll_view.scroll_to(msg_card)
        self.ids.msg_textbox.text=""

