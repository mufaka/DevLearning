// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// compiler complaining about using N variable below
// "variably modified 'table' at file scope"
// most likely an issue with gcc makefile
// #define NUM_BUCKETS 17575

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17575;

// Keep track of the word count as they are added
// so that we don't need to iterate the list each
// time count is called
unsigned int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int word_hash = hash(word);

    // get the list from the table
    node *word_list = table[word_hash];

    // if (word_list != NULL)
    while (word_list != NULL)
    {
        // strcasecmp is in gcc but not clang ..., need strings.h
        if (strcasecmp(word, word_list->word) == 0)
        {
            return true;
        }

        word_list = word_list->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    /*
        use base 26 for first 3 letters of the word for the hash?
        Z = 0, A = 1, B = 2, C = 3 ... Y = 25
    */
    int hash = 0;

    for (int i = 0; i < 3; i++)
    {
        if (word[i] == '\0')
        {
            break;
        }

        // see note in 'load' about seg fault on non-alpha
        if (!isalpha(word[i])) 
        {
            continue;
        }

        int h1 = toupper(word[i]) - 'A' + 1;
        int factor = pow(26, i);

        // if bigger than Y, assume Z (0)
        if (h1 > 25) 
        {
            h1 = 0;
        }

        hash += factor * h1;
    }

    return hash;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // read the dictionary file and populate the dictionary for
    // each word
    FILE *file = fopen(dictionary, "r");

    if (!file)
    {
        return false;
    }

    // create a buffer to read lines into
    char line[LENGTH + 1];
    int line_count = 0;

    while (fgets(line, LENGTH + 1, file))
    {
        line_count++;
        // skip empty lines
        if (line[0] == '\n') 
        {
            continue;
        }

        // line has the \n character, need to remove that but keep terminator ...
        int last_index = strlen(line) - 1;

        if (line[last_index] == '\n')
        {
            line[last_index] = '\0';
        }

        // create a new node
        node *word_node = malloc(sizeof(node));
        
        /*
        if (strlen(line) == 1)
        {
            printf("Adding %s to dictionary from line %i.\n", line, line_count);
        }
        */
        /*
        .
        .
        .
        Adding al's to dictionary. <-- hashing on an apostrophe causes seg fault.
        Segmentation fault

        // for some reason we are getting s in the dictionary ... LINE buff was 1 too short ...
        // for pneumonoultramicroscopicsilicovolcanoconiosis
        Adding a to dictionary.
        Adding i to dictionary.
        Adding s to dictionary.
        
        s's is in dictionary
        */

        // need to copy into the node
        strcpy(word_node->word, line);

        // get the hash for the word
        int word_hash = hash(word_node->word);

        // set next to whatever is currently in the table
        // NOTE: if there is nothing there, this still works
        //       because this will signify that it's the last
        //       item in the list
        word_node->next = table[word_hash];

        // set the word to the first in the list
        table[word_hash] = word_node;

        word_count++;
    }

    // printf("Added %i words to dictionary.\n", word_count);

    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    // loop through the table and free all from the list. same loop as checking 
    // for the word
    // for (int word_hash = 0; word_hash < NUM_BUCKETS; word_hash++)
    for (int word_hash = 0; word_hash < N; word_hash++)
    {
        node *word_list = table[word_hash];
        node *next_word = word_list;

        // if (word_list != NULL)
        while (word_list != NULL)
        {
            // we can't free the beginning of the list
            // because we will lose the pointer to next
            // so, capture the next one, free the current one,
            // then set the word list to the captured one
            next_word = word_list->next;
            free(word_list);
            word_list = next_word;
        }
    }

    return true;
}
