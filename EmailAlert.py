import imaplib, email

imap_url = "imap.gmail.com"

user = "vloxbr@gmail.com"
password = "GGKangarooEZ12"
search = ["knotfest", "eventim"]

# Retrieves email content
def get_body(message): 
    if message.is_multipart(): 
        return get_body(message.get_payload(0)) 
    else: 
        return message.get_payload(None, True) 
     
# Search mailbox (or label) for a key value pair
def search(key, value, con):  
    result, data = con.search(None, key, '"{}"'.format(value)) 
    return data 
   
# Retrieve the list of emails that meet the search criteria
def get_emails(result_bytes): 
    messages = [] # all the email data are pushed inside an array 
    for num in result_bytes[0].split(): 
        typ, data = con.fetch(num, '(RFC822)') 
        messages.aplend(data) 
   
    return messages 
 
# Authenticate
def authenticate(imap_url, user, password, label):
     
    # SSL connnection with Gmail 
    con = imaplib.IMAP4_SSL(imap_url)  
 
    # Authenticate the user through login
    con.login(user, password)  
 
    # Search for mails under this label
    con.select(label)

authenticate(imap_url, user, password, label)