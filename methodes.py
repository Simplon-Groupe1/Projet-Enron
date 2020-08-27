import pandas as pd
import csv

def wordFromCSV(src, word):
    """Create a dataframe of the mails containing the target word.
    
    Args:
        src(csv): source of mails to explore.
        word(str): target word to find.

    Returns:
        df:dataframe
    """
    csv.field_size_limit(100000000)
    data=[]
    target=word.lower()
    # for i in range(len(target)):            #-------TEST WITH A LIST OF WORDS
    #     target[i] = target[i].lower()


    with open(src, 'r') as csvfile:
        mails = csv.reader(csvfile, delimiter='|')
        for message in mails:
            body_message=message[7].lower()
            if body_message.__contains__(target)==True:
                temp=[
                    message[1],
                    message[2],
                    message[3],
                    message[4],
                    message[5],
                    message[6],
                    message[7]]
                    
                data.append(temp)
                df = pd.DataFrame(data, columns=['Date',  'From',  'To', 'Cc',  'Bcc',  'Subject', 'Body']) 

    return df

def wordFromDF(src, word):
    """Create a dataframe of the mails containing the target word.
    
    Args:
        src(dataFrame): source of mails to explore.
        word(str): target word to find.

    Returns:
        df:dataframe
        """

    data=[]
    target=word.lower()
    # for i in range(len(target)):            #-------TEST WITH A LIST OF WORDS
    #     target[i] = target[i].lower()

    for index, message in src.iterrows():
        body_message=message['Body'].lower()
        if body_message.__contains__(target)==True:
            temp=[
                    message[0],
                    message[1],
                    message[2],
                    message[3],
                    message[4],
                    message[5],
                    message[6]]
                    
            data.append(temp)
            df = pd.DataFrame(data, columns=['Date',  'From',  'To', 'Cc',  'Bcc',  'Subject', 'Body']) 

    return df