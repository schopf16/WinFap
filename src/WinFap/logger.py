
import logging

from logging.handlers import RotatingFileHandler

from WinFap import config


def parse_size(size_str):
    """Konvertiert die Größe aus dem Format '5MB', '2GB' etc. in Bytes."""
    size_str = size_str.upper()
    size_map = {'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
    for unit in size_map:
        if size_str.endswith(unit):
            return int(size_str[:-len(unit)]) * size_map[unit]
    return int(size_str)  # Fallback zu Bytes, falls keine Einheit


def setup_logging(log_config: config.LoggingConfig):
    log_file_path = log_config.path
    max_bytes = parse_size(log_config.size)
    backup_count = int(log_config.rotation)

    handler = RotatingFileHandler(log_file_path, maxBytes=max_bytes, backupCount=backup_count)
    logging.basicConfig(level=getattr(logging, log_config.level.upper()),
                        handlers=[handler],
                        format='%(asctime)s - %(name)s - %(levelname)s - \t%(message)s')
