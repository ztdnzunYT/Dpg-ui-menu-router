Copyright (c) <2023>, <ztdnzun>
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

import dearpygui.dearpygui as dpg
import pygame
from Iaaccounts import* 
from Iaprogramfile import Ia_audios as Iaa,Login as L,Closeapp as Ca,Windowmanagement as Wm
import keyboard

class Appstartup:
    Iaa.Startupaudio()
    dpg.create_context()
    dpg.create_viewport(title=' IA (Inventory Assistant)',resizable=False,decorated=True)
    dpg.set_viewport_large_icon("inventory.ico")
    dpg.set_viewport_small_icon("inventory.ico")
    dpg.set_viewport_width(500)
    dpg.set_viewport_height(300)

class Windows():
    with dpg.window(label="LOGIN BACKGROUND",tag="background",show=False,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.create_context()
    with dpg.window(label="LOGIN SCREEN", tag="login_window",show=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_text("Inventory Assistant",tag="login text",pos=[170,70],color=(255, 255, 255),) 
        dpg.add_text("-------------------",tag="underscores ",pos=[170,80],color=(255,255, 255,200),) 
        dpg.add_input_text(tag="Username",hint="Username",pos=[80,130],no_spaces=True, callback=Iaa.Inputaudio)
        dpg.add_input_text(tag="Password" ,hint="Password",pos=[80,160],password=True,no_spaces=True, callback=Iaa.Inputaudio)
        dpg.add_button(label="Login", pos=[212,200] ,show=True,callback=L.Gatekeeper,) 
        dpg.add_text(label="Incorrect username or password",tag="invalid_inputem",pos=[135,235], color=(255,0,0,), show=True)

    #Tab background windows
    with dpg.window(label="RELEASES",tag="releases",show=True,no_bring_to_front_on_focus=True,no_close=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_spacer(height=10)
        dpg.add_text("Releases window",)
    with dpg.window(label="BUY",tag="buy",show=True,no_bring_to_front_on_focus=True,no_close=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_spacer(height=10)
        dpg.add_text("Buy window")
    with dpg.window(label="SELL", tag="sell",show=True,no_bring_to_front_on_focus=True,no_close=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_spacer(height=10)
        dpg.add_text("Sell window")
    with dpg.window(label="TRADE", tag="trade",show=True,no_bring_to_front_on_focus=True,no_close=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_spacer(height=10)
        dpg.add_text("Trade window")
    with dpg.window(label="INFO", tag="info",show=True,no_bring_to_front_on_focus=True,no_close=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_spacer(height=10)
        dpg.add_text("Info window")
    with dpg.window(label="PROFILE", tag="profile",show=True,no_bring_to_front_on_focus=True,no_close=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_spacer(height=10)
        dpg.add_text("Profile window")
    with dpg.window(label="SETTINGS", tag="settings",show=True,no_bring_to_front_on_focus=True,no_close=True,width=dpg.get_viewport_width(),height=dpg.get_viewport_height()):
        dpg.add_spacer(height=10)
        dpg.add_text("Settings window")

    class Menutabs:
        with dpg.window(label="MENU BAR WINDOW",tag="menu_bar_window",no_background=True,no_title_bar=True,
                        show=False,pos=[0,0],width=dpg.get_viewport_width(),no_move=True,no_resize=True,no_focus_on_appearing=True):
            with dpg.menu_bar(label="MENU BAR",tag="menu_bar"):
                dpg.add_spacer(width=.1)
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="RELEASES",callback=Wm.Releases,user_data="release")
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="BUY",callback=Wm.Buy)
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="SELL",callback=Wm.Sell) 
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="TRADE",callback=Wm.Trade)
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="INFO",callback=Wm.Info)
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="PROFILE",callback=Wm.Profile)
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="SETTINGS",callback=Wm.Settings)
                dpg.add_separator(label="seperator")
                dpg.add_menu_item(label="X",callback=Ca.Closeapp)
                dpg.add_separator(label="seperator")

    #dpg.show_style_editor()
 

    dpg.set_primary_window("login_window",True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context() 
 


 
