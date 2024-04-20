import unittest
from unittest.mock import patch
from Lab2 import MusicPlayer, AdvancedMusicPlayer, MusicPlayerAdapter

class TestMusicPlayerAdapter(unittest.TestCase):
    @patch('builtins.print')
    def test_empty_file_name(self, mock_print):
        advanced_player = AdvancedMusicPlayer()
        adapter = MusicPlayerAdapter(advanced_player)
        adapter.play_music("")
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_different_file_formats(self, mock_print):
        advanced_player = AdvancedMusicPlayer()
        adapter = MusicPlayerAdapter(advanced_player)
        files = ["song.mp3", "song.ogg", "song.wav"]
        for file in files:
            adapter.play_music(file)
            mock_print.assert_called_with(f"Playing sound from {file}")

    @patch('builtins.print')
    def test_adapter_plays_music(self, mock_print):
        advanced_player = AdvancedMusicPlayer()
        adapter = MusicPlayerAdapter(advanced_player)
        adapter.play_music("test_track.mp3")
        mock_print.assert_called_with("Playing sound from test_track.mp3")

    @patch('builtins.print')
    def test_different_input_formats(self, mock_print):
        advanced_player = AdvancedMusicPlayer()
        adapter = MusicPlayerAdapter(advanced_player)
        test_files = ["song.mp3", "track.wav", "sample.ogg"]
        for file in test_files:
            adapter.play_music(file)
        calls = [unittest.mock.call(f"Playing sound from {file}") for file in test_files]
        mock_print.assert_has_calls(calls, any_order=True)

    @patch('builtins.print')
    def test_no_unwanted_calls(self, mock_print):
        advanced_player = AdvancedMusicPlayer()
        adapter = MusicPlayerAdapter(advanced_player)
        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
