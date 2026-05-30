import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = "stocks"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )

        await self.accept()

    async def stock_message(self, event):
        await self.send(text_data=json.dumps(event["data"]))
