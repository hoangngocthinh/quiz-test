import redis
from urllib.parse import urlparse
from django.conf import settings


class RedisService:
    def __init__(self, session_id):
        self.urls = urlparse(settings.REDIS_CONN_URL)
        self.client = redis.Redis(host=self.urls.hostname, port=self.urls.port, db=0, password=self.urls.password)
        self.leaderboard_key = f"leaderboard:{session_id}"

    def update_score(self, user_id, score):
        """
        Update score of user in leaderboard
        """
        self.client.zadd(self.leaderboard_key, {user_id: score})

    def get_leaderboard(self, top_n=10):
        """
        Get top n player in leader
        """
        top_users = self.client.zrevrange(self.leaderboard_key, 0, top_n - 1, withscores=True)
        leaderboard = [
            {"user_id": int(user_id), "score": int(score), "rank": index + 1}
            for index, (user_id, score) in enumerate(top_users)
        ]
        return leaderboard

    def get_user_rank_and_score(self, user_id):
        """
        Get rank and score of special user in leaderboard
        """
        score = self.client.zscore(self.leaderboard_key, user_id)
        rank = self.client.zrevrank(self.leaderboard_key, user_id)

        if score is not None and rank is not None:
            return {"user_id": user_id, "score": int(score), "rank": rank + 1}
        else:
            return None

    def clear_leaderboard(self):
        """
        Clear cache for quiz session.
        """
        self.client.delete(self.leaderboard_key)
