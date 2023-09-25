from src.implemented import youtube, str_json, dump_json
from typing import Any, Optional, Dict


class Channel:
    """Класс для ютуб-канала"""
    __youtube_api = youtube

    def __init__(self, channel_id: str) -> None:
        self._channel_id = channel_id
        self._channel = self.__youtube_api.channels().list(id=channel_id, part='snippet,statistics').execute()

    def __get_items(self) -> Optional[Dict]:
        return self._channel.get("items")[0]

    def __get_snippet(self) -> Optional[Dict]:
        return self.__get_items().get("snippet")

    def __get_statistics(self) -> Optional[Dict]:
        return self.__get_items().get("statistics")

    @property
    def channel_id(self):
        return self._channel_id

    @property
    def title(self) -> str:
        return self.__get_snippet().get("title")

    @property
    def description(self):
        return self.__get_snippet().get("description")

    @property
    def url(self) -> str:
        return f"https://www.youtube.com/channel/{self._channel_id}"

    @property
    def subscriber_count(self):
        return self.__get_statistics().get("subscriberCount")

    @property
    def video_count(self):
        return self.__get_statistics().get("videoCount")

    @property
    def total_view_count(self):
        return self.__get_statistics().get("viewCount")

    def print_info(self) -> None:
        print(str_json(self._channel))

    @classmethod
    def get_service(cls) -> Any:
        return cls.__youtube_api

    def to_json(self, fp) -> None:
        with open(fp, 'w', encoding='utf-8') as f:
            dump_json(self._channel, f)
