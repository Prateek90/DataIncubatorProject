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

The app assigns m videos to usersfor review randomly. The process of allocation could be defined as follows:
  * The process starts by creating list of m videos for n users, this is acheived in the following way:
    -A number is selected between 1 to n randomly
    -After selection of number m continuous numbers are taken n times in cyclic order thus creating a list of size n with m videos in each list
  * After that each review from previously created list needs to be assigned one of then user such that user is not reviewing his/her own video
    This is acheived in the following way:
      - A user from n users is selected randomly such that all the requirements are satisfied, and that user is allocated a list of videos to review
      - Above process continues n-m times and at the end we will be left with m+1 users and m+1 reviews
      - For assigning these m+1 users with m+1 reviews we use 2 data structures one is stack and other one is queue.
      - All m+1 users aare put into queue, users are selected one by one from queue and whoever satisfies the requirement is removed from queue and pushed into stack, a list of videos to review is allocated to that user.
      - If the queue is not empty and requirements are not satisfied for any user from the queue the a user is 
        popped from the stack and the list of videos allocated to that user is again unallocated and user is put back into the queue.
      - The above process continues until the queue becomes empty thereby allocating list of videos to review to each user.
  

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
As the users or reviews goes on increasing, considering our limited resources like memory and processing power the time to allocate videos to users also increases. In the algorithm that has been implemented the allocation is first stored in the list of list and the last m+1 allocation require stack as well as queue for there allocation, for smaller numbers of m it works really well but as the number of reviews per video increases the process starts to consume more memory and also more processing power making the process slower, the efficiency of this process can be increased by making use of distributed computing.
