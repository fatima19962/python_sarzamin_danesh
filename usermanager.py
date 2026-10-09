class UserManager:
    def __init__(self):
        self.Online_users=set()
        self.banned_users=set()

    def user_login(self,user_id):
        if user_id in self.banned_users:
            print(f"user can't login to system")
            txt_log=f"user {user_id} can't login to system"
            return False
        self.Online_users.add(user_id)
        txt_login=print(f"user {user_id} logged in")
        return True
    def checkUsernamePassword(self,userName,password):
        get_user_id=None
        self.user_login(get_user_id)

    def user_logout(self,user_id):
        if user_id in self.Online_users:
            self.Online_users.remove(user_id)
            print(f"user {user_id} logged out")
        else:
            print(f"user {user_id} is not logged in")
    def ban_user(self,user_id):
        self.banned_users.add(user_id)
        if user_id in self.Online_users:
            self.Online_users.remove(user_id)
            txt_log=f"user{user_id} is banned and logout"
            print(txt_log)
    def status_user(self,user_id):
        if user_id in self.Online_users:
            print('islog')
        else:
            print('isnot login')
manager=UserManager()
manager.user_login(1004)
manager.ban_user(1004)

