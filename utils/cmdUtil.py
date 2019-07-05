import os;
improt time;

adb_a = "adb -a"; #listen on all network interfaces, not just localhost
adb_d = "adb -d"; #use USB device (error if multiple devices connected)
adb_e = "adb -e"; #use TCP/IP device (error if multiple TCP/IP devices available)
adb_s = "adb -s "; #SERIAL   use device with given serial (overrides $ANDROID_SERIAL)
adb_t = "adb -t "; #ID  device with given transport id
adb_h = "adb -H"; #name of adb server host [default=localhost]
adb_p = "adb -P"; #port of adb server [default=5037]
adb_l = "adb -L ";#SOCKET listen on given socket for adb server [default=tcp:localhost:5037]

adb_connect = "adb connect "; #HOST[:PORT] 
adb_disconnect = "adb disconnect "; #HOST[:PORT] 
#adb_forward = "adb forward --list "; #HOST[:PORT] 
#adb_forward = "adb [--no-rebind] LOCAL REMOTE"; #HOST[:PORT] 
#forward --remove LOCAL   remove specific forward socket connection
#forward --remove-all     remove all forward socket connections
#ppp TTY [PARAMETER...]   run PPP over USB
#reverse --list           list all reverse socket connections from device
#reverse [--no-rebind] REMOTE LOCAL
#reverse --remove REMOTE  remove specific reverse socket connection
#reverse --remove-all     remove all reverse socket connections from device
adb_version = "adb version";
adb_logcat = "adb logcat ";
adb_devices = "adb devices"; #  
adb_devices = "adb devices -l"; #  [-l]   list connected devices (-l for long output)
adb_state = "adb get-state";
adb_start = "adb start-server";
adb_kill = "kill-server";
adb_push = "adb push "; #local remote 推送到手机
adb_pull = "adb pull "; #remote local 拉取到当前设备
#adb_sync = "adb sync" [all|data|odm|oem|product|system|vendor]  sync a local build from $ANDROID_PRODUCT_OUT to the device (default all)

#am和pm命令必须先切换到adb shell模式下才能使用

#am   activity manager 启动一个activity，强制停止进程，发送广播进程，修改设备屏幕属性等
adb_am_start = "am start -n ";  # {packageName}/.{activityName}
adb_am_kill = "am kill "; #<packageName>
adb_am_force_stop = "am force-stop "; # <packageName> 强制停止
adb_am_startservice = "am startservice";
adb_am_stopservice = "am stopservice";
adb_version = "adb version";