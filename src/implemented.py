import os
import json
from typing import IO, Dict, Any
from dotenv import load_dotenv
from googleapiclient.discovery import build


load_dotenv()

api_key: str = os.getenv('YT_API_KEY')
youtube: Any = build('youtube', 'v3', developerKey=api_key)


def str_json(data: Dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


def dump_json(data: Dict, fp: IO[str]) -> None:
    json.dump(data, fp, indent=2, ensure_ascii=False)
