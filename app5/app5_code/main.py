from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
import json, glob
from pathlib import Path
from datetime import datetime
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')


#class string has to be same as the rule <>
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current="sign_up_screen"
    def login(self,uname,pword):
        with open("users.json") as file:
            users=json.load(file)
        if uname in users and users[uname]['password']==pword:
            self.manager.current="login_screen_success"
        else:
            #printing later on 
            self.ids.login_wrong.text="Wrong username or password"


                

             

class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("users.json") as file:
            users=json.load(file)
            #creating new entry in the dictionary of dictionary that is the json
            users[uname]={'username':uname,'password':pword, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", 'w') as file:
            json.dump(users, file)
        
    def sign_up_screen_success(self):
        self.manager.current="sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def login_page(self):

        self.manager.transition.direction = 'right'
        self.manager.current="login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current="login_screen"
        
        #self.manager.transition.direction = 'right'
        #self.manager.current="login_screen"
    def get_quote(self, feel):
        feel=feel.lower()
        available_feelings=glob.glob("quotes/*txt")
        #glob.glob gives a list of file names

        #Path object extracts the filename using the extracts method
        #creates list
        available_feelings=[Path(filename).stem for filename in
                            available_feelings]

        #print(available_feelings)
        
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes= file.readlines()
            self.ids.quote.text= random.choice(quotes) 
        else:
            self.ids.quote.text = "Try another feeling we support happy, sad, unloved "
        

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        #Initialization of RootWidget no declaring class
        return RootWidget()

#button behaviour first as placing other classes first may hide that behaviour
class ImageButton( ButtonBehavior,HoverBehavior, Image):
    pass




if __name__ == "__main__":
    MainApp().run()

#Note: if no error in terminal then check kv file


#AppMain APP > RootWidget > Login Screen