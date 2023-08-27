import os
import dropbox

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root , dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path,"rb")as f:
                    dbx.files_upload(f.read(),dropbox_path, mode = WriteMode("overwrite"))

def main():
    access_token = 'sl.BjJ92uUJi0AMdNFqQTU6_8dr4a-9FC6_6GImqDp-uZX_iUIceqRd3IcRkNR3c4vf_LYPTD2aTf5GuO5UV_dazOGEW90_9JD0byQbc9nrW_B2CES6kxXtZ0PMdzi1AR_q1aAdf_ZIcfo9'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()