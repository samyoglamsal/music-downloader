# Music Downloader
A Firefox extension that downloads the current YouTube video as a .m4a file.

# Installation
1. Clone this repository.
2. Setup and activate a python virtual environment: `python3 -m venv .venv && . .venv/bin/activate`.
3. Install the required packages with `pip install -r requirements.txt`.

# Running
1. Start the python server by running `flask --app api/app.py run`.
2. Install the browser extension.
    1. Open Firefox and head to `about:debugging`.
    2. On the left hand side, click `This Firefox`.
    3. Click `Load Temporary Add-on` and click any file inside the cloned repository folder.
3. Ensure you have sidebars enabled.
    1. Click the three bars in the top right hand corner.
    2. Select `More tools`.
    3. Select `Customize toolbar`.
    4. Drag the `Sidebars` option into your toolbar.
3. Go to any YouTube video and then click on the sidebar button.
5. Select `Music Downloader` from the dropdown menu and enter the appropriate fields.