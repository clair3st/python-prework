# Ex40: Modules, Classes and Objects

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics #instances attribute

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]) # passing a list of strings into class

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


hey_jude = Song(["Hey jude",
                "don't get me down",
                "sing a sad song",
                "and make it better"])

run_rabit = Song(["Run rabbit, run rabbit",
                "run, run , run",
                "Don't let the farmer have his..."
                "fun, fun, fun"])

hey_jude.sing_me_a_song()

run_rabit.sing_me_a_song()

mary_lyrics = ["Mary had a little lamb",
                "It's fleece was white as snow",
                "And everywhere that Mary went"]

mary_had_a_little_lamb = Song(mary_lyrics)

mary_had_a_little_lamb.sing_me_a_song()
