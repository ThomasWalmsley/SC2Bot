#Controller controls all managers

class controller():
    clients = []
    def __init__(self):
        pass
    async def on_step(self):
        if not self.clients:
            return
        else: 
            for client in self.clients:
                await client.on_step()

    def send_request(self,message): 
        print(message)
    def process_request(self):
        pass
    def assign_client(self,client):
        self.clients.append(client)