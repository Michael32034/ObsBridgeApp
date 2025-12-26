import logging
from plyer import notification
from jnius import autoclass
from time import sleep

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("ObsBridgeApp#foreground")


def main():
    # Notification для foreground service
    notification.notify(
        app_name="ObsBridgeApp",
        title="ObsBridgeApp Service",
        message="Сервіс працює у фоні",
        timeout=5,
    )
    logger.info("#Java service run")
    java_service = autoclass("org.obsbridge.Bridge")
    java_service.run()


logger.info("#Service runned")
if __name__ == "__main__":
    main()
