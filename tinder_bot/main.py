import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

chrome_driver_path = "/Users/vincentbaron/dev/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
email = ""
password = ""
tinder_url = "https://tinder.com/"
tinder_home_url = "https://tinder.com/app/recs"
facebook_login_url = "https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1615025204790%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df213d1d1af154b8%2526domain%253Dtinder.com%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff2a7a71d356b54c%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_GB%26logger_id%3Df37fcdc2dbd9398%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df7272459f9dcec%2526domain%253Dtinder.com%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff2a7a71d356b54c%2526relation%253Dopener%2526frame%253Df3d050694b22c94%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df7272459f9dcec%26domain%3Dtinder.com%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff2a7a71d356b54c%26relation%3Dopener%26frame%3Df3d050694b22c94%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0"


def login():
    driver.get(tinder_url)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
    time.sleep(2)
    window_login = driver.window_handles[0]
    window_fb = driver.window_handles[1]
    driver.switch_to.window(window_fb)
    time.sleep(2)
    # driver.get(facebook_login_url)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    time.sleep(2)
    driver.switch_to.window(window_login)
    time.sleep(5)


def tinder_swiping():
    # Allow location
    driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]').click()
    time.sleep(2)
    # Allow notifications
    driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]').click()
    time.sleep(5)
    # swipe!
    for a in range(20):

        time.sleep(1)
        try:
            print("called")
            like_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
            like_button.click()

            # Catches the cases where  there is a "Matched" pop-up in front of the "Like" button:
        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element_by_css_selector(".itsAMatch a")
                match_popup.click()

            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
            except NoSuchElementException:
                try:
                    home_screen = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[2]/button[2]')
                    home_screen.click()
                except NoSuchElementException:
                    try:
                        super_like = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/button[2]')
                        super_like.click()
                    except NoSuchElementException:
                        continue
                    continue
                time.sleep(2)





        # try:
        #     like_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        #     if like_button:
        #         like_button.click()
        #         time.sleep(2)
        #     else:
        #         driver.get("https://tinder.com/")
        #         time.sleep(5)
        # except NoSuchElementException:
        #     time.sleep(2)
        #     continue


# not interested //*[@id="t-1222506740"]/div/div/div[2]/button[2]

login()
tinder_swiping()
time.sleep(4)
driver.close()