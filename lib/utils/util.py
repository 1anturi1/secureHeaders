# coding: utf-8
import csv

from pathlib import Path
from dotenv import load_dotenv


def load_env_config():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path,
                verbose=True,
                override=False)
