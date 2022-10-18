# 0x14. Javascript - Web scraping

## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
* How to manipulate JSON data
* How to use request and fetch API
* How to read and write a file using fs module
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc
* You are not allowed to use var
## More Info
Install Node 10
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard
Documentation

$ sudo npm install semistandard --global
Install request module and use it
Documentation

$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. Readme](./0-readme.js)** - Write a script that reads and prints the content of a file
- [x] **[1. Write me](./1-writeme.js)** - Write a script that writes a string to a file
- [x] **[2. Status code](./2-statuscode.js)** - Write a script that display the status code of a GET request
- [x] **[3. Star wars movie title](./3-starwars_title.js)** - Write a script that prints the title of a Star Wars movie where the episode number matches a given integer
- [x] **[4. Star wars Wedge Antilles](./4-starwars_count.js)** - Write a script that prints the number of movies where the character “Wedge Antilles” is present
- [x] **[5. Loripsum](./5-request_store.js)** - Write a script that gets the contents of a webpage and stores it in a file
- [x] **[6. How many completed?](./6-completed_tasks.js)** - Write a script that computes the number of tasks completed by user id
### Advance :muscle:
- [x] **[7. Who was playing in this movie?](./100-starwars_characters.js)** - Write a script that prints all characters of a Star Wars movie
- [x] **[8. Right order](./101-starwars_characters.js)** - Write a script that prints all characters of a Star Wars movie
- [x] **[9. Twitter Auth](./102-search_twitter.js)** - [856588726884982800] Itching to read my python book...instead picked up a mystery novel
