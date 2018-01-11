class User:

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.user_id

    def set_id(self, user_id):
        self.user_id = user_id


class Song:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class SongSelector:

    def __init__(self, song):
        self.current_song = song

    def set_song(self, song):
        self.current_song = song

    def get_current_song(self):
        return self.current_song


class PlayList:

    def __init__(self, song, song_list):
        self.song = song
        self.song_list = song_list

    def get_next_song(self):
        return self.song_list[-1]

    def add_to_list(self, song):
        return self.song_list.append(song)


class CD:

    def __init__(self, name):
        self.name = name


class CDPlayer:

    def get_playlist(self):
        return self.play_list

    def set_playlist(self, play_list):
        self.play_list = play_list

    def get_cd(self):
        return self.cd

    def set_cd(self, cd):
        self.cd = cd

    def __init__(self, play_list, cd):
        self.play_list = play_list
        self.cd = cd

    def play_song(self, song):
        print("playing song: %s" % song)


class JukeBox:

    def __init__(self, cd_player, user, cd_collection, song_selector):
        self.cd_player = cd_player
        self.user = user
        self.cd_collection = cd_collection
        self.song_selector = song_selector

    def get_current_song(self):
        return self.song_selector.get_current_song()

    def set_user(self, user):
        self.user = user
