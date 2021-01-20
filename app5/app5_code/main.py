from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
import json, glob
from datetime import datetime

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
        print(feel)
        print(type(feel))

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        #Initialization of RootWidget no declaring class
        return RootWidget()



if __name__ == "__main__":
    MainApp().run()

#Note: if no error in terminal then check kv file


#AppMain APP > RootWidget > Login Screen