
*** Variables ***
${EMAIL}    RobotFrameWorkTrial@outlook.com
${PASSWORD}    Left_Intentionally_Blank

*** Settings ***
Library    RPA.Email.ImapSmtp    smtp_server=smtp-mail.outlook.com    smtp_port=587    imap_server=outlook.office365.com
Task Setup    Authorize    account=${EMAIL}    password=${PASSWORD}
 