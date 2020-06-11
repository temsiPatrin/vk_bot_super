from server import Server
from server_key import ServerKey
from config import api_token

server_sunday = ServerKey(api_token, 191058276, "Sunday")

server_sunday.mainloop()
