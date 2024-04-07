from environs import Env

env = Env()
env.read_env()
api_key = env('BOT_TOKEN')
