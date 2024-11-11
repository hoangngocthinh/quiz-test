class WebSocketService {
    public socket: WebSocket | null = null;
  
    connect(sessionId: string): void {
      const wsUrl = `${process.env.VITE_WEBSOCKET_URL}/quiz/${sessionId}/leaderboard/`;
      this.socket = new WebSocket(wsUrl);
  
      this.socket.onopen = () => {
        console.log('WebSocket connection established');
      };
  
      this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log('Received data:', data);
      };
  
      this.socket.onclose = () => {
        console.log('WebSocket connection closed');
      };
  
      this.socket.onerror = (error) => {
        console.error('WebSocket error:', error);
      };

    }
  
    send(data: object): void {
      if (this.socket && this.socket.readyState === WebSocket.OPEN) {
        this.socket.send(JSON.stringify(data));
      }
    }
  
    disconnect(): void {
      if (this.socket) {
        this.socket.close();
      }
    }
  }
  
  export default new WebSocketService();
  