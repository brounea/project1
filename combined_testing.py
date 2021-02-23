# The script will:
#  Post any new user data to the REST API using POST method.
#  Submit a GET request to make sure data equals to the posted data.
#  Using pymysql, check posted data was stored inside DB (users table).
#  Start a Selenium Webdriver session.
#  Navigate to web interface URL using the new user id.
#  Check that the user name is correct.
#
# Any failure will throw an exception using the following code: raise Exception("test failed")

import requests
import db_connector
import frontend_testing

input_user_id = 901
input_json = {"user_name":"user-" + str(input_user_id)}

res = requests.post('http://127.0.0.1:5000/users/' + str(input_user_id) , json=input_json)
userj = res.json()
if res.status_code == 200:
    userj = res.json()
    user_posted = userj['user_added']
else:
    raise Exception("test failed")

res = requests.get('http://127.0.0.1:5000/users/' + str(input_user_id))
userj = res.json()
if res.status_code == 200:
    userj = res.json()
    user_get = userj['user_name']
    if user_get != user_posted :
        raise Exception("test failed")
else:
    raise Exception("test failed")

print(' Database AFTER GET query found user_name: ' + db_connector.get_user_name(input_user_id) + ' For user_id: ' + str(input_user_id))

user_fe = frontend_testing.fe_test(input_user_id)

if user_fe != db_connector.get_user_name(input_user_id):
    raise Exception("test failed")