import mailbox
import csv

def get_message(message):
    if not message.is_multipart():
        return message.get_payload()
    contents = ""
    for msg in message.get_payload():
        contents = contents + str(msg.get_payload()) + '\n'
    return contents

if __name__ == "__main__":

    with open("sampleCsv.csv", "w") as writer:
    #writer = csv.writer(open("clean_mail.csv", "wb"))
        for message in mailbox.mbox("archive.mbox"):
            contents = get_message(message)
            writer.writerow([message["subject"], message["from"], message["date"],contents])