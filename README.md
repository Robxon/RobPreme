# RobPreme
A Supreme bot allowing for quick checkout of most coveted items before they sellout.

<p align="center">
  <img src="https://user-images.githubusercontent.com/90696522/134012744-1752c8e8-b1e9-40a3-98f4-0c1e51b94781.png" alt="Logo"/>
    <br>
  
<p align="center">
  <img src="https://user-images.githubusercontent.com/90696522/134062222-ae4957da-07da-49b2-b656-6e5b4888b3f2.gif" alt="Autocheckout"/>
    <br>  
    
## Requirements
- Python 3
- Google Chrome
- ChromeDriver

## Usage
### 1. Clone the project and install dependencies:
```
$ git clone https://github.com/Robxon/RobPreme
$ cd RobPreme
$ pip install -r requirements.txt
```
### 2. ChromeDriver:
Download ChromeDriver (https://chromedriver.chromium.org/downloads) for the version of Google Chrome you're using and place executable in directory with the script.

### 3. Fill the `settings.py`:
```
    settings = {"search_delay": "2.5",                                        - delay (in seconds) between refreshing 'category' subpage
                "checkout_delay": "1.5",                                      - delay between filling fields and pressing 'process payment' button
                "category": "https://www.supremenewyork.com/shop/all/skate",  - subpage in which product is expected to drop
                "name": "Name Surname",                                       
                "email": "email@example.com",                                 
                "phone_number": "123456789",
                "street_address": "StreetName 4",
                "zip_code": "01-123",
                "city": "SomeCity",
                "country": "Poland",
                "card_number": "1111 1111 1111 1111",                         -  put spaces between each 4 digits
                "card_cvv": "111",
                "card_month": "11",
                "card_year": "2030"}
 ```
    
 ### 4. Run the bot:
   ```
   $ python main.py
   ```
  
 The program will ask you about the color and the keyword. Based on your response it will try to find item matching these criteria within subpage specified in settings. In case of match it will automatically start checkout process in browser.
  
 \* In case of occurence of captcha, it has to be solved manually in order to finalize the checkout.
 
 \* The program has been tested in EU region and may not work in other zones.
