TEAM: Dylan McCann and Damian Uduevbo

Design Talk:
Okay so this virtual router initially connects to the given neighboring sytems on the given ports by opening sockets and sending handshake messages, all of which is provided in the starter code. 
I added two lists, one simply called routes that will store the routing addresses the router recieves, and one called msg_log, that records the update announcements to be referred to when routes are withdrawn and the routing table needs to be rebuilt. 

The route.py file contains the route class, which basically stores the necessary route address information along with the CIDR of the network and netmask in one object for convenience. The routes list is populated by route objects. 

While the router is running it recieves various types of messages
and each type of message has it's respective method that handles the message. 

The two main helper methods that aren't one of the message types are aggregate, which adds a route to the routing table correctly depending on it's ability to be aggregated and calcOPT, which uses the 5 rules to determine the optimal port (prefix matching is handled right before the calcOPT method is used in the data method)

The rest of the helper methods are all relatively simple calculations or conversions that handle stuff like of ip address formats and values.


Challenges:
To be honest, this project was quite challenging. I remember when I first opened up the project I felt overwhelmed by the sheer volume of content that I needed to read through. I thought I understood routing and networking from class lectures but as I read through the project description I realized that my understanding was not nearly as good as I thought it was. For the first level of configs I actually drew out the network topology on pen and paper and wrote out all the messages and where I thought they should go and how the router should respond so that I would be able to understand errors i was getting. 

Of course as time went on I got MUCH more comfortable and now that I have finished the project I feel like a master of these ideas, but throughout the process I felt the challenge came less with actually coding or implementing the processes but understanding exactly how the processes work. For example I incorrectly aggregated routes and incorrectly implemented prefix match and did not understand why until I sat down and really solidified my understanding of ip addresses, netmasks, etc and then I finally understood where I was going wrong and changed it.  

Strengths:
I think that my design is very clean and has a flow that is easy to understand. Having a route object class allows for routing address information to be easily accessed and understandable. Everything is well documented and there is little to none repetition of code and the configs run smoothly and quickly. 

Testing:
Throughout the design process I was always running configs and troubleshooting the errors I would recieve. Any helper methods I made I would write some tests and run them in an outside interactive window to verify that they worked correctly and then would run configs to make sure they worked within my router. 





















