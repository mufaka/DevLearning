#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
// Per spec, we can't add margin of victory here :(
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool find_cycle(int winner, int loser);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            // ranks is an array for each voter. 
            ranks[rank] = i;
            return true;
        }
    }

    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // preferences[i][j] is number of voters who prefer i over j
    // so, iterate the array. 0 -> 1, 0 -> 2, 1 -> etc.
    for (int i = 0; i < candidate_count; i++)
    {
        // NOTE: if i is last index, this for condition won't run (expected, last candidate isn't preferred)
        for (int j = i + 1; j < candidate_count; j++) 
        {
            // increment the position in ranks
            preferences[ranks[i]][ranks[j]] += 1;
        }
    }

    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // create pairs from preferences
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            // only record pair if winner/loser (no ties)
            if (preferences[i][j] != preferences[j][i])
            {
                pairs[pair_count].winner = preferences[i][j] > preferences[j][i] ? i : j;
                pairs[pair_count].loser = preferences[i][j] > preferences[j][i] ? j : i;
                pair_count += 1;
            }
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // bubble sort the pairs
    for (int i = 0; i < pair_count - 1; ++i)
    {
        for (int j = 0; j < pair_count - i - 1; ++i)
        {
            int pref1 = preferences[pairs[j].winner][pairs[j].loser];
            int pref2 = preferences[pairs[j + 1].winner][pairs[j + 1].loser];

            if (pref1 < pref2) 
            {
                // swap so bigger one is before
                pair swap = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = swap;
            }
        }
    }

    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // we have a list of pairs that are sorted in order of biggest margin of victory.
    // locking means that there is no cycle where a > b > c > a
    for (int i = 0; i < pair_count; i++) 
    {
        // if this pair would create a cycle, don't lock (draw an arror / create an edge)
        if (!find_cycle(pairs[i].winner, pairs[i].loser)) 
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }

    return;
}

bool find_cycle(int winner, int loser)
{
    // if there is already a lock for the loser to the winner, return
    if (locked[loser][winner])
    {
        return true;
    }

    // if the test pair is already locked, don't bother
    // is there a lock where the loser of the test pair wins 
    // against a winner between the test_pair winner?
    // have to look at all candidates here "lock_pairs did not correctly lock all non-cyclical pairs"
    for (int i = 0; i < candidate_count; i++) 
    {
        if (locked[loser][i] && find_cycle(winner, i))
        {
            return true;
        }
    }

    return false;
}

// Print the winner of the election
void print_winner(void)
{
    // The winner is the one and only case where an edge isn't pointing
    for (int i = 0; i < candidate_count; i++)
    {
        bool edge_found = false;

        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i]) 
            {
                edge_found = true;
                break;
            }
        }

        if (!edge_found)
        {
            printf("%s\n", candidates[i]);
            break;
        }
    }

    return;
}
