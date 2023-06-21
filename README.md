<div><a href='https://github.com/darideveloper/facebook-posts-scraper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/facebook-posts-scraper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/facebook-posts-scraper/raw/master/imgs/logo.jpg' alt='Facebook Posts Scraper' height='80px'/>

# Facebook Posts Scraper

Python scraper for get facebook post from specific users, and save the output data in csv file.

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Details

The project opens each profius page, scroll for load all the posts, extract the data from each posts and validate if the post have specific keywords.

The data extract is:

* user
* link
* text
* reactions number
* comments number
* shares number
* shared form user (just in case that the post is shared)
* type (post or shared post)
* keyword found (if the post have one ore more of the keywords)

# Install

## Prerequisites

* [Google chrome](https://www.google.com/intl/es-419/chrome/)
* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/facebook-posts-scraper.git
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```

# Settings

Update your settings in the `.env` file:
 ```sh
	CHROME_PATH = C:Users<<your-user-name>>AppDataLocalGoogleChromeUser Data # Path of your chrome data folder
	SHOW_BROWSER = False # Show or hide the google chrome window
	MAX_POSTS = 50 # Max number of posts to extract from each user
 ```

# Run

1. Login in your facebook account in the google chrome browser.
2. Set the users in the `users.txt` file (the user name is the last part of the url). Sample: 
    ```txt
    abdenago.lopezh
    freddyvega
    sunoticiasuy
    profile.php?id=100011069504105
    Dragster.Systems
    ReneRojas1968
    ```
3. Set the keywords in the `keywords.txt` file. Sapmple:
    ```txt
    and
    hello
    this
    el
    la
    y
    este
    ```
4. Run the script, opening a terminal in the project folder
   ```sh
   python __main__.py
   ```
4. The output data will be saved in the `posts.csv` file.

# Roadmap

- [x] Load users from file
- [x] Load keywords from file
- [x] Scroll for show all the posts
- [x] Extract data from each post
- [x] Save data in csv file

