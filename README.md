<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Fiverr][fiverr-shield]][fiverr-url]
[![Gmail][gmail-shield]][gmail-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/darideveloper/facebook-posts-scraper">
    <img src="imgs/logo.jpg" alt="Logo" width="200" height="120">
  </a>

<h3 align="center">Facebook Post Scraper</h3>

  <p align="center">
    Python scraper for get facebook post from specific users, and save the output data in csv file.
    <br />
    <a href="https://github.com/darideveloper/facebook-posts-scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/darideveloper/facebook-posts-scraper/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

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

### Built With


<div>
<a href="https://www.python.org/">
  <img src="https://cdn.svgporn.com/logos/python.svg" width="50" alt="python" title="python">
</a>
<a href="https://www.selenium.dev/">
  <img src="https://cdn.svgporn.com/logos/selenium.svg" width="50" alt="selenium" title="selenium">
</a>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Google chrome](https://www.google.com/intl/es-419/chrome/)
* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/facebook-posts-scraper.git
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```
3. Update your settings in the `.env` file:
   ```sh
    CHROME_PATH = C:\Users\<<your-user-name>>\AppData\Local\Google\Chrome\User Data # Path of your chrome data folder
    SHOW_BROWSER = False # Show or hide the google chrome window
    MAX_POSTS = 50 # Max number of posts to extract from each user
   ```

<!-- USAGE EXAMPLES -->
## Usage

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

<!-- ROADMAP -->
## Roadmap

- [x] Load users from file
- [x] Load keywords from file
- [x] Scroll for show all the posts
- [x] Extract data from each post
- [x] Save data in csv file

See the [open issues](https://github.com/darideveloper/facebook-posts-scraper/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Darideveloper - [@developerdari](https://twitter.com/developerdari) - darideveloper@gmail.com.com

Project Link: [https://github.com/darideveloper/facebook-posts-scraper](https://github.com/darideveloper/facebook-posts-scraper)


<!-- MARKDOWN LINKS & imgs -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/darideveloper/facebook-posts-scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/darideveloper/facebook-posts-scraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/darideveloper/facebook-posts-scraper.svg?style=for-the-badge
[forks-url]: https://github.com/darideveloper/facebook-posts-scraper/network/members
[stars-shield]: https://img.shields.io/github/stars/darideveloper/facebook-posts-scraper.svg?style=for-the-badge
[stars-url]: https://github.com/darideveloper/facebook-posts-scraper/stargazers
[issues-shield]: https://img.shields.io/github/issues/darideveloper/facebook-posts-scraper.svg?style=for-the-badge
[issues-url]: https://github.com/darideveloper/facebook-posts-scraper/issues
[license-shield]: https://img.shields.io/github/license/darideveloper/facebook-posts-scraper.svg?style=for-the-badge
[license-url]: https://github.com/darideveloper/facebook-posts-scraper/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/
[product-screenshot]: ./imgs/screenshot.gif
[gmail-url]: mailto:darideveloper@gmail.com
[fiverr-url]: https://www.fiverr.com/darideveloper
[gmail-shield]: https://img.shields.io/badge/-gmail-black.svg?style=for-the-badge&logo=gmail&colorB=555&logoColor=white
[fiverr-shield]: https://img.shields.io/badge/-fiverr-black.svg?style=for-the-badge&logo=fiverr&colorB=555&logoColor=white

<span>Last code update: <time datetime="2022-11-29" class="last-update">2023-01-21</time>
