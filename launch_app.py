# Import the required libraries
from tkinter import *
import random, os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# The required scopes for accessing the Google Contacts API
SCOPES = ['https://www.googleapis.com/auth/contacts']

def contacts():
    # Initialize the credentials
    creds = None
    '''
    The file token.json stores the user's access and refresh tokens, and is
    created automatically when the authorization flow completes for the first
    time.
    '''
    # Check if the token.json file exists
    if os.path.exists('token.json'):
        # If token.json exists, use it to create the credentials object
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        # If the credentials have expired, refresh them
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Create an InstalledAppFlow object using the client secrets file
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            
        '''
            reference github: https://github.com/wittyhandle/go-google-contacts-api
            
            following params required for Auth Code:
            
            CLIENT_ID = // used from credentials.json
            REDIRECT_URI = <redirect uri> "http://localhost:42047" // used from credentials.json
            SCOPE = <list of scopes>
            access_type = offline
            response_type = code
        '''
        # Run the local server and retrieve the authorization code
        creds = flow.run_local_server(port=42047) # match port according to redirect uri for localhost
        # Save the credentials for the next run
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Build the People API service
        service = build('people', 'v1', credentials=creds)

        # Call the People API to retrieve the user's connections (contacts)
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=1000,
            pageToken=None,
            sortOrder='FIRST_NAME_ASCENDING',
            personFields='names,emailAddresses').execute()
        
        # Get the list of connections
        connections = results.get('connections', [])
        
        # Clear the listbox
        contact_list.delete(0, END)
        
        # Create a list of all the connections' display names
        all_connections = []
        for person in connections:
            names = person.get('names', [])
            if names:
                name = names[0].get('displayName')
                all_connections.append(name)
        '''
        # Just for testing (Printing 1000 connections to file)
        with open(r'docs.txt', 'w') as fp:
            for item in all_connections:
                # write each item on a new line
                fp.write("%s\n" % item)
            print('Done')
        '''
        
        # Generate 5 random connections
        gen_con = random.sample(all_connections, 5)
        
        # Insert the generated connections into the listbox
        for i in gen_con:
            contact_list.insert(END, i)
    except HttpError as err:
        # If there's an error, print the error message
        print(err)

# Create the GUI window
window = Tk()
window.geometry('300x250')
window.title('Google Contacts')
window.configure(background='white')
window.resizable(0, 0)
window.bell()

# Add a button to refresh the contacts
refresh_button = Button(window, text='Refresh', command=contacts)
refresh_button.pack()

# Add a listbox to display the contacts
contact_list = Listbox(window, width=20,font=('Helvetica', 12), 
                       bg="white", 
                       fg="black", 
                       selectbackground="grey", 
                       selectforeground="white", 
                       justify=CENTER)
contact_list.pack()

def delete_token():
    # Delete the token.json file so that the user can log in again
    os.remove('token.json')
    
# Display the initial set of contacts
delete_token()
contacts()

# Start the GUI event loop
window.mainloop()