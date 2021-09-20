def define_settings():
    """Modify values for keys accordingly to your needs"""

    settings = {"search_delay": "2.5",  # Suggested >=2 to avoid IP ban.
                "checkout_delay": "1.5",  # Suggested >=1.0 to avoid bot detection on checkout.
                "category": "https://www.supremenewyork.com/shop/all/skate",  # Subpage where product will be present.
                "name": "Name Surname",
                "email": "email@example.com",
                "phone_number": "123456789",
                "street_address": "StreetName 4",
                "zip_code": "01-123",
                "city": "SomeCity",
                "country": "Poland",
                "card_number": "4721 4066 6220 1838",
                "card_cvv": "678",
                "card_month": "12",
                "card_year": "2030"}

    return settings
