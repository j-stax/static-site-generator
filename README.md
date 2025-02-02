# Static Site Generator

This is an object-oriented program written in Python that turns markdown files into static websites. Here is the flow of data:

1. Markdown files are in the ```/content``` directory. A ```template.html``` file is in the root of the project.
2. The static site generator (the Python code in ```src/```) reads the Markdown files and the template file.
3. The generator converts the Markdown files to a final HTML file for each page and writes them to the ```/public``` directory.
4. The built-in Python HTTP server (a separate program, unrelated to the generator) is used to serve the contents of the ```/public``` directory on ```http://localhost:8888``` (local machine).
5. Open a browser and navigate to ```http://localhost:8888``` to view the rendered site.

## How to run the program:

1. Download the files into a code editor that has Python3 installed.
2. Either use the example markdown files in the ```/content``` directory, or write your own markdown in these files.
3. Open up a terminal in the code editor and run ```./main.sh```
4. Open a browser and go to ```http://localhost:8888``` to see the rendered markup.
