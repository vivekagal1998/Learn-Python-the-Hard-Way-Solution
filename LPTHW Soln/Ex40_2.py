class MyClass(object):
    """docstring for."""
    def __init__(self, lyrics):
        #super, self).__init__()
        self.lyrics = lyrics
        print(lyrics)

    def printme(self):
        var = self.lyrics
        for k,v in var.items():
            print("Key is given by: %s\nValue is given by: %s "%(k,v))

lyrics = {
            'Sakira':       "Sing Well",
            'Sonam Kapoor': "Acts Well",
            'Tiger Shrouff': "Dance Well",
            'Shahrukh Khan': "Romantic Well"
        }

obj = MyClass(lyrics)

obj.printme()
