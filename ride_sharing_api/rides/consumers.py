import json
from channels.generic.websocket import AsyncWebsocketConsumer


class RideTrackingConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        try:
            # Get ride id from URL
            self.ride_id = self.scope["url_route"]["kwargs"]["ride_id"]
            self.group_name = f"ride_{self.ride_id}"

            # Join group
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )

            await self.accept()

        except Exception as e:
            print("WebSocket connect error:", e)
            await self.close()

    async def disconnect(self, close_code):
        # Prevent crash if group_name not set
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

    async def send_location(self, event):
        await self.send(
            text_data=json.dumps({
                "latitude": event["latitude"],
                "longitude": event["longitude"],
            })
        )
