# Google Contacts Random Selector

This program allows the user to authenticate with their Google account and retrieve a list of their Google Contacts. The program then generates 5 random contacts from the list and displays them in a GUI window.

## Prerequisites

-   Python 3.x
-   tkinter
-   google-auth
-   google-auth-oauthlib
-   google-auth-httplib2
-   google-api-python-client

## Installation

1.  Clone the repository or download the source code as a zip file and extract it.
2.  Install the required packages by running `pip install -r requirements.txt` in the command prompt.
3.  Download the `credentials.json` file from your [Google Cloud Console](https://console.developers.google.com/apis/credentials).
4.  Place the `credentials.json` file in the same directory as the source code.
5.  Run the program by executing the `python launch_app.py` file.

## Usage

1.  Upon running the program, a GUI window will appear.
2.  Click the "Refresh" button to authenticate with your Google account and retrieve your Google Contacts.
3.  The program will generate 5 random contacts from your Google Contacts list and display them in the GUI window.
4.  To log out, close the GUI window and delete the `token.json` file that was created in the same directory as the source code.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
