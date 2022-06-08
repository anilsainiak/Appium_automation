

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
default_capabilities={
    'autoGrantPermissions':'true',
    "platformName": "android",
    "appActivity": "com.atg.world.activity.SplashActivity",
    "appWaitDuration": "5000",
    "appExecTimeout": "50000",
    "uiautomator2ServerLaunchTimeout": "50000",
    "uiautomator2ServerInstallTimeout": "50000",
    "appPackage": "com.ATG.World",
    "deviceName": "emulator-5554",
    "driver": "http://localhost:4723/wd/hub"
}
driver=webdriver.Remote(default_capabilities['driver'],default_capabilities)
#print(driver)


def test_LoginWithRightCredential():


    a = driver.find_element(by=AppiumBy.ID,value='com.ATG.World:id/getStartedTv')
    a.click()

    b=driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
    b.click()
    driver.implicitly_wait(5000)

    email = driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.EditText')
    email.send_keys("akssaini1012@gmail.com")

    btn=driver.find_element(by=AppiumBy.ID,value='com.ATG.World:id/signinbutton')
    btn.click()

    driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText').set_text('Anilsaini')

    signin = driver.find_element(by=AppiumBy.ID,value="com.ATG.World:id/passwordloginbutton")
    signin.click()
    print("test_LoginWithRightCredential passed")


def post_img():
    driver.find_element(by=AppiumBy.ID,value='com.ATG.World:id/btnGotit').click()
    driver.find_element(by=AppiumBy.ID,value='com.ATG.World:id/fab').click()
    driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView').click()
    driver.find_element(by=AppiumBy.ID,value='android:id/button1').click()
    driver.find_element(by=AppiumBy.ID,value='com.ATG.World:id/img_clicked_btn').click()
    driver.find_element(by=AppiumBy.ID,value='com.ATG.World:id/toolbar_post_action').click()
    driver.find_element(by=AppiumBy.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]').click()


test_LoginWithRightCredential()
post_img()