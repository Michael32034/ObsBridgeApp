package org.obsbridge;

import android.app.PendingIntent;
import android.hardware.usb.UsbDevice;
import android.hardware.usb.UsbManager;
import android.util.Log;
import java.util.HashMap;
// import android.hardware.camera2.CameraManager;
// import android.hardware.usb.UsbConstants;
// import android.hardware.usb.UsbEndpoint;
// import android.hardware.usb.UsbInterface;
// import q

public class Bridge {
  private static final String TAG = "MyActivity";
  public static void run() {
    Log.d(TAG, "#ObsBridgeApp running");

    Log.d(TAG, "#Connecting to computer");
    UsbManager usbManager = (UsbManager)getSystemService(Context.USB_SERVICE);

    HashMap<String, UsbDevice> connectedDevices = usbManager.getDeviceList();

    for (UsbDevice device : connectedDevices.values()) {
      Log.d(TAG, "#UsbDevice: " + device.getDeviceName());
    }
    /*
    PendingIntent permissionIntent = PendingIntent.getBroadcast(
        this, 0, new Intent(ACTION_USB_PERMISSION), 0);
    usbManager.requestPermission(device, permissionIntent);
    */
  }
}
