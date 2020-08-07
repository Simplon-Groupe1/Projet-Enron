from email.message import Message
#from pandas.DataFrame import to_csv
import pandas as pd
import os
import email
import csv
from mail import Mail

PATH = os.path.dirname(os.getcwd())+os.sep


def get_files(path):
    for path, dirs, files in os.walk(maildir):
        for filename in  files :
            yield os.path.join(path, filename)


def maildir_to_message(maildir):
    lstMsg=[]
    for f in get_files(maildir):
        with open (f, 'r'):
            message = email.message_from_string(f)

            if message.is_multipart():
                for part in message.walk():
                    msgType = part.get_content_type()
                    msgDispo = str(part.get('Content-Disposition'))

                    # skip any text/plain (txt) attachments
                    if msgType == 'text/plain' and 'attachment' not in msgDispo:
                        content = part.get_payload(decode=True)
                        break
            else:
                content = message.get_payload(decode=True)
            header=message.items()
            path= os.path.abspath(__file__)#Wrong path !
            un_msg=Mail(header, content, path)
            lstMsg.append(un_msg)

    return lstMsg

def to_csv(lstMsg):
    with open ('sampleCsv.csv', 'w'):
        df = pd.DataFrame()
        df.to_csv(index=False)


maildir=(PATH+'maildir'+os.sep+'bass-e'+os.sep+'funny'+os.sep)
print(maildir_to_message(maildir)[2].header)
