from src.implemented import youtube


class Video:

    __youtube_api = youtube

    def __init__(self, video_id):
        self._video_id = video_id
        self._video = self.__youtube_api.videos().list(id=video_id, part='snippet,contentDetails,''statistics,status').execute()

    def __str__(self):
        return self.title

    def __get_items(self):
        return self._video.get("items")[0]

    def __get_snippet(self) -> dict | None:
        return self.__get_items().get('snippet')

    def __get_statistics(self) -> dict | None:
        return self.__get_items().get('statistics')

    def __get_content_details(self) -> dict | None:
        return self.__get_items().get('contentDetails')
    
    @property
    def id(self):
        return self._video_id
    
    @property
    def title(self):
        return self.__get_snippet().get('title')

    @property
    def link(self):
        return f"https://www.youtube.com/watch?v={self._video_id}"
    
    @property
    def views_count(self):
        return self.__get_statistics().get('viewCount')

    @property
    def likes_count(self):
        return self.__get_statistics().get('likeCount')


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self._playlist_id = playlist_id
