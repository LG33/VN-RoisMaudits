# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.95
        
        $i = 0
        $hSpacing = 20
        $vSpacing = 20
            
        hbox:
            spacing hSpacing
            vbox:
                style "menu"
                spacing vSpacing 
                 
                for caption, action, chosen in items:
                    $i += 1
                    if i % 2 == 1:
                        if action:
                             
                            button:
                                action action
                                style "menu_choice_button"                       
                               
                                text caption style "menu_choice"
                             
                        else:
                            text caption style "menu_caption"
                   
                if i % 2 == 0:
                    $i = 1
                else:
                    $i = 1               
                           
            vbox:
                style "menu"
                spacing vSpacing
                 
                for caption, action, chosen in items:
                    $i += 1
                    if i % 2 == 1:
                        if action:
                             
                            button:
                                action action
                                style "menu_choice_button"                     
                               
                                text caption style "menu_choice"
                             
                        else:
                            text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default
    
    #le texte
    style menu_choice is button_text:
        color "#fff"
        size 28
        drop_shadow [ (-1, -1), (1, -1), (-1, 1), (1, 1) ] 
        outlines [(1, "#000099", 0, 0)]
        hover_outlines [(1, "#000000", 0, 0)]
        selected_outlines [(1, "#000000", 0, 0)]
        selected_hover_outlines [(1, "#000000", 0, 0)]
    
    # la boite de texte
    style menu_choice_button is button:
        xminimum 700
        xmaximum 700
        yminimum 90
        ymaximum 90
        ypadding 10
        xpadding 10
        background "#000000dd"
        hover_background "#000033dd"
        

## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■
## Screen that's used to display the main menu, when Ren'Py first starts
## http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.
    # begin-end comments like the one in the next line are used to display code examples in the game
#begin add_image
    add "gui/main_menu_ground.jpg" # Add a background image for the main menu.
#end add_image
    $ y=250 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start_%s.png" xpos 1490 ypos y focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav")] at main_eff1
    # Imagebutton documentation: http://www.renpy.org/doc/html/screens.html#imagebutton
    
    # auto - is used to automatically define the images used by this button. We could also use:
    # imagebutton idle "main_start_idle.png" hover "main_start_hover.png"
    
    # xpos 773 ypos y - are used set the coordinates to position the button at 773, 114 (y has a value of 114)
    
    # focus_mask True ensures that only non-transparent areas of the button can be focused. focus_mask defines which parts of the image can be focused, and hence clicked on. http://www.renpy.org/doc/html/style.html#button-style-properties
    
    # action - action to run when the button is activated. This also controls if the button is sensitive, and if the button is selected.
    
    # hovered - action to run when the button gains focus. Square brackets are used to run multiple actions. In this case we play a sound effect and show a tooltip.
    
    # unhovered - action to run when the button loses focus. In this case we hide a tooltip.
    
    $ y+=142 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load_%s.png" xpos 1490 ypos y focus_mask True  action [ShowMenu('charger'), Show("load")] hovered [ Play ("test_two", "sfx/click.wav")] at main_eff2
    $ y+=142
    imagebutton auto "gui/main_quit_%s.png" xpos 1490 ypos y focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav")] at main_eff3
    
screen example: #this screen isn't used. It's just used as an example in the script.
#begin at_atl
    imagebutton auto "gui/main_start_%s.png" xpos 1490 ypos 114 focus_mask True action Start() at main_eff1
#end at_atl

# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
#begin main_eff
init -2:
    transform main_eff1:
        zoom 1
        easein 0.4 zoom 2
    transform main_eff2:
        zoom 1
        easein 0.8 zoom 2
    transform main_eff3:
        zoom 1
        easein 1.2 zoom 2
#end main_eff

            
## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
        
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    
    $ x1=x+220
    $ y1=y+10
    add FileScreenshot(number) xpos x1 ypos y1
    $ x2=x+10
    $ y2=y+10
    text file_text xpos x2 ypos y2 size 20
    

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
    
screen charger:
    tag menu
    
    use sound_On
    use fullscreen_Off
    
    use nav_buttons
    
screen sauvegarder:
    tag menu
    
    use save
    
    use sound_On
    use fullscreen_Off
    
    use nav_buttons
    
screen save:
    image "gui/save_tab_on.png" xpos 0.22 ypos 0.1
    imagebutton auto "gui/load_tab_off_%s.png" xpos 0.1 ypos 0.1 focus_mask True action [Hide("save"), Show("load")] hovered [ Play ("test_one", "sfx/click.wav")]
    
    use save_load_slots
    
screen load:
    image "gui/load_tab_on.png" xpos 0.1 ypos 0.1
    imagebutton auto "gui/save_tab_off_%s.png" xpos 0.22 ypos 0.1 focus_mask True action [Hide("load"), Show("save")] hovered [ Play ("test_one", "sfx/click.wav")]
    
    use save_load_slots
    
screen save_load_slots:
    $ y=210
    for i in range(0, 3):
        imagebutton auto "gui/fileslot_%s.png" xpos 195 ypos y focus_mask True action FileAction(i)
        use load_save_slot(number=i, x=195, y=y)
        $ y+=124
    
    $ y=210
    for i in range(3, 6):
        imagebutton auto "gui/fileslot_%s.png" xpos 620 ypos y focus_mask True action FileAction(i)
        use load_save_slot(number=i, x=620, y=y)
        $ y+=124
        
screen nav_buttons:
    imagebutton auto "gui/retour_%s.png" xpos 0.1 ypos 0.8 action [Return(), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    imagebutton auto "gui/menu_%s.png" xpos 0.22 ypos 0.8 action [MainMenu(), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    imagebutton auto "gui/log_%s.png" xpos 0.7 ypos 0.8 action [ShowMenu('text_history'), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    imagebutton auto "gui/log_%s.png" xpos 0.6 ypos 0.8 action [Jump('credits'), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    
screen sound_Off: 
    imagebutton auto "gui/sound_off_%s.png" xpos 0.58 ypos 0.22 focus_mask True action [SetMute("music",False), SetMute("sfx",False), SetMute("voice",False), Hide("sound_Off"), Show("sound_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    
screen sound_On: 
    imagebutton auto "gui/sound_on_%s.png" xpos 0.58 ypos 0.22 focus_mask True action [SetMute("music",True), SetMute("sfx",True), SetMute("voice",True), Hide("sound_On"), Show("sound_Off")] hovered [ Play ("test_one", "sfx/click.wav")]
    
screen fullscreen_Off:
    imagebutton auto "gui/config_display_fullscreen_%s.png" xpos 0.58 ypos 0.1 focus_mask True action [Preference('display', 'fullscreen'), Hide("fullscreen_Off"), Show("fullscreen_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    
screen fullscreen_On: 
    imagebutton auto "gui/config_display_window_%s.png" xpos 0.58 ypos 0.1 focus_mask True action [Preference('display', 'window'), Hide("fullscreen_On"), Show("fullscreen_Off")] hovered [ Play ("test_one", "sfx/click.wav")]

## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    on "show" action Play("sound", "sfx/alert.wav")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yesno_ground.png"
    imagebutton auto "gui/yesno_yes_%s.png" xpos 0.35 ypos 0.8 action yes_action hover_sound "sfx/click.wav"
    imagebutton auto "gui/yesno_no_%s.png" xpos 0.65 ypos 0.8 action no_action hover_sound "sfx/click.wav"
    
    if message == layout.ARE_YOU_SURE:
        add "gui/yesno_are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yesno_delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno_overwrite_save.png"
    elif message == layout.LOADING:
        add "gui/yesno_loading.png"
    elif message == layout.QUIT:
        add "gui/yesno_quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno_main_menu.png"

## ■██▓▒░ CUSTOM MOUSE POINTER ░▒▓██████████████████████████■
##This block is responsible for the custom mouse pointer
# init python:
    # config.mouse = { }
    # config.mouse["default"] = [
         # ("gui/mouse_pointer.png", 8.8, 0.0),
    # ]
# Configuration variables: http://www.renpy.org/doc/html/config.html
# Custom mouse pointer is commented out, to disable it for the time being, because of an issue in all recent versions of Ren'Py.
# PyTom: "There's also an issue where display latency introduced by newer Nvidia drivers makes config.mouse noticeably slow, when Maximum Pre-Rendered Frames is set (which is the default for the driver). As far as I know, this isn't fixable in the short term. For now, I strongly recommend disabling custom mouse cursors (config.mouse)." (Mar 29, 2013) http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=19703&start=45#p259263

## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

## ■██▓▒░ CUSTOM SOUND CHANNEL ░▒▓██████████████████████████■
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)

## ■██▓▒░ THE TEXTBOX ░▒▓███████████████████████████████████■
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say:
    default side_image = None
    window:
        id "window"
        has vbox:
            style "say_vbox"
        if who:
            text who id "who"
        text what id "what"              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Which quick menu should we use? We use 5 different quick menues for presentation purposes in the script.

## ■██▓▒░ TEXTBOX DROP SHADOW ░▒▓███████████████████████████■
## This block is responsible for the text drop shadow effect for the textbox dialogue.
init:
    $ style.say_dialogue.drop_shadow = (2, 2)
    $ style.say_dialogue.drop_shadow_color = "#000000"

## ■██▓▒░ QUICK MENU ░▒▓████████████████████████████████████■
## Screens for the quick menus above the textbox. We use several different quick menus for presentation purposes.

screen menu_button:
    imagebutton auto "gui/ingame_menu_%s.png" action ShowMenu('sauvegarder') xpos 0.85 ypos 0 focus_mask True

screen ingame_menu:
    imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') focus_mask True at option
    imagebutton auto "gui/quick_main_%s.png" action MainMenu() focus_mask True at home
    imagebutton auto "gui/ingame_menu_%s.png" action [Show('menu_button'), Hide('ingame_menu')] xpos 0.85 ypos 0 focus_mask True
    
init -2:
    transform option:
        xpos 0.85
        ypos -150
        easein_bounce 0.5 ypos 75
        on hide:
            ypos 75
            linear 0.3 ypos -150
    transform home:
        xpos 0.85
        ypos -75
        easein_bounce 0.5 ypos 150
        on hide:
            ypos 150
            linear 0.3 ypos -75
            