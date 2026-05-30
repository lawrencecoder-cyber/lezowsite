document.body.addEventListener("htmx:afterSwap", function (evt) {
    console.log("UI updated:", evt.target);
});
