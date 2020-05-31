from server import Server
from config import api_token

server_sunday = Server(api_token, 191058276, "Sunday")

server_sunday.mainloop()
