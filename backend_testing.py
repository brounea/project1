import requests
import db_connector

res = requests.post('http://127.0.0.1:5000/users/1', json={"user_name":"John"})
if res.ok:
    print(res.json())
else:
    print(res.json())

print(' Database AFTER POST query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')

res = requests.get('http://127.0.0.1:5000/users/1')
if res.ok:
    print(res.json())
else:
    print(res.status_code)
    print(res.json())

print(' Database AFTER GET query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')

res = requests.put('http://127.0.0.1:5000/users/1', json={"user_name":"John-updated"})
if res.ok:
    print(res.json())
else:
    print(res.status_code)
    print(res.json())

print(' Database AFTER PUT query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')

res = requests.delete('http://127.0.0.1:5000/users/1')
if res.ok:
    print(res.json())
else:
    print(res.status_code)
    print(res.json())
print(' Database AFTER DELETE query found user_name: ' + db_connector.get_user_name(1) + ' For user_id: 1')
