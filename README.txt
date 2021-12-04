README File

GitHub Link: https://github.com/AidanD-21/10.1_Make_A_Class/tree/main

10.1 - Make your own Class!
Aidan Doshier - CSE20-03

Class Documentation --

Desc. Of Class - The class I have created is one that resembles a speaker. The purpose of my class is to portray the speaker (specifically the one I have) and the functions it has. This class has 3 get methods, 3 set methods, and 2 other methods. 

Desc. Of Data/Class Variables - 

All of these variables have 'self.' before them and are private in my actual code.
Class Variables:
-volume: The volume the speaker is currently set to. The default value is 5.
-color: The color the speaker is currently set to. The default value is "Blue".
-mode: The mode the speaker is currently set to. The default value is "Bluetooth".
-list_of_devices: An empty list to be added to by the add_device function.

Data Variables:
-vol_change: The argument used in 'set_vol', which adds to the current value of the volume, which is 5.

-new_vol: The sum of the current volume and vol_change.

-colors: A list of available colors to choose from to change the color of the speaker. ["Red", "Blue", "Green", "Light Blue", ]

-new_color: The argument used in 'set_color' which is what the default color is changed to. Can be a color in the colors list or None.

-modes: A list of available modes to choose from to change the mode of the speaker. ["Aux", "Bluetooth"]

-new_mode: The argument used in 'set_mode' which is what the default color is changed to. Can be a mode in the modes list or None.

-t_f: The argument of the 'song' method. Can be True or False.

-device_name: The argument used in the 'add_device' method. Can technically be anything but is supposed to be what a name of a device would be such as 'Aidan's iPhone'.

-your_name: The argument used in the __str__ method. Is 

Desc. Of Methods - 
-__init__: This method defines all of the class variables.

-set_vol: This method changes the volume of the speaker. It adds or subtracts from the default value of the volume (set in the __init__ function). Has parameters so the volume can't go past 10 or below 0. The argument is a positive or negative integer. Argument can also be None if no volume change is desired.

-set_color: This method changes the color of the speaker from the default color value of the speaker (set in the __init__ function). Also checks if the argument given is in the list of colors. The argument is preferably a color in the colors list but has a message printed if not. Argument can also be None if no color change is desired.

-set_mode: This method changes the mode of the speaker from the default mode value of the speaker (set in the __init__ function). Also checks if the argument given is in the list of modes. The argument is preferably a mode in the modes list but has a message printed if not. Argument can also be None if no mode change is desired. 

-get_vol: Returns a message with what the volume currently is. No arguments are needed.

-get_color: Returns a message with what the color currently is. No arguments are needed.

-get_mode: Returns a message with what the mode currently is. No arguments are needed.

-song: Returns a message if a song is playing or not depending on the argument. The argument 't_f' can be either of the booleans True or False. 

-add_device: Adds a selected device to a list of devices (empty by default). The argument can technically be anything but is supposed to be what a name of a device would be such as 'Aidan's iPhone'. This method has been ran in my code multiple times to show the adding of multiples devices to the list.

-__str__: Returns a string of all of the information used in the get-set methods.

Demo Program Documentation --

Desc. Of Demo Program -
-My demo program prints creates the 'speaker' object from the Speaker class. It runs calls each function with its required arguments, which in turn print out a series of lines that give information about the speaker. There will be a line for every function, that prints out in succession.

Instructions - 
-All that is needed to run the program is to put the specific arguments you want to test in the functions, and then run it.


