class Phone:
    def __init__(self, battery, working, storage_used):
        self.battery = battery
        self.working = True
        self.storage_used = storage_used

    def charging(self, percent):
        self.battery = min(100, self.battery_level + percent)
        print(f"The battery is at {self.battery} %")

    def take_photo(self):
        if not self.is_on:
            print("Phone is off. Cannot take photo.")
            return
        if self.storage_used >= 100:
            print("Storage full!")
            return
        self.storage_used += 1
        self.battery_level -= 2
        print(f"Photo taken! Storage used: {self.storage_used}%")

    def play_music(self):
        if not self.is_on:
            print("Phone is off. Cannot play music.")
            return
        self.battery_level -= 5
        print(f"Playing music... Battery: {self.battery_level}%")

    def show_status(self):
        print("Phone status")
        print("------------")
        print(f"Power: {'ON' if self.is_on else 'OFF'}")
        print(f"Battery level: {self.battery_level}%")
        print(f"Storage used: {self.storage_used}%")
        print()
