About this APP:
Online Code Editor to code,compile and run the program

Features:
1)Code compile and run
2)Custom input field
3)Auto code save
4)Share code urls 
	option to choose between read-only urls and read-write urls
5)Changing the language option

Used Resources:
1)Hackerearth code api for compilation/running
2)Ace Editor JS for syntax-highlighting, auto-complete
3)Jquery
4)Bootstrap for FrontEnd

How to run:

2)access the manage.py in root of unzipped folder, and do "python manage.py makemigrations CodeEditor" -- this will ready the db schemas.
3)then "python manage.py migrate" -- will create the schemas
4)then "python manage.py runserver" -- to start the server
5)if no url and port are given , it will  run the server on the default ones.
6) Access the url it'll open the codeeditor to generate the unique token for the code editor.
7) write, compile and run 
8) Press 'share url' button to create the url by giving the read/write options.
9)  Choose the drop-down menu to choose the language.
10) Give the input field to take the input tests