# Fit-Pro-Quo

Fit-Pro-Quo is a small site made for the code institute Data Centric Milestone Project. Here You can create, edit and delete pre-planned training session. The aim is to help people plan training, specific to what sport they want to progress in. Sports can be added in and deleted out if needed.

## UX

When the user first opens the home page, they are clearly presented with different options to take them to different pages elsewhere in the site. The navbar and footer is clearly laid out, easy to read and consistent throughout the whole site.

The Fit Tracker page is where all planned and completed sessions are displayed for the user to see. Each session is shown in date order for ease of use and once clicked on is expanded to show more detail. The specific details of each session are laid out in a table format which is easy for the user to process and understand. Once completed the user can use the Feedback button to add extra information or if the training session had changed in anyway then they can edit what was already there. There is also the option to delete each session if the user decides that it is no longer needed in the fit Tracker.

On the Sports page, all the different sport categories are displayed in a similar format to the Fit Tracker page however simply just more compact. The extra detail under every sport describes what each individual sport is. Again, the user has the ability to add and delete different sport categories when needed.

The final page on the navbar is the add session. This is so the user has quick access to this form at all points while on the site. Here they fill out the simple form that will update the Fit Tracker page with any new sessions the user has added.

## Features

Fit-Pro-Quo is an interactive site that allows users the plan, create, review, edit and delete specific sessions.

The user can add both sessions with session plans specific to their sport and there expected fatigue levels along with the ability to add a new sport to the database. When a user has added either a new session or sport the database is updated and the new information is then displayed in other places on the site. 

All sessions added to the database are also able to be edited and updated with feedback from the user. The site will load all the current data from the database and then display it in an easy to understand format for the user to modify and submit. 

Both the sessions and the sports can also be deleted from the database. Both are linked with a modal so that the user will never accidentally delete a session without meaning to. Once the information has been deleted it cannot be retrieved however can be recreated by the user if needed.

Finally, on the sports page the information below each sport describes that sport which is update when the sport is being added to the database.

### Future features

In the future I would potentially change the layout of the Fit Tracker page to a calendar layout so that finding session could be even easier.

I would also like to add in more input options for the Fit Tracker sessions so that the user can be even more specific in what they want to achieve and do in each individual session.

I would also like to have a completed feature added so that you can filter down the sessions on the Fit Tracker page to those that have been completed and those that are yet to be completed.

## Technologies Used 

Google Chrome developer tools https://www.google.com/chrome/ I used these to test my site on different device sizes and to receive information from javascript in the console.

Google fronts https://fonts.google.com/ Google fonts allowed me to change my text throughout the site to give it a more appropriate style and look for the user.

Materialize https://materializecss.com/ Materialize was used throughout this site for its grid system and different layout features. It has allowed me to change sizes and add features to my site which has helped give it a more professional look and easier for the user to understand.

JQuery https://jquery.com/ JQuery has made it easier to target specific aspects of the site in javascript by simplifying the DOM.

W3C validator https://validator.w3.org/ The W3C validator allowed to check my code is clean and had no faults.

MongoDB https://www.mongodb.com MongoDB is a database that I'm using to store all the information gained from the site.

Flask https://www.fullstackpython.com/flask.html Flask is a framework that has help make the code easier to write and display.

Heroku https://www.heroku.com Heroku allows me to create a link with the site running with a working application.

## Testing

For testing to begin with all the HTML and CSS code was run through direct input into the W3C Validator and any errors or coding problems were fixed. 

Code was tested for adding to to database first by fillinging the form and then simply reading to the console. There are no requirments in many of the form options because they are not always needed in every option. 

The link was then sent to 5 people to test on diffrent devices from an apple imac to a samsung galaxy phone and visually the site appeared well across the board. 

Then I asked them to find diffrent areas of the site to test how easy it was to navigate. For example I asked one person to find the add sports page or asked another person to find the fit tracker page. Every time I asked anyone to find somewhere on the site they were easily able to find the correct page which shows the site was easy to navigate.

Next I asked them to use the site for it's functionality by having them add a sport and then delete it from the database. Followed by having them add a new session, edit it after already submitting it and then finally deleting it. All were able to easy follow my instructions and the site worked as supposed to. 

Next I asked them to do their best to break the site in anyway they could. They pointed out to me that when adding or editing sessions you could leave spaces blank and still submit but I felt that to give anyone using this site to create a better plan for themselves, it was better to be able to leave gaps because it might be something they don't know at the time and can come back to.

## Deployment

Throughout development the application and code was written in AWS cloud 9 and run locally for testing.

This site has been pushed to github pages and then conected to heroku to run the app. While uploading and linking to Heroku, my tutor Aaron Sinnott help me make sure everything was in place to run the code and make sure it works. We set the config var IP to 0.0.0.0 and the PORT to 5000.



### Content
All hard coded content on this site was written by myself.
### media
The background image for this site came from https://pxhere.com/en/photo/1376234 which was labelled for reuse. 
### Acknowledgements
I received inspiration for this project while attempting to plan out my own training plan and create a specific training regime