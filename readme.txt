SIMPLESERVER - MY TEST TASK

This was my first trial project that I developed on Django. This was my first trial project that I developed on Django. It is a simple web server that allows you to run Linux OS shell commands in a browser and receive the result of the command in text/plain format.


HOW TO USE THE PROJECT.
1. Download the simpleserver.zip archive from this repository and extract it with the UNZIP command.
2. After unpacking the archive, go to the ~/simpleserver directory.
3. Start the server with the command:
python3 manage.py runserver
(for this, you must have the python3 package installed. If you do not have this package installed yet, install it using the following command: sudo apt update && sudo apt install python3). You can stop the server with the Ctrl+C key combination.
4. When you see that the server has started, open a browser convenient for you and enter the following address in the address field:
http://localhost:8000
5. On the page you will see, enter any Linux shell command in the text field and click the "Submit" button. A new page will open in your browser with the result of the command in text/plain format.
