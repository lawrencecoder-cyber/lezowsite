const socket = new WebSocket("ws://" + window.location.host + "/ws/stocks/");

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);

    if (data.type === "stock.price_update") {
        const symbol = data.data.symbol;

        const el = document.getElementById("stock-" + symbol);

        if (el) {
            el.innerHTML = `
                <strong>${symbol}</strong>
                <p>$${data.data.price}</p>
                <p>${data.data.percent_change}%</p>
            `;
        }
    }
};



const socket = new WebSocket("ws://" + window.location.host + "/ws/stocks/");

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);

    const row = document.querySelector(`#stock-${data.symbol}`);

    if (row) {
        row.querySelector(".price").innerText = data.price;
        row.querySelector(".change").innerText = data.change;
        row.querySelector(".percent").innerText = data.percent;
    }
};
