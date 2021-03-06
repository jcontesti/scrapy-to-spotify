"""Class that represents a song that has been extracted from any source."""
from typing import List


class ExtractedSong:
    """Class that represents an song that has been extracted from any source."""

    ARTISTS_SEPARATORS = [
        ' & ',
        ' ft ',
        ' ft. ',
        ' feat ',
        ' feat. ',
        ' presents ',
        ' pres. ',
        ' with ',
        ' and ',
        ', ',
    ]

    SONGS_TITLES_SEPARATORS = [
        '/',
        ' - ',
    ]

    def __init__(self,
                 artist: str,
                 song_title: str,
                 album_title: str = "",
                 label: str = "") -> None:
        self._artist = artist
        self._song_title = song_title
        self._album_title = album_title
        self._label = label

    @property
    def artist(self) -> str:
        """Return the artist text."""
        return self._artist

    @property
    def song_title(self) -> str:
        """Return the title text."""
        return self._song_title

    @property
    def album_title(self) -> str:
        """Return the album name."""
        return self._album_title

    @property
    def label(self) -> str:
        """Return the label of the song."""
        return self._label

    def get_separated_artists(self) -> List[str]:
        """
        Split artists names into a list.

        For instance "Artist A feat. Artist B" returns ["Artist A", "Artist B"].

        :return: list of artists related to the song.
        """

        replaced_artists = self._artist
        for separator in self.ARTISTS_SEPARATORS:
            replaced_artists = replaced_artists.replace(separator, "#")

        if "#" in replaced_artists:
            separated_artists = replaced_artists.split("#")
        else:
            separated_artists = [replaced_artists]

        return separated_artists

    def get_separated_titles(self) -> List[str]:
        """
        Split songs titles into a list.

        For instance "Song 1 / Song 2" returns ["Song 1", "Song 2"].

        :return: list of different titles related to the extracted song.
        """

        replaced_song_titles = self._song_title
        for separator in self.SONGS_TITLES_SEPARATORS:
            replaced_song_titles = replaced_song_titles.replace(separator, "#")

        if "#" in replaced_song_titles:
            separated_song_titles = replaced_song_titles.split("#")
        else:
            separated_song_titles = [replaced_song_titles]

        return separated_song_titles

    def format(self) -> None:
        """Format artists, titles and label."""
        self._artist = self._artist.lower().strip(" \t\n\r")
        self._song_title = self._song_title.lower().strip(" \t\n\r")
        self._album_title = self._album_title.lower().strip(" \t\n\r")
        self._label = self._label.lower().strip(" \t\n\r")
