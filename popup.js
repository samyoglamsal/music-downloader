window.addEventListener("load", () => {
    let submitButton = document.getElementById("submit");
    submitButton.addEventListener("click", onClick);
});

async function onClick() {
    const artist = document.getElementById("artist").value;
    const title = document.getElementById("title").value;
    const date_added = (new Date()).toISOString().split("T")[0];

    const response = await browser.runtime.sendMessage({
        action: "download",
        artist: artist,
        title: title,
        date_added: date_added
    })
}