import os


def set_google_credentials(credential_path: str):
    if os.path.exists(credential_path):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
        os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    else:
        print("Sorry! File doesn't exist, pls check the path")