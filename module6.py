#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lenovo
#
# Created:     23-12-2021
# Copyright:   (c) lenovo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.A-tVURbNCmC0Pa0bqhidIDNhMtzTisJdiI9q14k3aB9p6JYJqx95-uvtQ14TA-vM5mkXm1dL8Aa0iqbel-CFcga8X82wdhFdWkVzPwesdaO7cCzmN3aR09P_fchsScP_upfi-r1e9Pw"
    transferData = TransferData(access_token)

    file_from = "test.txt"
    file_to = "/backupFiles/notes5.txt"
    transferData.upload_file(file_from,file_to)
    print("file has been moved")


main()