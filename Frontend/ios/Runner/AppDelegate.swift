import UIKit
import Flutter
import Firebase

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
    override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    
    ) -> Bool {
        GMSServices.provideAPIKey("AIzaSyDoc4emFcd-TsH2ercuuMzmnn_6_y1M8fk")
        GeneratedPluginRegistrant.register(with: self)
        if #available(iOS 10.0, *) {
        UNUserNotificationCenter.current().delegate = self as? UNUserNotificationCenterDelegate
    }   

//        FirebaseApp.configure()
            
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }
    
}
