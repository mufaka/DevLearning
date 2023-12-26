class GameState {
	gameStatus = -1; // -1 = not started, 0 = in progress, 1 = game over

    player1 = '';
    player2 = '';
    player2IsAi = true;
    player1IsHome = true;
    player1Scores = [];
    player2Scores = [];

    lastRoll1 = -1;
    lastRoll2 = -1;
    lastRollAction = '';

    currentInning = 0;
    currentPlayer = '';
    currentOuts = 0;

    base1Occupied = false;
    base2Occupied = false;
    base3Occupied = false;

    constructor(player1, player2, player2IsAi) {
        this.player1 = player1;
        this.player2 = player2;
        this.player2IsAi = player2IsAi;

        var x;
        for (x = 1; x < 9; x++) {
            this.player1Scores[x] = -1;
            this.player2Scores[x] = -1;
        }
        this.player1Scores[0] = 0;
        this.player2Scores[0] = 0;
    }

    get homePlayer() {
        if (this.player1IsHome) {
            return this.player1;
        } else {
            return this.player2;
        }
    }

    get awayPlayer() {
        if (!this.player1IsHome) {
            return this.player1;
        } else {
            return this.player2;
        }
    }

    get homeScore() {
        if (this.player1IsHome) {
            return this.player1Score;
        } else {
            return this.player2Score;
        }
    }

    get awayScore() {
        if (!this.player1IsHome) {
            return this.player1Score;
        } else {
            return this.player2Score;
        }
    }

    get homeScores() {
        if (this.player1IsHome) {
            return this.player1Scores;
        } else {
            return this.player2Scores;
        }
    }

    get awayScores() {
        if (!this.player1IsHome) {
            return this.player1Scores;
        } else {
            return this.player2Scores;
        }
    }

    get player1Score() {
        var score = 0;

        var x;
        for (x = 0; x < this.player1Scores.length; x++) {
            var inningScore = this.player1Scores[x];
            if (inningScore > 0) {
                score += inningScore;
            }
        }

        return score;
    }

    get player2Score() {
        var score = 0;

        var x;
        for (x = 0; x < this.player2Scores.length; x++) {
            var inningScore = this.player2Scores[x];
            if (inningScore > 0) {
                score += inningScore;
            }
        }

        return score;
    }
}