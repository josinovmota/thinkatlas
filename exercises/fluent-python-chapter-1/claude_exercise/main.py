import collections

playlists = collections.namedtuple("playlists", ["name", "music_number"])


class Playlist:
    music_number = (number for number in range(1, 11))
    name = ("Estudo", "Academia", "Correr", "Cozinhar", "Jogar", "Live")

    def __init__(self):
        self._playlists = [
            playlists(name, music_number)
            for name in self.name
            for music_number in self.music_number
        ]

    def __len__(self):
        return len(self._playlists)

    def __getitem__(self, position):
        return self._playlists[position]


playlist = Playlist()

for sounds in playlist:
    print(sounds)
