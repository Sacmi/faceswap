from tqdm import tqdm
from os import listdir
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import threading

class GoogleDriveSync:
    """ Simple PyDrive wrapper for sync model """
    def __init__(self, model_dir, key="gdrive_key"):
        """ Log in to Google Drive account using OAuth key """
        auth = GoogleAuth()
        if key == "gdrive_key":
            message = "Please, get OAuth key and start \"faceswap.py\" with flag -gd <your key>"
            raise GoogleDriveAuthError(
                message)
        try:
            auth.Auth(key)
        except Exception:
            if key == None:
                self.is_activated = False
            else:
                message = "Something wrong with your OAuth key. Try to get new one and restart this script"
                raise GoogleDriveAuthError(
                    message)
        
        self.drive = GoogleDrive(auth)
        self.model_dir = model_dir
        self.is_activated = True

    def upload(self):
        """ Upload model to Google Drive """
        if self.is_activated:
            file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

            for h5file in tqdm(listdir(self.model_dir)):
                for gd_file in file_list:
                    if h5file == gd_file["title"]:
                        file = self.drive.CreateFile({ "id": gd_file["id"] })
                    
                if "file" not in locals() and h5file.endswith(".h5"):
                    file = self.drive.CreateFile({ "title": h5file })

                if "file" in locals():            
                    file.SetContentFile("{}/{}".format(self.model_dir, h5file))
                    file.Upload()

                    del file

    def uploadThread(self, thread_name="Google Sync Thread"):
        """ Create and start thread with upload function """
        thread = threading.Thread(target=self.upload, name=thread_name)
        thread.start()
        return thread

class GoogleDriveAuthError(BaseException):
    pass