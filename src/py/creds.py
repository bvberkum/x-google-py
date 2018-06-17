import os
import oauth2client
from oauth2client import client
from oauth2client import tools


CLIENT_SECRET_FILE = 'client_secret.json'
CRED_FILE = os.path.expanduser('~/.credentials/script-blogger.json')


def get_credentials(app_name, secret_file, credential_path, scopes):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(secret_file, scopes)
        flow.user_agent = app_name
        #credentials = tools.run(flow, store)
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials

if __name__ == '__main__':
    if 'GOOGLE_SCRIPT_JSON_SECRET_FILE' in os.environ:
        secret = os.environ['GOOGLE_SCRIPT_JSON_SECRET_FILE']
    else:
        secret = CLIENT_SECRET_FILE
    SCOPES = 'https://www.googleapis.com/auth/blogger'
    credentials = get_credentials('name', secret, CRED_FILE, SCOPES)
