from android import mActivity
from jnius import autoclass, cast
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    # Запущений процес чи ні
    started = False
    connection = False
    transfering_procces_name = "io.github.michael32034.obsbridgeapp.ServiceTransfering"

    def build(self):
        # Screen Layout
        self.main = BoxLayout(orientation="vertical")

        self.top_void = Widget()
        self.header = Label(text="ObsBridgeApp", font_size="25px")
        self.text = Label(
            text="App for emulating webcam \n Connect phone to computer",
            font_size="15px",
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
        self.main.add_widget(self.top_void)
        self.main.add_widget(self.header)
        self.main.add_widget(self.text)
        self.main.add_widget(self.status)
        self.main.add_widget(self.bottom_void)
        return self.main

    def connect(self):
        self.service = autoclass(self.transfering_procces_name)
        mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
        argument = ""
        self.service.start(mActivity, argument)

    def click_button(self, _):
        if self.started:
            self.connect_stop()
            self.status_button.text = "Start"
            self.connection = True
        else:
            self.connect()
            Clock.schedule_interval(self.check_connection, 0.5)
            self.status_button.text = "Stop"
            self.status_label.text = "[color=#4293FF]Waiting[/color]"
            self.connection = True

    def check_connection(self, _):
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
        if status:
            self.status_label.text = "[color=#00FF00]Connections active[/color]"
        else:
            self.status_label.text = "[color=#FF0000]Disconnect[/color]"

    def connection_stop(self):
        self.service.stopSelf()


if __name__ == "__main__":
    MyApp().run()
