Python Project - Whisker & Walkies

Whiskers and Walkies is a web app to help a veterinary practice keep track of Vets and Pets registered at the practice.

There is the added ability to create Owners and assign them to Pets and for Owners and Vets to book appointments for Pets to come in for treatment.


To run the project:

1. Once you have cloned the repo create the database in your terminal by running `createdb whiskers_and_walkies`

2. Next, run this psql query to set up the SQL database `psql -d whiskers_and_walkies -f db/whiskers_and_walkies.sql`

3. To add the seed data in the console.py file run `python3 console.py`

4. Lastly, use `flask run` to run the web framework and then head to your local ip address `http://127.0.0.1:5000/` to see the website home page which should look something like this!

![Home Page](templates/img/Home%20Page.png)