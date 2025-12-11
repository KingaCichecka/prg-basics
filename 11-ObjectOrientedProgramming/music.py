# class definition
class Song:
    def __init__(self, performer, title, album, year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return (
            f"Performer: {self.performer}\n"
            f"Title:     {self.title}\n"
            f"Album:     {self.album}\n"
            f"Year:      {self.year}"
        )


# object creation
song1 = Song("George Michael", "Amazing", "Patience", 2004)
song2 = Song("Guns N' Roses", "Patience", "G N' R Lies", 1988)

# object usage
print(song1)
print()
print(song2)
