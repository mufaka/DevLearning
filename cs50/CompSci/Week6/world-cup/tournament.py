# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 10000


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    counts = {}

    # TODO: Read teams into memory from file
    with open(sys.argv[1], "r") as file:
        """
        team,rating
        Uruguay,976
        """
        reader = csv.DictReader(file)
        for row in reader:
            team = {}
            team["team"] = row["team"]
            team["rating"] = int(row["rating"])
            teams.append(team)
            counts[row["team"]] = 0

    # TODO: Simulate N tournaments and keep track of win counts
    for r in range(N):
        winner = simulate_tournament(teams)
        counts[winner] += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""

    """
    The order in which the teams are listed determines which teams will play 
    each other in each round (in the first round, for example, Uruguay 
    will play Portugal and France will play Argentina; in the next round, 
    the winner of the Uruguay-Portugal match will play the winner of the 
    France-Argentina match). So be sure not to edit the order in which 
    teams appear in this file!    
    """
    # TODO
    # define winners for the round, call simulate_round until 1 winner
    # all winners from group stage
    winners = teams 

    while len(winners) > 1:
        winners = simulate_round(winners)

    return winners[0]["team"]


if __name__ == "__main__":
    main()
