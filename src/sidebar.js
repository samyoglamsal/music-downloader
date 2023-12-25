window.addEventListener("load", () => {
    const form = document.getElementById("form");
    form.addEventListener("submit", event => onSubmit(event));
});

async function onSubmit(event) {
    // Prevents the page from reloading after hitting submit -- caused many headaches
    event.preventDefault();

    const tabs = await browser.tabs.query({ currentWindow: true, active: true });
    const artist = document.getElementById("artist").value;
    const title = document.getElementById("title").value;
    const date_added = (new Date()).toISOString().split("T")[0];
    const url = tabs[0].url.split("&")[0];

    const body = {
        artist: artist,
        title: title,
        date_added: date_added,
        url: url
    };

    const response = await fetch("http://localhost:5000/download-song", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body)
    });

    console.log(response.json());
}