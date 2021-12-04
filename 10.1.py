# Aidan Doshier
# 10.1 Make your own Class!

# Speaker Class
class Speaker():

    # init Method 
    # Defines volume, color, and mode as default values -
    # - so if no new ones are entered, these are what appear.
    # Also defines an empty list for the add_device function later on.

    def __init__(self, volume=5, color="Blue", mode="Bluetooth"):
        self.__volume = volume
        self.__color = color
        self.__mode = mode
        self.list_of_devices = []

    # set_vol Method
        # Defines vol_change and new_vol
        # If there is no volume change -
            # The new_vol = the default volume value.
        # If the volume is greater than 10 or less than 0 after the change -
            # Chanags the volume to either 10 or 0.
            # Prints a message that tells the min or max volume level.
        # If it is just a normal volume change - 
            # Print out what the volume was, how much it changed by, and what it is now.
        # Sets the volume of the speaker to whatever new_vol is, for the get_vol method later.

    def set_vol(self, vol_change):
        self.__vol_change = vol_change
        self.__new_vol = self.__volume + self.__vol_change
        if self.__vol_change == None:
            self.__new_vol = self.__volume
            print("There was no volume change.")
        elif self.__new_vol > 10:
            self.__new_vol = 10
            print(f"The speaker's max volume is 10, so the volume is now {self.__new_vol}.")
        elif self.__new_vol < 0:
            self.__new_vol = 0
            print(f"The speaker's minimum volume is 0, so the volume is now {self.__new_vol}.")
        else:
            print(f"The volume was {self.__volume}, was changed by {self.__vol_change}, and is now {self.__new_vol}.")
        self.__volume = self.__new_vol

    # set_color Method
        # Defines valid colors and new_color.
        # If there is no color change -
            # The new_color = the default color value.
        # If the new_color isn't in the colors list - 
            # Prints out an error message, and what the valid colors are.
        # If there is a color change - 
            # Print out what the color was, and what it is now.
            # Sets the color of the speaker to whatever new_color is, for the get_color method later.

    def set_color(self, new_color):
        self.__colors = ["Red", "Blue", "Green", "Light Blue", ]
        self.__new_color = new_color
        if self.__new_color == None:
            self.__new_color = self.__color 
            print("There was no color change.")
        elif self.__new_color not in self.__colors:
            print(f"That is not an valid color, please pick a diffent color out of {self.__colors}.")
        else:
            print(f"The color was {self.__color} and is now {self.__new_color}.")
            self.__color = self.__new_color

    # set_mode Method
        # Defines valid modes and new_mode.
        # If there is no mode change -
            # The new_mode = the default mode value.
        # If the new_mode isn't in the modes list - 
            # Prints out an error message, and what the valid mode options are.
        # If there is a mode change - 
            # Print out what the mode was, and what it is now.
            # Sets the mode of the speaker to whatever new_mode is, for the get_mode method later.

    def set_mode(self, new_mode):
        self.__modes = ["Aux", "Bluetooth"]
        self.__new_mode = new_mode
        if self.__new_mode == None:
            self.__new_mode = self.__mode
            print("There was no change in mode.")
        elif self.__new_mode not in self.__modes:
            print(f"That is not a valid mode, please pick a different mode out of {self.__modes} ")
        else:
            print(f"The mode was {self.__mode} and is now {self.__new_mode}.")
            self.__mode = self.__new_mode

    # get_vol, get_color, and get_mode Methods
        # Returns the value of either the volume, color, or mode of the speaker.

    def get_vol(self):
        return f"The volume is {self.__volume}."

    def get_color(self):
        return f"The color is {self.__color}"

    def get_mode(self):
        return f"The mode is {self.__mode}."

    # song Method
        # Defines t_f which stands for True or False.
        # If t_f is True - 
            # Return there is a song playing.
        # If t_f is False - 
            # Return there is no song playing.

    def song(self, t_f):
        self.__t_f = t_f
        if self.__t_f == True:
            return "There is a song currently playing."
        elif self.__t_f == False:
            return "There is no song currently playing."

    # add_device Method
        # Defines device name.
        # Appends the list of devices at from the __init__ method.
        # Prints the device has been added.
        # Returns the list of current addded devices.

    def add_device(self, device_name):
        self.__device_name = device_name
        self.list_of_devices.append(self.__device_name)
        print(f"{self.__device_name} has been added as a new device.")
        return f"Known devices: {self.list_of_devices}."

    # __str__ Method
        # Defines name variable.
        # Returns a string of all of the information used in the get-set methods.

    def __str__(self, name):
        self.__name = name
        return f"{self.__name}'s speaker is at volume {self.__volume}, has the color set to {self.__color}, and is currently on {self.__mode} mode."

# Main Function
    # Runs all methods.

def main():
    speaker = Speaker()
    speaker.set_vol(3)
    speaker.set_color(None)
    speaker.set_mode("Aux")
    print(speaker.get_vol())
    print(speaker.get_color())
    print(speaker.get_mode())
    print(speaker.song(False))
    print(speaker.add_device("Aidan's iPhone"))
    print(speaker.add_device("Andrew's Google Pixel"))
    print(speaker.__str__("Aidan"))

# Calls main function.
if __name__ == "__main__":
    main()