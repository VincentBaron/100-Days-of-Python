import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

email = ""
password = ""
phone = ""
chrome_driver_path = "/Users/vincentbaron/dev/chromedriver"

LOGIN_URL = "https://www.linkedin.com/login"
# job listings to look at, includes position and location
JOBS_URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=105015875&keywords=python%20developer&location=France"


def login():
    """Accepts cookies and logs in to the site."""
    driver.get(url=LOGIN_URL)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-global-alert-container"]/div[1]/section/div/div[2]/button[2]')\
        .click()
    driver.find_element_by_id("username").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("password").submit()


def get_job_urls():
    driver.get(url=JOBS_URL)
    time.sleep(2)
    jobs = driver.find_elements_by_class_name("job-card-container__link")
    job_url_list = []
    for job in jobs:
        job_url = job.get_attribute("href")
        # skip the company links and duplicates
        if job_url.find("www.linkedin.com/jobs/view/") >= 0 and job_url not in job_url_list:
            job_url_list.append(job_url)
    return job_url_list


def apply_to_job(link):
    driver.get(url=link)
    time.sleep(2)
    driver.find_element_by_class_name("jobs-apply-button").click()
    time.sleep(1)
    button = driver.find_element_by_css_selector("footer button")
    if button.text == "Submit application":
        driver.find_element_by_class_name("fb-single-line-text__input").send_keys(phone)
        print(f"*** Pretending to click on the \"{button.text}\" button. ***")
    else:
        print(f"One-step application is not possible for this job.")

driver = webdriver.Chrome(executable_path=chrome_driver_path)

login()

time.sleep(3)

url_list = get_job_urls()
if len(url_list) == 0:
    print("No jobs found.\nMake sure you're logged in properly or tweak the position or location name.")

# try to apply to each job
for url in url_list:
    try:
        apply_to_job(url)
    except NoSuchElementException:
        continue
    time.sleep(5)

# close the browser window
driver.close()









# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# import time
#
#
# chrome_driver_path = "/Users/vincentbaron/dev/chromedriver"
# email = "vbaron@student.42.fr"
# password = "vincent3004"
# phone = "0695143200"
#
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=105015875&keywords=python%20developer&location=France")
#
# time.sleep(2)
# test = driver.find_element_by_link_text("Sign in")
# test.click()
#
# time.sleep(5)
# input = driver.find_element_by_xpath('//*[@id="username"]')
# input.send_keys(email)
# input = driver.find_element_by_xpath('//*[@id="password"]')
# input.send_keys(password)
# input.send_keys(Keys.ENTER)
#
# time.sleep(5)
# all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
#
# for listing in all_listings:
#     print("called")
#     listing.click()
#     time.sleep(2)
#
#     # Try to locate the apply button, if can't locate then skip the job.
#     try:
#         apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
#         apply_button.click()
#         time.sleep(5)
#
#         # If phone field is empty, then fill your phone number.
#         phone = driver.find_element_by_class_name("fb-single-line-text__input")
#         if phone.text == "":
#             phone.send_keys(phone)
#
#         submit_button = driver.find_element_by_css_selector("footer button")
#
#         # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#             close_button.click()
#             time.sleep(2)
#             discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
#             discard_button.click()
#             print("Complex application, skipped.")
#             continue
#         else:
#             submit_button.click()
#
#         # Once application completed, close the pop-up window.
#         time.sleep(2)
#         close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#         close_button.click()
#
#     # If already applied to job or job is no longer accepting applications, then skip.
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue
#
# time.sleep(5)
# driver.quit()