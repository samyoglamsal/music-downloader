browser.runtime.onMessage.addListener((data, sender, sendResponse) => {
    console.log(data);
    if (data.action === "download") {
        console.log("Downloading song...");

        browser.tabs.query({ currentWindow: true, active: true })
            .then((tabs) => {
                const url = tabs[0].url.split("&")[0];
                data.url = url;
                console.log(data);

                const response = fetch("http://localhost:5000/download-song", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    }, 
                    body: JSON.stringify(data),
                });

                setTimeout(() => sendResponse({response: response}), 1000);
            })
            .catch((error) => {
                console.log(error);
            });
    }

    return true;
});