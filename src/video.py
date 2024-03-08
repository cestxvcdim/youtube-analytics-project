from src.implemented import youtube


class Video:

    __youtube_api = youtube

    def __init__(self, video_id: str) -> None:
        self._video_id = video_id
        self._video = self.__youtube_api.videos().list(id=video_id, part='snippet,contentDetails,''statistics,status').execute()

    def __str__(self) -> str:
        return self.title

    def __get_items(self) -> dict | None:
        return self._video.get("items")[0]

    def __get_snippet(self) -> dict | None:
        return self.__get_items().get('snippet')

    def __get_statistics(self) -> dict | None:
        return self.__get_items().get('statistics')

    def __get_content_details(self) -> dict | None:
        return self.__get_items().get('contentDetails')
    
    @property
    def id(self) -> str:
        return self._video_id
    
    @property
    def title(self) -> str | None:
        try:
            value = self.__get_snippet().get('title')
        except:
            return None
        else:
            return value

    @property
    def link(self) -> str | None:
        try:
            value = f"https://www.youtube.com/watch?v={self.id}"
        except:
            return None
        else:
            return value
    
    @property
    def views_count(self) -> str | None:
        try:
            value = self.__get_statistics().get('viewCount')
        except:
            return None
        else:
            return value

    @property
    def likes_count(self) -> str | None:
        try:
            value = self.__get_statistics().get('likeCount')
        except:
            return None
        else:
            return value

    @property
    def duration(self) -> str | None:
        try:
            value = self.__get_content_details().get('duration')
        except:
            return None
        else:
            return value


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self._playlist_id = playlist_id
