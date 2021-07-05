from environs import Env

# create instance of Env class
env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
ADMINS = env.list("ADMINS")

# database credentials
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")

POSTGRES_URI = f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

