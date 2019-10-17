#Instructions to run:


After cloning, 
from the directory where run.py is present, do the following:

export FLASK_APP=run.py;
flask run --host=0.0.0.0

#Documentation:

This will first download the file located in an AWS S3 bucket, parses it and loads the datastructures (list and dictionary)
It will then unzip the next file, parses it and loads the same datastructures

It sorts the list data in the increasing value of price.

Starts the api server with endpoints given

Endpoints are defined in the search package (psearch.search.routes) which is registered as a blueprint with the app for scalability purpose.

#API s provided:

 curl  http://localhost:5000/id/ID - retrieves a single product by its ID (where ID is a configurable string that the client can specify)
 
 curl  http://localhost:5000/cheap/N - retrieves the N cheapest products (where N is a configurable number that the client can specify)

<iframe src="https://giphy.com/embed/K9b2WiPZi0ZjO" width="480" height="361" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/eating-deer-K9b2WiPZi0ZjO">via GIPHY</a></p>
