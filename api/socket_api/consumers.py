import json
from channels.generic.websocket import AsyncWebsocketConsumer


class LeaderboardConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session_id = None
        self.group_name = None

    async def connect(self):
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        self.group_name = f'quiz_session_{self.session_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        score = data['score']

        # Gửi thông tin cập nhật đến tất cả các client trong nhóm
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_leaderboard_update',
                'user_id': user_id,
                'score': score
            }
        )

    async def send_leaderboard_update(self, event):
        user_id = event['user_id']
        score = event['score']

        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'score': score
        }))
