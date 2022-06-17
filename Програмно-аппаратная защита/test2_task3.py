class Role:
    def __init__(self, permissions):
        # на вход permission передаём словарь, где ключ это название права, 
        # а значение - логическая переенная, обозначающая разрешение или запрет
        self.permission = permissions

    def check_allow(self, rule):
        return self.permission[rule]
    

roles = {
"admin": Role({
    "read": True,
    "write": True,
    "execute": True,
    "add_user": True,
    "assign_role": True
}),
"moderator": Role({
    "read": True,
    "write": True,
    "execute": True,
    "add_user": False,
    "assign_role": False
}),
"writer": Role({
    "read": True,
    "write": True,
    "execute": False,
    "add_user": False,
    "assign_role": False
}),
"reder": Role({
    "read": True,
    "write": False,
    "execute": False,
    "add_user": False,
    "assign_role": False
}),
"null": Role({
    "read": False,
    "write": False,
    "execute": False,
    "add_user": False,
    "assign_role": False
})
}


class User:
    def __init__(self, role):
        self.role = roles[role]
        # другие атрибуты пользователя

user = User("reader")

# теперь если пользователь отправил запрос, например, на запись файла, 
# можно просто с помощью ветвления обратиться к роли пользователя

if user.role.check_allow("write"):
    pass
    # выполняем запрос на запись ...
