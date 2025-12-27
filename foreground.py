print("lokrestts")
import logging
from jnius import autoclass
from time import sleep
from kivy.logger import Logger

def main():
    # Notification для foreground service
    Logger.info("Transfering: Java service run")
    java_service = autoclass("org.obsbridge.Bridge")
    java_service.run()


Logger.info("Transferring: Service runned")
if __name__ == "__main__":
    main()
