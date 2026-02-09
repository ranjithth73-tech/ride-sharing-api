import json
from channels.generic.websocket import AsyncWebsocketConsumer


class RideTrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get ride ID from URL
        user = self.scope["user"]

        if user.is_anonymous:
            await self.close()
            return
        self.ride_id = self.scope["url_route"]["kwargs"]["ride_id"]

        # Create group name
        self.group_name = f"ride_{self.ride_id}"

        # Join group
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        # Accept Connection
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        latitude = data.get("latitude")
        longitude = data.get("longitude")

        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {"type": "send_location", "latitude": latitude, "longitude": longitude},
        )

    async def send_location(self, event):
        # Send data to Websocket client

        await self.send(
            text_data=json.dumps(
                {
                    "latitude": event["latitude"],
                    "longitude": event["longitude"],
                }
            )
        )
