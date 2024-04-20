class MusicPlayer:
    def play_music(self, file_name):
        print(f"Playing music from {file_name}")

class AdvancedMusicPlayer:
    def play_sound(self, track):
        print(f"Playing sound from {track}")

class MusicPlayerAdapter(MusicPlayer):
    def __init__(self, advanced_player):
        self.advanced_player = advanced_player

    def play_music(self, file_name):
        if file_name:  # Перевірка, що рядок не порожній
            self.advanced_player.play_sound(file_name)

def main():
    player = MusicPlayer()
    player.play_music("file.mp3")

    advanced_player = AdvancedMusicPlayer()
    adapted_player = MusicPlayerAdapter(advanced_player)
    adapted_player.play_music("file.mp3")

main()
