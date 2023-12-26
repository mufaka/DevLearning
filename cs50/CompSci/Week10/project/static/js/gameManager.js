class GameManager {
    getRollResult(gameState) {

        if (gameState.gameStatus == -1) {
            gameState.gameStatus = 0;
        } else if (gameState.gameStatus == 1) {
            // game is over
            return gameState;
        }

        var rollResult1 = Math.floor(Math.random() * 6) + 1;
        var rollResult2 = Math.floor(Math.random() * 6) + 1;

        gameState.lastRoll1 = rollResult1;
        gameState.lastRoll2 = rollResult2;

        var firstDice = rollResult1 <= rollResult2 ? rollResult1 : rollResult2;
        var secondDice = rollResult1 > rollResult2 ? rollResult1 : rollResult2;

        var resultKey = firstDice + '' + secondDice;

        switch (resultKey) {
            case '11':
            case '66':
                return this.actionHomeRun(gameState);
            case '12':
            case '55':
                return this.actionDouble(gameState);
            case '13':
            case '36':
                return this.actionFlyOut(gameState);
            case '14':
            case '33':
            case '44':
                return this.actionWalk(gameState);
            case '15':
            case '45':
                return this.actionPopOut(gameState);
            case '16':
            case '25':
                return this.actionSingle(gameState);
            case '22':
                return this.actionDoublePlay(gameState);
            case '23':
            case '35':
                return this.actionGroundOut(gameState);
            case '24':
            case '26':
            case '46':
                return this.actionStrikeOut(gameState);
            case '34':
                return this.actionTriple(gameState);
            case '56':
                return this.actionSacrificeFly(gameState);
        }

        gameState.lastRollAction = 'Invalid roll. ' + resultKey;
        return gameState;

    }

    actionScoreRun = function(gameState, runsScored) {
        if (gameState.currentPlayer == gameState.player1) {
            var newScore = gameState.player1Scores[gameState.currentInning] + runsScored;
            gameState.player1Scores[gameState.currentInning] = newScore;
        }
        else {
            var newScore = gameState.player2Scores[gameState.currentInning] + runsScored;
            gameState.player2Scores[gameState.currentInning] = newScore;
        }

        // was this a walk off?
        if (gameState.currentInning >= 8) { // zero based
            var player1Score = gameState.player1Score;
            var player2Score = gameState.player2Score;

            if (gameState.currentPlayer == gameState.player1) {
                if (gameState.player1IsHome) {
                    if (player1Score > player2Score) {
                        gameState.lastRollAction = "Walk Off " + gameState.lastRollAction;
                        gameState.gameStatus = 1; // game over
                    }
                }
            } else { // current player is player2
                if (!gameState.player1IsHome) { // player2 is home
                    if (player2Score > player1Score) { // player2 has more runs than player1 now
                        gameState.lastRollAction = "Walk Off " + gameState.lastRollAction;
                        gameState.gameStatus = 1; // game over
                    }
                } 
            }
        }
        return gameState;
    };

    actionRecordOut = function(gameState, outs) {
        gameState.currentOuts += outs;

        if (gameState.currentOuts >= 3) {
            gameState.lastRollAction += '. Inning over.';
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = false;

            if (gameState.currentInning >= 8) { // zero based
                var player1Score = gameState.player1Score;
                var player2Score = gameState.player2Score;

                // see if we are in the bottom of the last inning and not tied
                if (gameState.currentPlayer == gameState.player1) {
                    if (gameState.player1IsHome) {
                        if (player1Score != player2Score) {
                            gameState.gameStatus = 1; // game over
                            return gameState;
                        }
                    }
                } else { // current player is player2
                    if (!gameState.player1IsHome) { // player2 is home
                        if (player2Score != player1Score) {
                            gameState.gameStatus = 1; // game over
                            return gameState;
                        }
                    } else { // top of last inning, player 1 is home
                        if (player1Score > player2Score) {
                            gameState.gameStatus = 1; // game over
                            return gameState;
                        }
                    }
                }
            }

            // swap players and possibly inning
            if (gameState.currentPlayer == gameState.player1) {
                gameState.currentPlayer = gameState.player2;
                if (gameState.player1IsHome) {
                    if (gameState.currentInning < 8) { // play the 9th inning until winner determined
                        gameState.currentInning = gameState.currentInning + 1;
                    }
                }
            } else {
                gameState.currentPlayer = gameState.player1;
                if (!gameState.player1IsHome) {
                    if (gameState.currentInning < 8) {
                        gameState.currentInning = gameState.currentInning + 1;
                    }
                }
            }

            if (gameState.player1Scores[gameState.currentInning] == -1) {
                gameState.player1Scores[gameState.currentInning] = 0;
            }

            if (gameState.player2Scores[gameState.currentInning] == -1) {
                gameState.player2Scores[gameState.currentInning] = 0;
            }

            gameState.currentOuts = 0;
        }
        return gameState;
    };

    actionHomeRun = function(gameState) {
        gameState.lastRollAction = 'Home Run!';
        
        var runsScored = 1;

        if (gameState.base1Occupied) {
            runsScored += 1;
            gameState.base1Occupied = false;
        }

        if (gameState.base2Occupied) {
            runsScored += 1;
            gameState.base2Occupied = false;
        }

        if (gameState.base3Occupied) {
            runsScored += 1;
            gameState.base3Occupied = false;
        }

        return this.actionScoreRun(gameState, runsScored);
    };

    actionDouble = function(gameState) {
        gameState.lastRollAction = 'Double';
        
        if (!gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // no one one
            gameState.base2Occupied = true;
            return gameState;
        } else if (gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first only
            // if there are 2 outs, runner will score because he is going on contact
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = false;
                return this.actionScoreRun(gameState, 1);
            } else {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = true; // runner from first
                return gameState;
            }
        } else if (!gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on second only
            // runner on second scores, batter on second
            gameState.base1Occupied = false;
            gameState.base2Occupied = true;
            gameState.base3Occupied = false;
            return this.actionScoreRun(gameState, 1);
        } else if (!gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on third only
            gameState.base1Occupied = false;
            gameState.base2Occupied = true;
            gameState.base3Occupied = false; // runner scored
            return this.actionScoreRun(gameState, 1);
        } else if (gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first and second only
            // if there are 2 outs, both runners will score
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = false;
                return this.actionScoreRun(gameState, 2);
            } else {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = true; // runner from first
                return this.actionScoreRun(gameState, 1);
            }
        } else if (gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on first and third only
            // if there are 2 outs, both runners will score
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = false;
                return this.actionScoreRun(gameState, 2);
            } else {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = true; // runner from first
                return this.actionScoreRun(gameState, 1);
            }
        } else if (!gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // man on second and third only
            gameState.base1Occupied = false;
            gameState.base2Occupied = true; // batter
            gameState.base3Occupied = false; // runs scored from second and third
            return this.actionScoreRun(gameState, 2);
        } else if (gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // bases loaded
            // if there are 2 outs, all runners score
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = false;
                return this.actionScoreRun(gameState, 3);
            } else {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true; // batter
                gameState.base3Occupied = true; // runner from first
                return this.actionScoreRun(gameState, 2);
            }
        } else {
            // shouldn't get here
            gameState.base1Occupied = false;
            gameState.base2Occupied = true; // batter
            gameState.base3Occupied = false; 
            return gameState;
        }
    };

    actionFlyOut = function(gameState) {
        gameState.lastRollAction = 'Fly Out';
        return this.actionRecordOut(gameState, 1);
    };

    actionWalk = function(gameState) {
        gameState.lastRollAction = "Walk";
        if (!gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // no one one
            gameState.base1Occupied = true;
            return gameState;
        } else if (gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first only
            gameState.base1Occupied = true;
            gameState.base2Occupied = true;
            gameState.base3Occupied = false;
            return gameState;
        } else if (!gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on second only
            gameState.base1Occupied = true;
            gameState.base2Occupied = true;
            gameState.base3Occupied = false;
            return gameState;
        } else if (!gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on third only
            gameState.base1Occupied = true;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return gameState;
        } else if (gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first and second only
            gameState.base1Occupied = true;
            gameState.base2Occupied = true;
            gameState.base3Occupied = true;
            return gameState;
        } else if (gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on first and third only
            gameState.base1Occupied = true;
            gameState.base2Occupied = true;
            gameState.base3Occupied = true;
            return gameState;
        } else if (!gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // man on second and third only
            gameState.base1Occupied = true;
            gameState.base2Occupied = true;
            gameState.base3Occupied = true;
            return gameState;
        } else if (gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // bases loaded
            gameState.base1Occupied = true;
            gameState.base2Occupied = true;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 1);
        } else {
            // shouldn't get here
            gameState.base1Occupied = true;
            gameState.base2Occupied = false;
            gameState.base3Occupied = false;
            return gameState;
        }
    };

    actionPopOut = function(gameState) {
        gameState.lastRollAction = 'Pop Out';
        return this.actionRecordOut(gameState, 1);
    };

    actionSingle = function(gameState) {
        gameState.lastRollAction = 'Single';
        if (!gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // no one one
            gameState.base1Occupied = true;
            gameState.base2Occupied = false;
            gameState.base3Occupied = false;
            return gameState;
        } else if (gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first only
            gameState.base1Occupied = true;
            gameState.base2Occupied = true;
            gameState.base3Occupied = false;
            return gameState;
        } else if (!gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on second only
            // if 2 outs, runner on second scores
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = false;
                return this.actionScoreRun(gameState, 1);
            } else {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = true;
                return gameState;
            }
        } else if (!gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on third only
            gameState.base1Occupied = true;
            gameState.base2Occupied = false;
            gameState.base3Occupied = false;
            return this.actionScoreRun(gameState, 1);
        } else if (gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first and second only
            // if 2 outs, runners advance 2 bases
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = true;
                return this.actionScoreRun(gameState, 1);
            } else {
                gameState.base1Occupied = true;
                gameState.base2Occupied = true;
                gameState.base3Occupied = true;
                return gameState;
            }
        } else if (gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on first and third only
            // if 2 outs, runners advance 2 bases
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = true;
                return this.actionScoreRun(gameState, 1);
            } else {
                gameState.base1Occupied = true;
                gameState.base2Occupied = true;
                gameState.base3Occupied = false;
                return this.actionScoreRun(gameState, 1);
            }
        } else if (!gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // man on second and third only
            // if 2 outs, runners advance 2 bases
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = false;
                return this.actionScoreRun(gameState, 2);
            } else {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = true;
                return this.actionScoreRun(gameState, 1);
            }
        } else if (gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // bases loaded
            if (gameState.currentOuts == 2) {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = true;
                return this.actionScoreRun(gameState, 2);
            } else {
                gameState.base1Occupied = true;
                gameState.base2Occupied = true;
                gameState.base3Occupied = true;
                return this.actionScoreRun(gameState, 1);
            }
        } else {
            // shouldn't get here
            gameState.base1Occupied = true;
            gameState.base2Occupied = false;
            gameState.base3Occupied = false;
            return gameState;
        }
    };

    actionDoublePlay = function(gameState) {
        if (gameState.currentOuts < 2) {
            if (!gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
                // no one one
                gameState.lastRollAction = 'Ground Out';
                return this.actionRecordOut(gameState, 1);
            } else if (gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
                // man on first only
                gameState.lastRollAction = 'Double Play';
                gameState.base1Occupied = false;
                return this.actionRecordOut(gameState, 2);
            } else if (!gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
                // man on second only
                gameState.lastRollAction = 'Ground Out';
                return this.actionRecordOut(gameState, 1);
            } else if (!gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
                // man on third only
                gameState.lastRollAction = 'Ground Out';
                return this.actionRecordOut(gameState, 1);
            } else if (gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
                // man on first and second only
                gameState.lastRollAction = 'Double Play';
                gameState.base2Occupied = false;
                return this.actionRecordOut(gameState, 2);
            } else if (gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
                // man on first and third only
                gameState.lastRollAction = 'Line Out, Doubled Off 3rd';
                if (gameState.currentOuts == 1) {
                    return this.actionRecordOut(gameState, 2);
                } else {
                    gameState.base1Occupied = true; // runner didn't advance
                    gameState.base2Occupied = false; // no runner advanced
                    gameState.base3Occupied = false; // doubled off
                    return this.actionRecordOut(gameState, 2);
                }
            } else if (!gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
                // man on second and third only
                gameState.lastRollAction = 'Line Out, Doubled Off 3rd';
                if (gameState.currentOuts == 1) {
                    return this.actionRecordOut(gameState, 2);
                } else {
                    gameState.base1Occupied = false; // batter out
                    gameState.base2Occupied = false; // no runner advanced
                    gameState.base3Occupied = false; // doubled off
                    return this.actionRecordOut(gameState, 2);
                }
            } else if (gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
                // bases loaded
                gameState.lastRollAction = 'Double Play';
                gameState.base1Occupied = true; // batter advances
                gameState.base2Occupied = true; // first base advances
                gameState.base3Occupied = false; // runner out at home and third.
                return this.actionRecordOut(gameState, 2);
            } else {
                // shouldn't get here
                gameState.lastRollAction = 'Double Play';
                gameState.base1Occupied = false;
                gameState.base2Occupied = false;
                gameState.base3Occupied = false;
                return this.actionRecordOut(gameState, 2);
            }
        } else {
            // ground out, 3rd out.
            gameState.lastRollAction = "Ground Out";
            return this.actionRecordOut(gameState, 1);
        }
    };

    actionGroundOut = function(gameState) {
        // TODO: determine where the grounder was hit (left or right, coin flip)
        // TODO: so that we can determine which runners were out and if a runner
        // TODO: could advance. (eg: only runner on 3rd. ball hit left would hold runner
        // TODO: and get out at first. ball hit right would score runner and out at first)
        gameState.lastRollAction = 'Ground Out';
        if (!gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // no one one
            return this.actionRecordOut(gameState, 1);
        } else if (gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first only
            if (gameState.currentOuts < 2) {
                gameState.lastRollAction = 'Fielders Choice';
            } else {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true;
            }
            return this.actionRecordOut(gameState, 1);
        } else if (!gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on second only
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionRecordOut(gameState, 1);
        } else if (!gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on third only
            // TODO: this depends on where the ball was hit
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionRecordOut(gameState, 1);
        } else if (gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first and second only
            // TODO: this depends on where the ball was hit
            return this.actionRecordOut(gameState, 1);
        } else if (gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on first and third only
            // TODO: this depends on where the ball was hit
            return this.actionRecordOut(gameState, 1);
        } else if (!gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // man on second and third only
            // TODO: this depends on where the ball was hit
            return this.actionRecordOut(gameState, 1);
        } else if (gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // bases loaded
            return this.actionRecordOut(gameState, 1);
        } else {
            // shouldn't get here
            return this.actionRecordOut(gameState, 1);
        }
    };

    actionStrikeOut = function(gameState) {
        gameState.lastRollAction = "Strike Out";
        return this.actionRecordOut(gameState, 1);
    };

    actionTriple = function(gameState) {
        gameState.lastRollAction = 'Triple';
        if (!gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // no one one
            gameState.base3Occupied = true;
            return gameState;
        } else if (gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first only
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 1);
        } else if (!gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on second only
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 1);
        } else if (!gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on third only
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 1);
        } else if (gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first and second only
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 2);
        } else if (gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on first and third only
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 2);
        } else if (!gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // man on second and third only
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 2);
        } else if (gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // bases loaded
            gameState.base1Occupied = false;
            gameState.base2Occupied = false;
            gameState.base3Occupied = true;
            return this.actionScoreRun(gameState, 3);
        } else {
            // shouldn't get here
            gameState.base3Occupied = true;
            return gameState;
        }
    };

    actionSacrificeFly = function(gameState) {
        gameState.lastRollAction = 'Fly Out';
        if (!gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // no one one
            return this.actionRecordOut(gameState, 1);
        } else if (gameState.base1Occupied && !gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first only
            return this.actionRecordOut(gameState, 1);
        } else if (!gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on second only
            return this.actionRecordOut(gameState, 1);
        } else if (!gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on third only
            if (gameState.currentOuts < 2) {
                gameState.base1Occupied = false;
                gameState.base2Occupied = false;
                gameState.base3Occupied = false;
                gameState.lastRollAction = 'Sacrifice Fly';
                gameState = this.actionScoreRun(gameState, 1);
            }
            return this.actionRecordOut(gameState, 1); 
        } else if (gameState.base1Occupied && gameState.base2Occupied && !gameState.base3Occupied) {
            // man on first and second only
            return this.actionRecordOut(gameState, 1);
        } else if (gameState.base1Occupied && !gameState.base2Occupied && gameState.base3Occupied) {
            // man on first and third only
            if (gameState.currentOuts < 2) {
                gameState.base1Occupied = true;
                gameState.base2Occupied = false;
                gameState.base3Occupied = false;
                gameState.lastRollAction = 'Sacrifice Fly';
                gameState = this.actionScoreRun(gameState, 1);
            }
            return this.actionRecordOut(gameState, 1); 
        } else if (!gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // man on second and third only
            if (gameState.currentOuts < 2) {
                gameState.base1Occupied = false;
                gameState.base2Occupied = true;
                gameState.base3Occupied = false;
                gameState.lastRollAction = 'Sacrifice Fly';
                gameState = this.actionScoreRun(gameState, 1);
            }
            return this.actionRecordOut(gameState, 1); 
        } else if (gameState.base1Occupied && gameState.base2Occupied && gameState.base3Occupied) {
            // bases loaded
            if (gameState.currentOuts < 2) {
                gameState.base1Occupied = true;
                gameState.base2Occupied = true;
                gameState.base3Occupied = false;
                gameState.lastRollAction = 'Sacrifice Fly';
                gameState = this.actionScoreRun(gameState, 1);
            }
            return this.actionRecordOut(gameState, 1); 
        } else {
            // shouldn't get here
            return this.actionRecordOut(gameState, 1);
        }
    };
}