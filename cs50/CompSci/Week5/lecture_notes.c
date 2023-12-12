#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int dynamic_array();
int reallocate_array();
int sorted_list();

int main(void)
{
    printf("Hello, World! Data Structures\n");
    int result = dynamic_array();

    // initialize random
    srand(time(NULL));

    if (result != 0)
    {
        return result;
    }

    result = reallocate_array();

    if (result != 0)
    {
        return result;
    }

    result = sorted_list();

    if (result != 0)
    {
        return result;
    }

    return 0;
}

int dynamic_array()
{
    // create an initial list of size 3
    int *list = malloc(3 * sizeof(int));

    // if we can't allocate the memory, return
    if (list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // create another list of size 4
    int *tmp = malloc(4 * sizeof(int));

    if (tmp == NULL)
    {
        // make sure we free list
        free(list);
        return 1;
    }

    // copy list into tmp
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }    

    // add another number to tmp
    tmp[3] = 4;

    // free up the list
    free(list);

    list = tmp;

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);
    return 0;
}

// realloc saves the copy step (it does it for you while allocating new space)
int reallocate_array()
{
    // List of size 3
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Initialize list of size 3 with numbers
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Resize list to be of size 4
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }
    list = tmp;

    // Add number to list
    list[3] = 4;

    // Print list
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Free list
    free(list);
    return 0;    
}

typedef struct node
{
    int number;
    struct node *next;
}
node;

int sorted_list()
{
    // the pointer to list is the first element
    node *list = NULL;

    for (int i = 0; i < 10; i++)
    {
        int num = rand();

        node *n = malloc(sizeof(node));
        if (n == NULL) 
        {
            return 1;
        }

        n->number = num;
        n->next = NULL;

        if (list == NULL)
        {
            // first element in list
            list = n;
        }
        else if (n->number < list->number)
        {
            // new node should be first. the current
            // first node should be the next for the 
            // current node
            n->next = list;

            // set first node to the current one
            list = n;
        }
        else
        {
            // loop through the remaining nodes and find
            // where the current one belongs
            for (node *ptr = list; ptr != NULL; ptr = ptr->next)
            {
                if (ptr->next == NULL)
                {
                    // at the end of the list
                    ptr->next = n;
                    break;
                }
                else
                {
                    if (n->number < ptr->next->number)
                    {
                        n->next = ptr->next;
                        ptr->next = n;
                        break;
                    }
                }
            }
        }
    }

    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }    

    node *ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }

    return 0;
}