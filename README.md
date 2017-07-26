# DataIncubatorProject

## Requirements for running the app:-

* Python 2.7
* Jinja2-2.9.6
* Werkzeug-0.12.2
* flask-0.12.2
* gunicorn-19.7.1
* Nginx (for running on local)

## Setting up the app

The webapp could be run on localhost as well as on Heroku server

LocalHost:
- Running on localhost will require cloning of github repository using command
  ## $ git clone https://github.com/Prateek90/DataIncubatorProject.git
 
- After cloning of the repository and installing all the requirements the app can be run by following the below steps:
    * Go to the directory where repository is cloned.
    * Give the following command to run the app
      ### $ gunicorn DataIncubatorAlgorithm:app
    * After running the above command the app can be accessed via web browser at http://127.0.0.1:8000

HerokuServer:
- The app is deployed on the heroku server and it can be accessed by following this link : https://uservideoallocationapp.herokuapp.com/

## Algorithm for video assignment

The app assigns m videos to users for review randomly. The process of allocation could be defined as follows:
  * The process starts by creating list of m videos for n users, this is acheived in the following way:
    -A number is selected between 1 to n randomly
    -After selection of number m continuous numbers are taken n times in cyclic order thus creating a list of size n with m videos in each list
  * After that each review from previously created list needs to be assigned one of then user such that user is not reviewing his/her own video
    This is acheived in the following way:
      - A user from n users is selected randomly such that all the requirements are satisfied, and that user is allocated a list of videos to review
      - Above process continues n-m times and at the end we will be left with m+1 users and m+1 reviews
      - For assigning these m+1 users with m+1 reviews we use the process of recursion.
      - The recursion algorithm base case checks if number of reviews=0, this case suggests that every user is allocated list of videos to review.
      - If every user is not allocated video to review then a user is selected from the list of remaining users for allotment, this user is first checked that it complies with the requirement, if so video is allocated to this user, if not then other user from the list is selected that complies with requirements and this process continues until allotment to user is completed.

## Design Decisions

Following are the design decisions that were taken for webapp development

Framework: Python Flask, 
Why?
* It is easy to use light weight Framework
* It is extensively documented
* It has its own development server and debugger
* Flask uses Jinja 2 templating

Hosting Server: Heroku, 
Why?
* It is really easy to deploy on Heroku server
* It is easy to scale
* It is easy to setup as it doesn't require that much customization.

## Tradeoffs

### Memory Usage and Processing:

Since we have limited resources there is a tradeoff of memory and processing power, as the number of user and reviews per video increases the process starts to consume more memory and processing power. We have employed the process of recurison and as the number of reviews per video  increases recursion starts to consume more memory and processing power, but this won't be a problem if number of reviews are taken in a nominal range.

## Warning : 
As we have limited processing power and timeout of application on heroku is 30 sec,if very high value of users/number of videos is given, the process will work perfectly on local but on heroku timeout occurs as process takes more than 30 sec
