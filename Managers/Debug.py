class debug():
    top_display = [] #store the lines to be displayed in the top left
    def __init__(self,manager,client):
        self.manager = manager
        self.client = client

    async def on_step(self):
        await self.display_default_lines()
        for i in range(len(self.top_display)):
            line = self.top_display[i]
            position = [0,0.02*i]
            self.client.debug_text_screen(line,position,color=None,size=16)
        self.top_display = []#reset display

    async def display_default_lines(self):
        #default display
        self.top_display.append("Debug Information")
        self.top_display.append("Testing testing") 

    async def display_line(self,line):
        self.top_display.append(line)