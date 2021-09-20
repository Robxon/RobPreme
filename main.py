from settings import define_settings
import robpreme


if __name__ == "__main__":
    # Saves desired color and keyword to variables
    user_color, user_keyword = robpreme.start_bot()

    # Saves settings as dictionary.
    user_settings = define_settings()

    # Opens Chrome browser window.
    user_driver = robpreme.initialize_browser()

    # Performs scanning the website in search of product which name contains keyword in selected color.
    product_link = robpreme.search_for_product(user_settings, user_color, user_keyword)
    print(product_link)

    # Automates checkout process.
    robpreme.buy_product(product_link, user_driver, user_settings)
