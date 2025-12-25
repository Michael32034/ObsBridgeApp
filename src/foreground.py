from plyer import notification
from jnius import autoclass
from time import sleep


def main():
    # Notification для foreground service
    notification.notify(
        app_name="ObsBridgeApp",
        title="ObsBridgeApp Service",
        message="Сервіс працює у фоні",
        timeout=5,
    )
    print("#Java service run")
    java_service = autoclass("org.obsbridge.Bridge")
    java_service.run()


print("#Service runned")
if __name__ == "__main__":
    main()
