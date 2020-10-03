This program will automatically move files to designated locations.

To setup, change all of the "locations" int the file_mover python file.
Make sure to install python 2.7+
https://www.python.org/downloads/release/python-2718/

Next, on your command line, do "pip install -r requirements.txt"

Update the tasker.bat to have the path where downloads_lister.py exists.

You can set a task in the task scheduler on windows to automatically run the script at startup.
1. Open Task Scheduler
2. Select Create Task on the right side
3. Give the task a name and at the bottom select "run with highest privileges"
4. Select triggers and new..
5. On the dropdown for "begin the task" select "at log on" then OK.
6. Next go to actions, select new, then action should be start a program and start the tasker.bat