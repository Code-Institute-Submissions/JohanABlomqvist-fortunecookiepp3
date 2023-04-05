# Fortune Cookie App
Simple App made with python that interacts with google sheets takes fortunes preapplied into it and saves the name and fortune given into the document.

![Responsice Mockup](https://github.com/JohanABlomqvist/fortunecookiepp3/blob/58d2d6c4e88940adda6972a22fa83f92a45c5da7/assets/images/responsice.PNG)

[View Fortune Cookie App on the live Heroku website](https://fortunecookiepp3.herokuapp.com/)

[View Fortune Cookie App on Github pages](https://github.com/JohanABlomqvist/fortunecookiepp3/)
# CONTENTS
* [User Experience](#user-experience-ux)
  * [User stories](#user-stories)
* [Existing Features](#existing-features)
* [Features Left to Implement](#features-left-to-implement)
* [Testing and Bugs](#testing-and-bugs)
* [Validator Testing](#validator-testing)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Credits](#credits)

# User Experience (UX)

- Easy straight forward app to give you a fortune once you give it a name.

## User Stories

### First time visitor goals
- Hopefully they see a fun app that is functional and serves it's purpose.
- Straight forward what to do within the app.

### Returning visitor goals
- More fortunes, more options.

# Existing Features 

- __Game page__
 
  - Straight forward terminal fortune cookie app. tells you state your name to get a fortune in return.

![Home Page](https://github.com/JohanABlomqvist/fortunecookiepp3/blob/58d2d6c4e88940adda6972a22fa83f92a45c5da7/assets/images/appshow.PNG)


# Features Left to Implement

- None as of now

# Testing and Bugs
- Had problems when trying to get google sheets to communicate with python properly for the app, upon further inspection I had not set up my scopes in my code properly, managed to get that in and working after a few tries.
- Authentication set up to google sheets API was not set properly and json file was not properly introduced to the python or directory here. 
- 

## Unfixed bugs
- None that I know of.

# Validator Testing 

- Python
  -  

## Full testing
In the testing phase I tried breaking the app in any way I could think of, empty input, spaces, using !"#%¤# letter, number for example. I just get wrong input, please try again. so I think I made it foolproof, but I could be wrong. I did this in both the name in-put and the y/n prompts. 

# Technologies Used
## Languages Used
- Python was used to create this website


## Frameworks, Media, Libraries & Programs Used
- Heroku - To launch the terminal based app.
- Git - For version control.
- Github - To save and store the files for the website.
- [Am I Responsive?](https://ui.dev/amiresponsive) - Used to make the mockup picture for the Readme.

# Deployment
Github Pages was used to deploy the live website. The instructions to achieve this are below:

- Log in (or sign up) to Github.
- Find the repository for this project, fortunecookiepp3.
- Click on the Settings link.
- Click on the Pages link in the left hand side navigation bar.
- In the Source section, choose main from the drop down select branch menu. Select Root - From the drop down select folder menu.
- Click Save. Your live Github Pages site is now deployed at the URL shown.

## Local Development
### How to Fork
To fork the  design repository:

- Log in (or sign up) to Github.
- Go to the repository for this project, JohanABlomqvist/fortunecookiepp3.
- Click the Fork button in the top right corner..

### How to Clone
To clone the  design repository:

- Log in (or sign up) to GitHub.
- Go to the repository for this project, JohanABlomqvist/fortunecookiepp3.
- Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


# Credits

## Code Used
- Readme help from [Kera Cudmore](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md).
## Content
- All the written content is done by Johan Blomqvist.
## Acknowledgments
- Chatgpt for being a good learningtool, asking it the right questions can give you alot of clarity on code and how to build it.
- One of my friend's named Thomas Kjos that works in game development, giving alot of good feedback on what I need to work on.
- Lauren-Nicole, my mentor for all the support.
- Kera Cudmore, for all the information about the Readme-file.
- Stack Overflow for being the great repository it is, providing solutions and answers to questions regarding code.