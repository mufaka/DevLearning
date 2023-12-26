var gameState = new GameState('Bill', 'Ken', false);
var gameManager = new GameManager();

/*
var fieldCanvas = $('#field-canvas')[0];
var fieldCanvas2DContext = fieldCanvas.getContext('2d');
var fieldImage = new Image();
fieldImage.onload = function() {
    fieldCanvas2DContext.drawImage(fieldImage, 0, 0);
};
fieldImage.src = 'static/img/field.svg';
*/

window.onresize = function() {
    this.fieldCanvas.style.width = '50%';
    this.fieldCanvas.style.height = '75%';
    fieldCanvas2DContext.drawImage(fieldImage, 0, 0);
}

function drawGameState(gameState) {
    var homeScore = gameState.homeScore;
    var awayScore = gameState.awayScore;

    $('#hn').text(gameState.homePlayer);
    $('#an').text(gameState.awayPlayer);

    if (gameState.homePlayer == gameState.currentPlayer) {
        $('#hn').css('font-weight', 'Bold');
        $('#an').css('font-weight', 'Normal');
    } else {
        $('#hn').css('font-weight', 'Normal');
        $('#an').css('font-weight', 'Bold');
    }

    $('#ht').text(homeScore);
    $('#at').text(awayScore);

    $('#inning').text(gameState.currentInning + 1);

    var x;
    for (x = 0; x < gameState.homeScores.length; x++) {

        if (x <= gameState.currentInning) {
            var inningScore = gameState.homeScores[x];
            if (inningScore == -1) {
                inningScore = 0;
            }
            $('#h' + x).text(inningScore);
        }
    }

    for (x = 0; x < gameState.awayScores.length; x++) {

        if (x <= gameState.currentInning) {
            var inningScore = gameState.awayScores[x];
            if (inningScore == -1) {
                inningScore = 0;
            }
            $('#a' + x).text(inningScore);
        }
    }

    if (gameState.base1Occupied) {
        $('#base1').text('Base Runner');
    } else {
        $('#base1').html('&nbsp;');
    }

    if (gameState.base2Occupied) {
        $('#base2').text('Base Runner');
    } else {
        $('#base2').html('&nbsp;');
    }

    if (gameState.base3Occupied) {
        $('#base3').text('Base Runner');
    } else {
        $('#base3').html('&nbsp;');
    }

    if (gameState.currentOuts == 3) {
        $('#o1').text('X');
        $('#o2').text('X');
        $('#o3').text('X');
    } else if (gameState.currentOuts == 2) {
        $('#o1').text('X');
        $('#o2').text('X');
        $('#o3').text('');
    } else if (gameState.currentOuts == 1) {
        $('#o1').text('X');
        $('#o2').text('');
        $('#o3').text('');
    } else {
        $('#o1').text('');
        $('#o2').text('');
        $('#o3').text('');
    }

    if (gameState.lastRoll1 != -1) {
        if (gameState.gameStatus == 1) {
            $('#result').text(gameState.lastRoll1 + ' ' + gameState.lastRoll2 + ' - ' + gameState.lastRollAction + ' - Game Over.');
            $('#roll_dice').prop('disabled', true);
        } else {
            $('#result').text(gameState.lastRoll1 + ' ' + gameState.lastRoll2 + ' - ' + gameState.lastRollAction);
        }
    }
}

$(function() {
    drawGameState(gameState);
});

function roll(gameState) {
    gameState = gameManager.getRollResult(gameState);
    updateGameState(gameState);
}

function rollDice() {
    roll(gameState);
}
