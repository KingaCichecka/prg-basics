class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1   

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print("Channel list:")
        if len(self.channels) == 0:
            print("No channels.")
        else:
            number = 1
            for number in self:
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")