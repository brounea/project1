# Start a Selenium Webdriver session.
# Navigate to web interface URL using an existing user id.
# Check that the user name element is showing (web element exists).
# Print user name (using locator).

from selenium import webdriver

def fe_test(uid):
    driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
    driver.get("http://127.0.0.1:5001/users/get_user_data/" + str(uid))
    head1 = driver.find_element_by_tag_name('H1')
    return head1

driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
#driver.implicitly_wait(5) # wait upto 10 sec to find_element(s) functions
# # functions get - load a new webpage in the current browser window
driver.get("http://127.0.0.1:5001/users/get_user_data/1")
head1 = driver.find_element_by_tag_name('H1')
print(head1.text)

