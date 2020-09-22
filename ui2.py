import uiautomator2 as u2

class Douyin:
    def __init__(self,appName='抖音',appPkgName='com.ss.android.ugc.aweme',serial='FJH7N19114001942'):
        self.d = u2.connect_usb(serial)
        print("正在启动app:" + appName + "...")
        print(appName + "包名:" + appPkgName)
        self.d.app_start(appPkgName)
        self.d.sleep(3)
    def skip(self):
        print("跳过广告...")
        self.d(resourceId="com.android.systemui:id/clock").click_exists(timeout=7)
    def start_run(self):
        self.skip()
        self.d.sleep(3)
        print("开始向上滑动...")
        for i in range(5):
            i = i+1
            print("第 %d 条视频..." % i)
            self.d.sleep(3)
            self.d.swipe(0.5, 0.85, 0.5, 0.15)
        print("结束!")

if __name__ == '__main__':
    douyin = Douyin()
    douyin.start_run()