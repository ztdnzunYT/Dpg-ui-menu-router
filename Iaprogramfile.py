import dearpygui.dearpygui as dpg
import Iaaccounts
import pygame
pygame.mixer.init(frequency=60000,size=-16, channels=2,buffer=1050)
import time
import keyboard

class Ia_audios:
    volume = .7
    def Startupaudio():
        loadupchime = pygame.mixer.Sound("Audio/Appstartupsound.mp3")
        pygame.mixer.Sound.play(loadupchime)

    def Inputaudio():
        Input_audio = pygame.mixer.Sound("Audio/keyclick.mp3")
        Input_audio.set_volume(Ia_audios.volume-.3)
        pygame.mixer.Sound.play(Input_audio)
        dpg.set_value("invalid_inputem","")

    def Accessdeniedaudio():
        Access_denied_audio = pygame.mixer.Sound("Audio/Accessdenied.mp3")
        Access_denied_audio.set_volume(Ia_audios.volume)
        pygame.mixer.Sound.play(Access_denied_audio)
        
    def Accessgrantedaudio():
        Access_granted_audio = pygame.mixer.Sound("Audio/Accessgranted.mp3")
        Access_granted_audio.set_volume(Ia_audios.volume)
        pygame.mixer.Sound.play(Access_granted_audio)

    def Interfaceclick():
        Interfaceclick_audio = pygame.mixer.Sound("Audio/Interfaceclick.mp3")
        Interfaceclick_audio.set_volume(Ia_audios.volume)
        pygame.mixer.Sound.play(Interfaceclick_audio)

class Login:
    def Gatekeeper(sender,val,user_data):
        user_input = dpg.get_value("Username")
        pass_input = dpg.get_value("Password")
        username = ""  #ANYTHING YOU WANT
        password = "" #ANYTHING YOU WANT 
        user_data = user_data
        
        if user_input == username and pass_input == password:
            Ia_audios.Accessgrantedaudio()
            time.sleep(.2)
            dpg.show_item("menu_bar_window")
            dpg.show_item("releases")
            dpg.set_primary_window("releases",True)
            dpg.hide_item("login_window")
            
        else:
            Ia_audios.Accessdeniedaudio()
            dpg.set_value("Username","")
            dpg.set_value("Password","")
            dpg.set_value("invalid_inputem","Incorrect username or password")

class Windowmanagement():
    def Releases():
        Windowmanagement.Windowmanager("releases")
        Ia_audios.Interfaceclick()
    def Buy():
        Windowmanagement.Windowmanager("buy")
        Ia_audios.Interfaceclick()
    def Sell():
        Windowmanagement.Windowmanager("sell")
        Ia_audios.Interfaceclick()
    def Trade():
        Windowmanagement.Windowmanager("trade")
        Ia_audios.Interfaceclick()
    def Info():
        Windowmanagement.Windowmanager("info")
        Ia_audios.Interfaceclick()
    def Profile():
        Windowmanagement.Windowmanager("profile")
        Ia_audios.Interfaceclick()
    def Settings():
        Windowmanagement.Windowmanager("settings")
        Ia_audios.Interfaceclick()

    def Windowmanager(self):
        Windowmanagement.Hidewindows()
        dpg.show_item(self)
        dpg.set_primary_window(self,True)
    def Hidewindows():
        windows = dpg.get_windows()
        for i in range(len(windows)-1):
            dpg.hide_item(windows[i])
            
class Closeapp:
    def Closeapp():
        dpg.destroy_context()









            

        
            

            
            





'''def Gatekeeper(sender,val,user_data):
    User_input = dpg.get_value("Username")
    Pass_input = dpg.get_value("Password")
    Username = "Dnzun"
    Password = "Password"
    
    if User_input == Username and Pass_input == Password:
        print("Login successfull")
        Ia_audios.Accesgrantedaudio()
    else:
        dpg.set_value( user_data, "Incorrect username or password")
        User_input = dpg.set_value("Username","")
        Pass_input = dpg.set_value("Password","")   
        Ia_audios.Accessdeniedaudio()'''




#if login condition true print message
#else input audio error sound and clear username and password dpg
#test the while true try exect value error 
