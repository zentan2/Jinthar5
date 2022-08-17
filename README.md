Instructions to run the flask application

1. Install python virtual env into your project directory
- python -m venv venv

2. go into the python virtual env
- source venv/bin/activate

3. Install the dependancies from the requirements.txt file
- pip3 install -r requirements.txt

4. Run the python flask application to start the flask server


#### CitiTraining ####

# quick installation start

git init

git remote add upstream git@github.com:zentan2/Jinthar5.git

py -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

# commands to write for setting up

python3 -m venv venv

# start the virtual environment

venv\Scripts\activate

# to deactivate the virual environment

deactivate

# command to update the dependency used

python -m pip freeze > requirements.txt

# github work flow

## how to get changes from Zen's repo

git fetch upstream

git merge upstream/main


## How to update the sqlite database
1. update/add/remove the columns from the models.py
2. go to init.py and remove flask run
3. go to run.py and run the following
# flask db migrate
# flask db upgrade