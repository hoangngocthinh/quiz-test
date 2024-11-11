from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def update_leaderboard(session_id, user_id, score):
    channel_layer = get_channel_layer()
    group_name = f'quiz_session_{session_id}'

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_leaderboard_update',
            'user_id': user_id,
            'score': score
        }
    )
