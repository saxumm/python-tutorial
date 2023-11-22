from user import User
from post import Post
app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James Bond", "goldeneye", "007")
app_user_two.get_user_info()

newpost = Post("on a secret miwsion", app_user_two.name)
newpost.get_post_info()
