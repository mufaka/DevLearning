var g_gameState;
var g_gameManager;
var back;
var baseRunner;
var button;

function preload() {
    back = loadImage("static/img/field.svg")
    baseRunner = loadImage("static/img/baseball-player.png")
}

function setup() {
    let canvas = createCanvas(800, 600);
    canvas.parent("game")
    // TODO: is there a way to pass in a GameState?
    g_gameState = new GameState('Player 2', 'Player 1', false);
    g_gameManager = new GameManager();

    // can we preload a font?
    textFont('Roboto');

    button = createButton('Roll Dice');
    // button.parent("defaultCanvas0"); <-- this doesn't work because the canvas hasn't been drawn?
    button.parent("game");

    let parentRect = document.getElementById('game').getBoundingClientRect();

    // the canvas is centered inside of the parent. need to offset the button x and y because it 
    // is a DOM element, not a canvas element. can we just get the canvas x position?
    button.position(361 + ((parentRect.right - parentRect.left - 800)  / 2), 500);
    button.mousePressed(() => {
        g_gameState = g_gameManager.getRollResult(g_gameState);
    });
}

function draw() {
    background(back);
    renderGameState(g_gameState);
}

function renderGameState(gamestate) {
    drawScoreBoard(gamestate);
    drawBaseRunners(gamestate);
    drawRollResult(gamestate);

    fill('black')
    //textFont('Roboto');
    textSize(24);

    let currentPlayer = gamestate.currentPlayer == '' ? gamestate.awayPlayer : gamestate.currentPlayer;
    text('Batting: ' + currentPlayer, 310, 550);
}

function drawRollResult(gamestate) {
    if (gamestate.lastRoll1 > 0) {
        drawDice(200, 150, gamestate.lastRoll1);
        drawDice(230, 150, gamestate.lastRoll2);
        fill('white')
        textFont('Roboto');
        textSize(24);
        text(gamestate.lastRollAction, 270, 168);
    }

    if (gamestate.gameStatus == 1) {
        textSize(44);
        text("Game Over!", 275, 300);
        button.hide();
    }
}

function drawDice(x, y, roll) {
    textSize(16)
    fill('black');
    rect(x, y, 25, 25, 5);
    fill(255);
    rect(x - 2, y - 2, 25, 25, 5);
    stroke(0);
    fill(255, 0, 0);
    text(roll, x + 6, y + 16);
}

function drawBaseRunners(gamestate) {
    // first base
    if (gamestate.base1Occupied) {
        drawBaseRunner(560, 395)
    }

    // second base
    if (gamestate.base2Occupied) {
        drawBaseRunner(385, 310)
    }

    // third base
    if (gamestate.base3Occupied) {
        drawBaseRunner(185, 395)
    }
}

function drawScoreBoard(gamestate) {
    // define some relative coords for scoreboard
    // changing these should move all elements below
    let scoreboardX = 185;
    let scoreboardY = 10;
    let teamNameWidth = 125;
    let padding = 2;
    let cellHeight = 18;
    let cellWidth = 18;

    // draw team names
    // smoky black
    fill(26,17,0);
    rect(scoreboardX, scoreboardY + (1 * (cellHeight + padding)), teamNameWidth, cellHeight)
    rect(scoreboardX, scoreboardY + (2 * (cellHeight + padding)), teamNameWidth, cellHeight)

    textSize(16);
    fill('yellow');
    text(gamestate.awayPlayer, scoreboardX + 4, scoreboardY + (1 * (cellHeight + padding)) + 14);
    text(gamestate.homePlayer, scoreboardX + 4, scoreboardY + (2 * (cellHeight + padding)) + 14);

    // draw the inning numbers
    for (i = 0; i < 9; i++) {
        fill(26,17,0);
        let x = scoreboardX + teamNameWidth + padding + (i * (cellWidth + padding));
        rect(x, scoreboardY, cellWidth, cellHeight);

        textSize(16);
        fill('yellow');
        text(i + 1, x + 4, 24);
    }

    // draw the away inning scores
    for (i = 0; i < 9; i++) {
        // smoky black
        fill(26,17,0);
        let x = scoreboardX + teamNameWidth + padding + (i * (cellWidth + padding));
        rect(x, scoreboardY + (1 * (cellHeight + padding)), cellWidth, cellHeight);

        if (gamestate.awayScores[i] > -1) {
            textSize(8);
            fill('white');
            text(gamestate.awayScores[i], x + 4, scoreboardY + (1 * (cellHeight + padding)) + 12);
        }
    }

    // draw the home inning scores
    for (i = 0; i < 9; i++) {
        // smoky black
        fill(26,17,0, 255);
        let x = scoreboardX + teamNameWidth + padding + (i * (cellWidth + padding));
        rect(x, scoreboardY + (2 * (cellHeight + padding)), cellWidth, cellHeight);

        if (gamestate.homeScores[i] > -1) {
            textSize(8);
            fill('white');
            text(gamestate.homeScores[i], x + 4, scoreboardY + (2 * (cellHeight + padding)) + 12);
        }
    }

    // draw the total scores
    fill(26,17,0, 255);
    rect(scoreboardX + teamNameWidth + padding + (9 * (cellWidth + padding)), scoreboardY, cellWidth, cellHeight);
    rect(scoreboardX + teamNameWidth + padding + (10 * (cellWidth + padding)), scoreboardY, cellWidth, cellHeight);
    textSize(16);
    fill('yellow');
    text('R', scoreboardX + teamNameWidth + padding + (10 * (cellWidth + padding)) + padding, 24);

    fill(26,17,0, 255);
    rect(scoreboardX + teamNameWidth + padding + (9 * (cellWidth + padding)), scoreboardY + (1 * (cellHeight + padding)) , cellWidth, cellHeight);
    rect(scoreboardX + teamNameWidth + padding + (10 * (cellWidth + padding)), scoreboardY + (1 * (cellHeight + padding)), cellWidth, cellHeight);

    fill(26,17,0, 255);
    rect(scoreboardX + teamNameWidth + padding + (9 * (cellWidth + padding)), scoreboardY + (2 * (cellHeight + padding)), cellWidth, cellHeight);
    rect(scoreboardX + teamNameWidth + padding + (10 * (cellWidth + padding)), scoreboardY + (2 * (cellHeight + padding)), cellWidth, cellHeight);

    // stroke(r, g, b) for border color
    // stroke(127, 63, 120);
    textSize(8);
    fill('white');
    text(gamestate.awayScore, scoreboardX + teamNameWidth + padding + (10 * (cellWidth + padding)) + padding, scoreboardY + (1 * (cellHeight + padding)) + 12);
    text(gamestate.homeScore, scoreboardX + teamNameWidth + padding + (10 * (cellWidth + padding)) + padding, scoreboardY + (2 * (cellHeight + padding)) + 12);

    fill(26,17,0, 255);
    rect(scoreboardX + teamNameWidth + padding + (7 * (cellWidth + padding)), scoreboardY + (3 * (cellHeight + padding)), 4 * (cellWidth + padding) - padding, cellHeight);

    textSize(12);
    fill('white');
    text("Outs:", scoreboardX + teamNameWidth + padding + (7 * (cellWidth + padding) + padding), scoreboardY + (3 * (cellHeight + padding)) + 12);

    // just need to indicate 2 outs. third out resets
    // the next half inning
    if (gamestate.currentOuts > 0) {
        fill('yellow');
        circle(scoreboardX + teamNameWidth + padding + (7 * (cellWidth + padding) + padding) + 40, scoreboardY + (3 * (cellHeight + padding)) + 8, 8)    
    }

    if (gamestate.currentOuts > 1) {
        fill('yellow');
        circle(scoreboardX + teamNameWidth + padding + (7 * (cellWidth + padding) + padding) + 50, scoreboardY + (3 * (cellHeight + padding)) + 8, 8)
    }
}

function drawBaseRunner(x, y) {
    // players are in a rectangle starting with top left being at x, y
    image(baseRunner, x, y, 50, 50);
}

