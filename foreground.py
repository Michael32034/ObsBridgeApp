print("lokrestts")
from jnius import autoclass
from android import mActivity
from kivy.logger import Logger

from android_notify import Notification


def startForeground():
    Logger.info("Transfering: Start foreground func runs")
    BuildVersion = autoclass("android.os.Build$VERSION")
    ServiceInfo = autoclass("android.content.pm.ServiceInfo")
    main_service = autoclass(
        "io.github.michael32034.obsbridgeapp.ServiceTransfering"
    ).mService
    foreground_type = (
        ServiceInfo.FOREGROUND_SERVICE_TYPE_CAMERA
        | ServiceInfo.FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE
        if BuildVersion.SDK_INT >= 30
        else 0
    )

    n = Notification(
        title="Foreground Service Active",
        message="This service is running in the foreground",
    )
    builder = n.start_building()

    main_service.startForeground(n.id, builder.build(), foreground_type)


def main():
    startForeground()
    # Notification для foreground service
    Logger.info("Transfering: Java sclass run")
    context = mActivity.getApplicationContext()
    java_service = autoclass("org.obsbridge.Bridge")
    java_service.run(context)


Logger.info("Transferring: Service runned")
if __name__ == "__main__":
    main()
