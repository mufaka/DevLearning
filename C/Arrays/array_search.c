#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct 
{
    char* name; // string; don't want to define size here
    int age;
}
Person;

// compare for Person name
int comparePersonName(const void *s1, const void *s2) 
{
    /*
        IMPORTANT!!!!

        The array being sorted is an array of
        pointers so we have pointers to pointers
        and need to use ** here to get the pointer
        to Person.

        https://stackoverflow.com/questions/3903849/issue-with-qsort-the-sorting-is-not-properly-done-c
    */
    Person * person1 = *(Person **)s1;
    Person * person2 = *(Person **)s2;

    return strcmp(person1->name, person2->name);
}

// compare for Person age
int comparePersonAge(const void *s1, const void *s2) {
    Person * person1 = *(Person **)s1;
    Person * person2 = *(Person **)s2;

    return person1->age - person2->age;
}

// function prototypes
Person* createPerson(char* name, int age);
Person* linearFind(int peopleLength, Person* people[], char* name);
Person * binaryFind(Person * people[], char * name, int low, int high);

int main(void)
{
    Person * one = createPerson("Bill", 51);
    Person * two = createPerson("Michelle", 47);
    Person * three = createPerson("Tanner", 15);
    Person * four = createPerson("Blaise", 11);

    // array is of pointers to Person structs
    Person * people[] = { one, two, three, four };

    // sort people by name
    // My first segmentation fault :) Keeping here for nostalgia.
    // qsort(people, 4, sizeof(Person), comparePersonName);
    qsort(people, 4, sizeof(one), comparePersonName);

    // are the People sorted?
    for (int i = 0; i < 4; i++) 
    {
        printf("Person %i: %s\n", i + 1, people[i]->name);
    }

    Person * tanner = linearFind(5, people, "Tanner");

    if (tanner) 
    {
        printf("Found Tanner with linear search. They are %i years old.\n", tanner->age);
    }
    else 
    {
        printf("Could not find Tanner with linear search.\n");
    }

    Person * michelle = binaryFind(people, "Michelle", 0, 3);

    if (michelle) 
    {
        printf("Found Michelle with binary search. They are %i years old.\n", michelle->age);
    }
    else 
    {
        printf("Could not find Michelle with binary search.\n");
    }

}

Person * createPerson(char * name, int age) 
{
    // allocate memory for the struct
    Person * person = malloc(sizeof(Person));

    // allocate memory for the string
    person->name = malloc(sizeof(char) * 4); // need 8 for unicode?
    strcpy(person->name, name); // -> instead of . because pointer
    person->age = age;

    return person;
}

// The Person[] people is a pointer to an array that 
// has decayed to being just a pointer to the first
// element in the array. For that reason, size/length
// cannot be determined here. Length needs to be passed
// into the function.
Person * linearFind(int peopleLength, Person * people[], char * name) 
{
    for (int i = 0; i < peopleLength; i++) 
    {
        // this won't work either, pointers won't
        // be the same value...need strcmp ...
        //if (people[i]->name == name) 
        if (strcmp(people[i]->name, name) == 0)
        {
            return people[i];
        }
    }

    // is returning a null pointer bad?
    return NULL;
}

Person * binaryFind(Person * people[], char * name, int low, int high) 
{
    if (high >= low)
    {
        // get the mid point of array. what about even length arrays?
        int mid = low + (high - low) / 2;
        printf("Mid point is %i\n", mid);

        int checkMid = strcmp(people[mid]->name, name);
        printf("Mid compare for %s is %i\n", people[mid]->name, checkMid);

        // if name at mid matches search, return it
        if (checkMid == 0)
        {
            return people[mid];
        }

        // search left
        if (checkMid > 0)
        {
            return binaryFind(people, name, low, mid - 1);
        }

        // search right
        if (checkMid < 0)
        {
            return binaryFind(people, name, mid + 1, high);
        }
    }

    return NULL;
}