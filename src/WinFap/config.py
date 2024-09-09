

import configparser

# default parameter
DEFAULT_LOGGING_CONFIG = {
    'path':     '.',
    'rotation': '1',  # 1 day
    'size':     '5MB',  # 5 Megabyte
    'level':    'INFO'
}

class LoggingConfig(object):
    path = r".\WinFap.log"
    rotation = 1
    size = "5MB"
    level = "INFO"


class DefaultConfig(object):
    logging = LoggingConfig()


def init_config() -> DefaultConfig:
    # Erstellen einer Default-Config-Instanz
    config = DefaultConfig()
    parser = configparser.ConfigParser()

    # INI-Datei einlesen
    parser.read('config.ini')

    # Iterieren durch die DefaultConfig-Attribute
    for section in config.__dict__:
        if section in parser:  # Wenn die Sektion in der INI-Datei existiert
            section_obj = getattr(config, section)
            for option in section_obj.__dict__:  # Iterieren durch die Optionen der Sektion
                if parser.has_option(section, option):
                    setattr(section_obj, option, parser.get(section, option))

    return config
