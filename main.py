from kivy.graphics import Canvas, Color
from android import mActivity
from jnius import autoclass, cast
from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from android_notify import Notification


class TransferingService:
    java_class = "io.github.michael32034.obsbridgeapp.ServiceTransfering"

    def start(self) -> None:
        BuildVersion = autoclass("android.os.Build$VERSION")
        ServiceInfo = autoclass("android.content.pm.ServiceInfo")
        PythonService = autoclass("org.kivy.android.PythonService")

        self.main_class = autoclass(self.java_class)
        self.main_class.start()
        self.main_service = self.main_class.mService
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

        self.main.startForeground(n.id, builder.build(), foreground_type)

    def check(self) -> bool:
        context = mActivity.getApplicationContext()
        manager = cast(
            "android.app.ActivityManager",
            mActivity.getSystemService(context.ACTIVITY_SERVICE),
        )
        for service in manager.getRunningServices(100):
            Logger.debug("AFS: Class '" + service.service.getClassName() + "'")
            if service.service.getClassName() == self.java_class:
                return True
        return False

    def stop(self):
        self.main.stopSelf()


class MyApp(App):
    # Запущений процес чи ні
    started = False

    def build(self):
        # Screen Layout
        self.main = BoxLayout(orientation="vertical")
        self.main.canvas = Canvas()
        self.main.canvas.add(Color(0.32, 0.26, 0.59))

        self.top_l_void = Widget()
        self.bottom_l_void = Widget()
        self.header = Label(text="ObsBridgeApp", font_size="78px")
        self.text = Label(
            text="App for emulating webcam \n Connect phone to computer",
            font_size="30px",
        )
        self.status = BoxLayout()
        self.status_label = Label(
            text="[color=#9B9B9B]Connection status[/color]", markup=True
        )
        self.status_button = Button(
            text="Connect", size_hint=(0.25, 1), on_press=self.click_button
        )
        self.bottom_void = Widget()

        self.status.add_widget(self.status_label)
        self.status.add_widget(self.status_button)
        self.main.add_widget(self.top_l_void)
        self.main.add_widget(self.header)
        self.main.add_widget(self.bottom_l_void)
        self.main.add_widget(self.text)
        self.main.add_widget(self.status)
        self.main.add_widget(self.bottom_void)

        self.transfering = TransferingService()

        return self.main

    def click_button(self, _):
        Logger.info("Button clicked")
        if self.started:
            self.status_button.text = "Start"
        else:
            self.transfering.start()
            self.status_button.text = "Don't resolved"
            self.status_button.disabled = True
            self.status_label.text = "[color=#4293FF]Waiting[/color]"
            Clock.schedule_interval(self.check_connection, 0.5)

    def check_connection(self):
        self.status_label.text = "[color=#4293FF]Waiting[/color]"
        status = False

        service_name = self.transfering_procces_name
        context = mActivity.getApplicationContext()
        manager = cast(
            "android.app.ActivityManager",
            mActivity.getSystemService(context.ACTIVITY_SERVICE),
        )
        for service in manager.getRunningServices(100):
            if service.service.getClassName() == service_name:
                status = True
                Logger.info("AFS: Class '" + service.service.getClassName() + "'")
        if status:
            self.status_label.text = "[color=#00FF00]Connections active[/color]"
        else:
            self.status_label.text = "[color=#FF0000]Disconnect[/color]"


if __name__ == "__main__":
    MyApp().run()
