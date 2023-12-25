window.addEventListener("load", () => {
    const form = document.getElementById("form");
    form.addEventListener("submit", event => onSubmit(event));
});

async function onSubmit(event) {
    // Prevents the page from reloading after hitting submit -- caused many headaches
    event.preventDefault();

    const artistField = document.getElementById("artist");
    const titleField = document.getElementById("title");
    const submitButton = document.getElementById("submit");
    const tabs = await browser.tabs.query({ currentWindow: true, active: true });

    artistField.disabled = true;
    titleField.disabled = true;
    submitButton.disabled = true;

    const body = {
        artist: artistField.value,
        title: titleField.value,
        date_added: new Date().toISOString().split("T")[0],
        url: tabs[0].url.split("&")[0]
    };

    const response = await fetch("http://localhost:5000/download-song", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body)
    });

    console.log(response.json());

    artistField.value = "";
    titleField.value = "";

    artistField.disabled = false;
    titleField.disabled = false;
    submitButton.disabled = false;
}