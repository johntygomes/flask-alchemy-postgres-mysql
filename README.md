# flask-alchemy-postgres-mysql
## A Single Flask App Connected To Two Different Databases

## STEPS TO RUN ON YOUR MACHINE

1. Download the Zip File

2. Open Command Prompt in Root Directory where requirements.txt exists.

3. Create A Virtual Environment If Possible(Optional).

4. Run Command:: pip install -r requirements.txt

5. Note:: You Need To Have Created Two Databases As Follows<br>
                a. Postgresql Database Named As myheroes(refer to Output Screenshots folder)<br>
                b. Mysql Database Named As mycompanies(refer to Output Screenshots folder)<br>
                c. I used PG admin For The Postgres Database [Download PG Admin](https://www.pgadmin.org/download/)<br>
                d. I used Wamp phpmyadmin for the Mysql Database [Download Wamp](https://www.wampserver.com/en/)<br>

6. Run Command:: set FLASK_APP=hello.py<br>
    Note(Replace set with export if your on linux or mac os)

7. Run Command:: set APP_SETTINGS=config.DevelopmentConfig         
    Note(Replace set with export if your on linux or mac os)

8. Finally Run Command:: flask run
9. Copy The output link which might look like► http://127.0.0.1:5000/ and paste on Chrome
10. Complete






