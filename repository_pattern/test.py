from repository_pattern.user_repository import User

if __name__ == "__main__":
    _user = User(**{"_id": '001', 'userId': "user001", 'name': 'amit', 'email': '7jdeep@gmail.com'})
    _user.add(_user.__dict__)

    print(_user.get("001"))

    _user.name = "Jagdeep"
    _user.update(_user._id, _user.__dict__)

    print(_user.get("001"))

    _user = User(**{"_id": '002', 'userId': "user002", 'name': 'zishan', 'email': 'zkkhan@gmail.com'})
    _user.add(_user.__dict__)

    print(User.get_all())






