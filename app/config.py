from environs import Env

env = Env()
env.read_env()
user = env('user')
password = env('password')
host = env('user')
port = env('port')
database_name = env('database_name')
print(user, password, host, port, database_name)