# flask-live-charts
This rep show how to display live charts on a dashboard implemented using Flask. 
User don't have to refresh the page everytime to see the changes. That will happen automatically. 

# implementation
The idea is to send the data recieved from mqtt broker to the chart over a socket.

-> Connects to the mqtt in Flask
-> message recieved from mqtt broker are sent through sockets
-> base.html connects to sockets and draw the chart
 