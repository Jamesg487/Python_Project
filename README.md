Python Project - Whisker & Walkies

To run the project:

1. Once you have cloned the repo create the database in your terminal by running `createdb whiskers_and_walkies`

2. Next, run this psql query to set up the SQL database `psql -d whiskers_and_walkies -f db/whiskers_and_walkies.sql`

3. To add the seed data in the console.py file run `python3 console.py`

4. Lastly, use `flask run` to get the wed framwork going and then head to your local ip address `http://127.0.0.1:5000/` to see the website home page which should look something like this!

![Home Page](templates/img/Home%20Page.png)
