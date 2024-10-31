This is a project I completed following the completion of my work experience placement in October 2022 at SRS Consulting Inc. in Fremont, California. 

I built a web scraper that fetches the stock price of a stock that is chosen by the user. 

This stock data is then validated against data I find from looking at the Yahoo! Finance API request I make and then once validated, if there is negligible change between the web scraped data and the API fetch data, an email is sent out to users on a pre-defined mailing list utilising the Robot framework.

In order for the emailing functionality, I had to create an mail account on Outlook and in order to athenticate myself, I had to hardcode the login details and include them in the program as well as the email addresses of the users in the mailing list. 

The only other change I've made to the code excluding any personal data is swapping the for loop I used to iterate through the email addresses and opted for a hardcoded version instead which works for a singular email address.
