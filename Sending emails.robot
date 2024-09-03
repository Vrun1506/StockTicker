*** Settings ***
Library    RPA.Email.ImapSmtp    smtp_server=smtp-mail.outlook.com    smtp_port=587    imap_server=outlook.office365.com
Task Setup    Authorize    account=%{EMAIL}    password=%{PASSWORD}

*** Variables ***


*** Tasks ***
Sending Email
    Send Message    sender=%{EMAIL}    
    ...                recipients=vnayak1506@gmail.com
    ...                subject=A message from your robot
    ...                body=Message from your robot
    ...                attachments=example.xlsx            
