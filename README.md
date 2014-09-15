dataweek2014
============

Megaopolis is an app that addresses the issue of Crowd Counting. Simply put, crowd counting is the task of trying to count the number of people in a large crowd ideally through automated means. The benefits of having a good system in place that can do this task well include improving security, resource management, emergency response, and many others.

Current ways of doing this include manual tally counters at the entrances of events, top-down satellite views that estimate, and most recently check-ins. 

However, such methods require a lot of manpower, are potentially very costly, and are many times not accurate (not everyone who goes to an event actually checks-in to the event). Also once we start looking at cases when the crowd is moving, the problem becomes significantly harder. 

Thus, in order to address this problem, we turned towards the growing-area of computer vision. For our dataset, we looked to examining real-time webcam data in New York in order to count how many people there are at a given time. 

Our app was implemented in three stages:
* Remove all the background from the video using Python's OpenCV library.
* Detect contiguous regions.
* Filter out regions that do not match human forms.

Once this was done we utilized the Google Maps and Youtube API to visually display our webcam feeds and present our counts. We also allowed for a "Send Email Alert" button that could be used by government or authorities to send out an email alert if the number of people shown by the webcam is too high. 

Hopefully this project can be extended to utilize methods found in papers such as [this](http://mplab.ucsd.edu/wp-content/uploads/CVPR2008/Conference/data/papers/229.pdf).

To run the project, follow the directions found [here](https://github.com/zichongkao/dataweek2014/tree/master/megalopolis_server)
