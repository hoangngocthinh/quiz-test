<template>
	<div>
		<h2>Leaderboard</h2>
		<ul>
			<li v-for="(user, index) in leaderboard" :key="index">
				{{ user.user_id }} - Score: {{ user.score }}
			</li>
		</ul>
	</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, onUnmounted, reactive } from 'vue';
import WebSocketService from '../services/websocket.service';

export default defineComponent({
	props: {
		sessionId: {
			type: String,
			required: true,
		},
	},
	setup(props) {
		const leaderboard = reactive<any[]>([]);

		const connectWebSocket = () => {
			WebSocketService.connect(props.sessionId);
			if (WebSocketService.socket) {
				WebSocketService.socket.onmessage = (event: MessageEvent) => {
					const data = JSON.parse(event.data);
					leaderboard.splice(0, leaderboard.length, ...data.leaderboard);
				};
			}
		};

		onMounted(() => {
			connectWebSocket();
		});

		onUnmounted(() => {
			WebSocketService.disconnect();
		});

		return {
			leaderboard,
		};
	},
});
</script>

<style scoped>
/* CSS cho component */
</style>
