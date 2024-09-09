
import logging

from WinFap import config
from WinFap import logger
from WinFap import version


def main():
    app_version = version.get_version()

    # Read ini-file and create configuration object
    config_obj = config.init_config()

    # Config the logging module
    logger.setup_logging(config_obj.logging)

    # Print application start to log-file
    logging.info("*" * 20)
    logging.info("Start WinFap v%s", app_version)
    logging.info("*" * 20)


    logging.debug("Dies ist eine Debug-Nachricht.")
    logging.error("Fehler aufgetreten.")


if __name__ == '__main__':
    main()
