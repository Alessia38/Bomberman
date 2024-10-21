import json

with open('C:/Users/Jerem/OneDrive/Bureau/python-course/course/user.json') as f:
    user_data = f.read()
    user_json_dict = json.loads(user_data)

    print(user_json_dict['age'])
    print(user_json_dict['hobbies'][1])
    print(user_json_dict['email'])