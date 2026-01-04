package org.obsbridge;

// import android.hardware.camera2.CameraManager;
// import android.app.PendingIntent;
import android.content.Context;
import android.hardware.usb.UsbDevice;
import android.hardware.usb.UsbManager;
import android.util.Log;
import java.util.HashMap;
// import android.hardware.usb.UsbConstants;
// import android.hardware.usb.UsbEndpoint;
// import android.hardware.usb.UsbInterface;

public class Bridge {
  private static final String TAG = "ObsBridgeApp";
  public Bridge() {
    Log.d(TAG, "Initialize");
    UsbManager this.usbManager = getSystemService(Context.USB_SERVICE);

    HashMap<String, UsbDevice> connectedDevices =
        this.usbManager.getDeviceList();

    for (UsbDevice device : connectedDevices.values()) {
      Log.d(TAG, "#UsbDevice: " + device.getDeviceName());
    };
  }
  public void connect() {}
  public int get_cadr() {}
  public void send_cadr(int i) {}
  public static void run() {
    /* Main func
     * Entry point
     */
    Log.d(TAG, "Java is running");

    Bridge main = new Bridge();
    main.connect();
    int i = 1;
    while (i < 7) {
      i = i + 1;
      main.send_cadr(main.get_cadr());
    };
  }
}
