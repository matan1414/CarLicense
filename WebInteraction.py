from bs4 import BeautifulSoup
from seleniumbase import Driver
import logging
import Enums
import time


class WebInteraction:

    def __init__(self, _logger):
        self.logger = _logger


    def print_class(self):
        # object_members = (f'Title: {self.agora_object.product_title} '
        #                   f'\nCondition: {self.agora_object.product_state}'
        #                   f'\nFrom region: {self.agora_object.product_region} '
        #                   f'\nFrom City: {self.agora_object.product_city} '
        #                   f'\nDetails: {self.agora_object.product_details} '
        #                   # f'\nPrice: {self.agora_object.product_price} '
        #                   f'\n\n To the product -> {self.agora_object.product_url}')
        #                   # f'\nProduct id: {self.agora_object.product_id}')
        # return object_members
        pass

    def interact_with_website(self, car_number):
        self.logger.debug('interact_with_website!')
        # self.agora_object.__init__()
        count = 0

        try:
            driver = Driver(uc=True, headless=True)
            driver.get(Enums.URLs.police_stolen_car)
            # Parse the HTML code using BeautifulSoup
            driver.wait_for_element('/html/body/div[3]/app-root/article/app-stolen-car/div[2]/div/div[2]', timeout=30)
            time.sleep(2)
            # Locate the textbox using its XPath or CSS selector and insert text
            driver.type("/html/body/div[3]/app-root/article/app-stolen-car/div[2]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div/div[1]/div[2]/input", car_number)

            # Click the button
            button = driver.click("/html/body/div[3]/app-root/article/app-stolen-car/div[2]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div/div[1]/div[2]/button")  # Replace with the actual XPath or selector
            # Wait for the new text to appear (you might need to adjust the waiting time or method)
            driver.wait_for_element_visible("/html/body/div[3]/app-root/article/app-stolen-car/div[2]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div/div[3]/span")  # Replace with the actual XPath or selector

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # Find the new text
            new_text = soup.find("div", class_="constText").text  # Adjust the tag and attributes as needed
            if new_text == 'הרכב לא מופיע במאגר כרכב גנוב':
                return 'This vehicle is not stolen.'
            else:
                return new_text

        except NameError:
            self.logger.error("Error fetching url")
        except Exception as e:
            self.logger.error("Something else went wrong, the error is: ", e)
            # await update.message.reply_text("Something else went wrong, the error is: ", e)
        finally:
            self.logger.debug(f'driver.quit()')
            driver.quit()

        return self.agora_object
