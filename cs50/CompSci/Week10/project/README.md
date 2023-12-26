# Hardball Dice
#### Video Demo:  https://youtu.be/3XjzxV-Nqy0
#### Description:

Hardball Dice is a two player baseball dice game. Users take turns playing an inning of baseball until 9 innings are complete. It was written in Javascript and HTML. Vanilla Javascript was used for managing the game flow and p5.js was used to render the user interface. Bootstrap was used as an aid for the HTML layout. The content for this application is inside of the Flask framework to allow for continued development beyond the scope of this project.

The application can be run with the following command in the root of the project:

```
flask run
```

This executes app.py and by default renders the Index.html template. Index.html is a full HTML document that uses p5.js to render a game canvas and draw user interface elements. The bulk of the application is in 3 separate Javascript files.

##### gameState.js
gameState.js defines a class, GameState, that contains the necessary properties to describe the state of the game. Player names, inning scores, total score, who's turn it is, the current inning, and which bases are occupied. GameState is used by the gameManager.js and the p5.js sketch in sketch.js.

##### gameManager.js
gameManager.js defines a class, GameManager, that controls the flow of the game. The main entry point is getRollResult that uses its gameState parameter to decide the result of the turn. It handles simulating a roll of two dice and the action that is the result of that combination. It ultimately returns an updated GameState instance as the result that is used as input for the next turn as well as being used to draw the current state using p5.js.

There was much care in defining the actions and results based on the current state. For example; if there are 2 outs and runner on second based then a single will score that runner. If there are less than 2 outs, a single will just advance the runner 1 base. Another example is that if there are less than 2 outs, a runner on 3rd based, and someone hits a fly ball, that will result in a sacrafice fly where the runner from third scores.

##### sketch.js
sketch.js provides the user interface logic for the game. It draws the current state of the game in a game loop, draw(), defined by the p5.js framework. The scoreboard, runners on base, the textual result of a turn, and whether or not the game is over is all drawn by hand in this file.

##### app.py
app.py is a boilerplate implementation of a Flask application. It simply loads the Index.html template.

```
from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

##### Index.html
Index.html provides the HTML layout for hosting the p5.js application. It uses bootstrap for ease in styling the layout.

##### Final thoughts
This was a fun project! I had no prior experience with p5.js and still have a lot to learn about it but was able to fairly easily implement the game interface with it. There is a lot to learn about best coding practices and I will definitely be exploring that further. My design choice of having a game state separate from a game manager definitely paid off as it was easy to hand off a current state to p5.js for drawing purposes. This allowed for a clean separation of the two which resulted in fairly clean p5.js code. The p5.js code is still a little messy but it would be way worse if I included the game flow inside of the sketch.

