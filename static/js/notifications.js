const socket = new WebSocket(
    "ws://" + window.location.host + "/ws/notifications/"
);

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);

    if (data.type === "price_alert") {
        alert(data.message);
    }
};
