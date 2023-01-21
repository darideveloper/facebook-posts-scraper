import os
from time import sleep
from logs import logger
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from scraping_manager.automate import WebScraping
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

# paths
CURRENT_FOLDER = os.path.dirname(__file__)

class PostsScraper (WebScraping):

    def __init__(self, users: list):
        # Read environment variables
        chrome_folder = os.getenv("CHROME_FOLDER")
        headless = os.getenv("SHOW_BROWSER") == "False"
        self.max_posts = int(os.getenv("MAX_POSTS"))

        # div.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs.xdj266r.x126k92a div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd[role="button"][role="button"]
        # div.x1vvkbs div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd[role="button"][role="button"] 

        # Class variables
        self.selectors_text = {
            "text": '[data-ad-comet-preview="message"]',
            "reactions_num": '[role="button"] > span.xt0b8zv.x1jx94hy.xrbpyxo.xl423tq span.x1e558r4',
            "comments_num": 'div:nth-child(2) > span.x4k7w5x.x1h91t0o.x1h9r5lt.xv2umb2 [aria-expanded="true"] > span.x193iq5w.xeuugli.x13faqbe.x1vvkbs',
            "shares_num": 'div:nth-child(3) > span.x4k7w5x.x1h91t0o.x1h9r5lt.xv2umb2 [tabindex="0"] > span.x193iq5w.xeuugli.x13faqbe.x1vvkbs',
            "shared_form_user": '.x1y332i5 > .x1a8lsjc.x1swvt13.x1pi30zi .xu06os2.x1ok221b strong > span'
        }
        self.selector_post = "div[aria-posinset]"
        self.selector_link = 'span[id^="jsc_c"] a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd'
        self.selector_show_all = f'{self.selectors_text["text"]} div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd[role="button"][role="button"]'
        self.users = users

        # Start scraper
        super().__init__(chrome_folder=chrome_folder, headless=headless, start_killing=True)

    def scrape_posts(self):
        """ Scrape all facebook posts from specific user """

        # Generate header based on selectores
        data = list(self.selectors_text.keys())

        for user in self.users:

            print(f"Current user: {user}")

            # Open user profile
            user_page = f"https://www.facebook.com/{user}"
            self.set_page(user_page)
            sleep(2)
            self.refresh_selenium()

            last_posts_num = 0

            # # Load all posts of user
            # while True:

            #     # Scroll down for load more posts
            #     self.go_bottom()
            #     sleep(3)

            #     # Get number of posts
            #     self.refresh_selenium()
            #     posts_num = len(self.get_elems(self.selector_post))

            #     # End loop if all posts are loaded
            #     if posts_num == last_posts_num or self.max_posts and posts_num >= self.max_posts:
            #         break

            #     # Update last posts number
            #     last_posts_num = posts_num

            # Loop for each post found
            logger.info(f"\tScraping posts...")
            posts = self.get_elems(self.selector_post)                
            for post in posts:
                                
                # Hover for load post link
                link_elem = post.find_element(By.CSS_SELECTOR, self.selector_link)
                hover = ActionChains(self.driver).move_to_element(link_elem).perform()
                
                # Display full text of current post
                try:
                    show_all_button = post.find_element(By.CSS_SELECTOR, self.selector_show_all)
                except:
                    pass
                else:
                    self.driver.execute_script("arguments[0].click();", show_all_button)
                    
                # Get post link
                self.refresh_selenium()
                link_elem = post.find_element(By.CSS_SELECTOR, self.selector_link)
                link = link_elem.get_attribute("href")
                
                # Get text data from posts based in selectors
                row = [link]
                clean_words = ["\n", "comments", "shares", "comment", "share"]
                for selector in self.selectors_text.values():
                    # elem_text = " ".join(list(map(lambda elem: elem.text, post.find_elements(By.CSS_SELECTOR, selector))))
                    try:
                        elem_text = post.find_element(By.CSS_SELECTOR, selector).text
                    except:
                        elem_text = ""
                    else:
                        elem_text = " ".join([word for word in elem_text.split() if word not in clean_words])
                    
                    row.append(elem_text)
                    
                # Save post type
                post_type = "post"
                if row[-1]:
                    post_type = "shared"
                row.append(post_type)
                    
                # Save data
                data.append(row)
                logger.debug (row)
                print ()
                
            print ()

    def auto_run(self):
        """ Auto run for extract and save data """

        self.scrape_posts()


if __name__ == "__main__":

    # Get facebook users from txt file
    users_path = os.path.join(CURRENT_FOLDER, "users.txt")
    with open(users_path, encoding="utf-8") as file:
        users = file.read().splitlines()

    post_scraper = PostsScraper(users)
    post_scraper.auto_run()
