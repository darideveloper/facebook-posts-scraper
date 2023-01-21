import os
import csv
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
        self.selector_link_hidden = f'{self.selector_link}[href="#"]'
        self.selector_show_all = f'{self.selectors_text["text"]} div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd[role="button"][role="button"]'
        self.users = users
        self.data = [["link"] + list(self.selectors_text.keys()) + ["type"]]

        # Start scraper
        super().__init__(chrome_folder=chrome_folder, headless=headless, start_killing=True)

    def scrape_posts(self):
        """ Scrape all facebook posts from specific user """

        # Loop for each user
        for user in self.users:

            print ()
            logger.info (f"Current user: {user}")

            # Open user profile
            user_page = f"https://www.facebook.com/{user}"
            self.set_page(user_page)
            sleep(2)
            self.refresh_selenium()

            # Posts counters
            posts_num = 0
            last_posts_num = 0
            posts_links = []

            # Loop for load all posts
            more_posts = True
            while more_posts:
                
                logger.info(f"\tScraping current posts...")
                
                # Hover for load all post links, if links are hidden
                link_elems = self.get_elems(self.selector_link_hidden)
                for link_elem in link_elems:
                    try:
                        hover = ActionChains(self.driver).move_to_element(link_elem).perform()
                    except:
                        pass
                
                # Display full text of all post
                show_all_buttons = self.get_elems(self.selector_show_all)
                for show_all_button in show_all_buttons:
                    try:
                        self.driver.execute_script("arguments[0].click();", show_all_button)
                    except:
                        pass
                    
                self.refresh_selenium()

                # Loop for each post visible in the current page
                posts = self.get_elems(self.selector_post)                
                for post in posts:
                        
                    # Get post link
                    link_elem = post.find_element(By.CSS_SELECTOR, self.selector_link)
                    link = link_elem.get_attribute("href")
                    
                    # Skip post if already scraped
                    if link in posts_links or "#" in link:
                        continue
                    
                    # Save post link in history
                    posts_links.append (link)
                    
                    # Incress counter
                    posts_num += 1
                    
                    # Get text data from posts based in selectors
                    row = [link]
                    clean_words = ["\n", "comments", "shares", "comment", "share"]
                    for selector in self.selectors_text.values():
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
                        
                    # Save data in list
                    self.data.append(row)
                    logger.debug (row)
                    
                    # Validate if there are found new posts
                    if posts_num == last_posts_num or posts_num >= self.max_posts:
                        more_posts = False
                        break
                
                # Update counters
                logger.info (f"\tPosts scraped: {posts_num}")
                last_posts_num = posts_num
                
                # Scroll down for load more posts
                logger.info ("\tLoading more posts...")
                self.go_bottom()
                sleep(3)
                self.refresh_selenium()
                
            logger.info (f"\tTotal posts scraped: {posts_num}")
                
    def get_data (self):
        """ return post scraped data as a nested list """
        return self.data

if __name__ == "__main__":

    # Get facebook users from txt file
    users_path = os.path.join(CURRENT_FOLDER, "users.txt")
    with open(users_path, encoding="utf-8") as file:
        users = file.read().splitlines()

    post_scraper = PostsScraper(users)
    post_scraper.scrape_posts()
    data = post_scraper.get_data()
    
    print ()
    logger.info ("Saving data in csv file...")    
    csv_path = os.path.join (CURRENT_FOLDER, "posts.csv")
    with open (csv_path, "w", encoding="utf-8", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
    logger.info ("Done!")