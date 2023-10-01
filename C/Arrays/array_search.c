#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct 
{
    char* name; // string; don't want to define size here
    int age;
}
Person;

// function prototypes
Person* createPerson(char* name, int age);
Person* linearFind(int peopleLength, Person* people[], char* name);

int main(void)
{
    Person * one = createPerson("Bill", 51);
    Person * two = createPerson("Michelle", 47);
    Person * three = createPerson("Tanner", 15);
    Person * four = createPerson("Blaise", 11);

    // array is of pointers to Person structs
    Person * people[] = { one, two, three, four };
    Person * tanner = linearFind(4, people, "Tanner");

    if (tanner) 
    {
        printf("Found Tanner. He is %i years old.\n", tanner->age);
    }
    else 
    {
        printf("Could not find Tanner.");
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