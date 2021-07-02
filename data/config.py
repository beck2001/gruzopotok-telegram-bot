from environs import Env

# create instance of Env class
env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
ADMINS = env.list("ADMINS")

