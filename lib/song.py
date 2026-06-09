class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        self.__class__.count += 1

    def add_to_genres(self):
        cls = self.__class__
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)

    def add_to_artists(self):
        cls = self.__class__
        if self.artist not in cls.artists:
            cls.artists.append(self.artist)

    def add_to_genre_count(self):
        cls = self.__class__
        cls.genre_count[self.genre] = cls.genre_count.get(self.genre, 0) + 1

    def add_to_artist_count(self):
        cls = self.__class__
        cls.artist_count[self.artist] = cls.artist_count.get(self.artist, 0) + 1
