print("lokrestts")
import logging
from jnius import autoclass
from time import sleep

logging.basicConfig(
    level=logging.CRITICAL, format="%(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("ObsBridgeApp#foreground")


def main():
    # Notification для foreground service
    logger.info("#Java service run")
    java_service = autoclass("org.obsbridge.Bridge")
    java_service.run()


logger.info("#Service runned")
if __name__ == "__main__":
    main()
