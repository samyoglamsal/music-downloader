window.addEventListener("load", () => {
    let form = document.getElementById("form");
    form.addEventListener("submit", onSubmit);
});

async function onSubmit() {
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