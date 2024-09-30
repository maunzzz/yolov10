"""The config module handles reading config.ini file"""
from configparser import ConfigParser
from pathlib import Path
from typing import Optional

config_reader = ConfigParser()
config_reader.read(Path(__file__).absolute().parent / 'config.ini')


def _get_dir(option: str) -> Optional[Path]:
    """Return the directory named `option` under [dirs] in config ini

    If the folder does not exist create it.

    Return:
        Path to option if set, else None.
    """

    if not config_reader.has_section('dirs'):
        return None

    if not config_reader.has_option('dirs', option):
        return None

    path = Path(config_reader.get('dirs', option))

    if not path.exists():
        path.mkdir(parents=True)

    return path


def model_folder():
    return _get_dir('models')


def data_folder():
    return _get_dir('data')
