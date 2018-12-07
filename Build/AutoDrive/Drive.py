import numpy as np
import cv2
import move
import time
import picamera
import multiprocessing
import datetime as dt

camera = picamera.PiCamera()
start_time=time.clock()

"""
To be written :

- Loop
-- Sends the captured image to the model for prediction
-- Recieves the direction of movement and acts on it
-- Drive is logged.

--Tertiary control is added : Haar cascade classifiers for object detection and
ultrasonic sensor based driving interrupts
"""

def CaptureImage():
    camera.capture("%s" %time.clock() + "jpg", resize=(150,150))
    sleep(0.2)
    print "Image captured on this process."

def Predict():
    result = loaded_model.predict_classes(image)
    if result='FF':
        forward(5)
    elif result="FL"
        left(5)
    elif result='FR'
        right(5)

def Move()

void deleteNode()
{
    int position, count = 0, i;
    newnode temp, prevnode;

    printf("\nPleas enter the position of the node that needs to be deleted ");
    scanf("%d", &position);

#include <stdio.h>
#include <stdlib.h>
typedef struct node //Structure to define the node
{
    char *val;
    struct node *next;
    struct node *prev;
} n;
typedef struct node *newnode;
newnode new;
newnode ptr;
newnode prev;
newnode first = NULL, last = NULL;
void insertAtBeginning();
void insertAtEnd();
void insertbefore();
void insertAfter();
void deleteNode();
void search();
void display();
void add_node();
int number_of_nodes = 0;

// Dynamic memory allocation operation :
newnode createnewnode(char *data)
{
    number_of_nodes++;
    new = malloc(sizeof(n));
    new->val = data;
    new->next = NULL;
    new->prev = NULL;
    return new;
}

void insertbefore()
{
    char *data = malloc(sizeof(char));
    int position, length = 0;
    int i;
    newnode prevnode;

    printf("\nPlease enter the value that you would like to be inserted.");
    scanf("%s", data);
    printf("\nPlease enter the position to which the string is to be inserted");
    scanf("%d", &position);
    new = createnewnode(data);

    if (first == last && first == NULL)
    {
        if (position == 1)
        {
            first = last = new;
            first->next = last->next = NULL;
            first->prev = last->prev = NULL;
        }
        else
            printf("\nCan't be done because the linked list is empty.");
    }
    else
    {
        if (number_of_nodes < position)
            printf("\nExceeding length therefore the operation can't be executed ");

        else
        {
            for (ptr = first, i = 1; i <= number_of_nodes; i++)
            {
                prevnode = ptr;
                ptr = ptr->next;
                if (i == position-1)
                {
                    prevnode->next = new;
                    new->prev = prevnode;
                    new->next = ptr;
                    ptr->prev = new;
                    printf("\nThe string has been inserted into the %dth position succesfully", position);
                    break;
                }
            }
        }
    }
}
/*
*INSERTS THE ELEMENT AT GIVEN POSITION AFTER THE SPECIFIED LOCATION
*/
void insertAfter()
{
    char *data = malloc(sizeof(char));
    int position, length = 0, i;
    newnode prevnode;

    printf("\nPlease enter the string:");
    scanf("%s", data);
    printf("\nPlease enter the position after which you want the string to be pushed ");
    scanf("%d", &position);
    position++;
    new = createnewnode(data);

    if (first == last && first == NULL)
    {
        if (position < 1)
        {
            first = last = new;
            first->next = last->next = NULL;
            first->prev = last->prev = NULL;
        }
        else
            printf("\nCan't be done because the linked list is empty.");
    }
    else
    {
        if (number_of_nodes < position)
            printf("\nExceeding length therefore the operation can't be executed");

        else
        {
            for (ptr = first, i = 1; i <= number_of_nodes; i++)
            {
                prevnode = ptr;
                ptr = ptr->next;
                if (i == position-1)
                {
                    prevnode->next = new;
                    new->prev = prevnode;
                    new->next = ptr;
                    ptr->prev = new;
                    printf("\nThe string has been inserted into the %dth position succesfully", position);
                    break;
                }
            }
        }
    }
}

//Adding the node in the very beginning :
void insertAtBeginning()
{
    char *data = malloc(sizeof(char));
    printf("\nPlease enter the string: ");
    scanf("%s", data);
    new = createnewnode(data);
    if (first == last && first == NULL)
    {
        printf("\nThe list was empty and the string was added to the first psosition ");
        first = last = new;
        first->next = last->next = NULL;
        first->prev = last->prev = NULL;
    }
    else
    {
        new->next = first;
        first->prev = new;
        first = new;
        first->prev = last;
        last->next = first;
        printf("\n The value has been inserted :");
    }
}


void add_node()
{

    char *data = malloc(sizeof(char));
    printf("\nEnter the string : :");
    scanf("%s", data);
    new = createnewnode(data);

    if (first == last && first == NULL)
    {

        first = last = new; //Defining all nodes as equal.
        first->next = last->next = NULL;
        first->prev = last->prev = NULL;
    }
    else
    {
        last->next = new;
        new->prev = last;
        last = new;
        last->next = first;
        first->prev = last;
    }
}

//Simple search procedure
void search()
{
    int count = 0;
    char *key = malloc(sizeof(char));
    int i, f = 0;

    printf("\n Please enter the string that needs to be searched ");
    scanf("%s", key);;

    if (first == last && first == NULL)
        printf("\nList has empty no elemnets in list to search");
    else
    {
        for (ptr = first,i = 0; i < number_of_nodes; i++,ptr = ptr->next)
        {
            count++;
            printf("%sVALUES = \n", ptr->val);
            if (strcmp(ptr->val,key) == 0)
            {
                printf("\n the string is found at position at %d", count);
                f = 1;
            }
        }
        if (f == 0)
            printf("\n %s the string is not found in linked list", key);
    }
}

//Simple display function.
void display()
{
    int i;
    if (first == last && first == NULL)
        printf("\nThe linked list is empty");
    else
    {
        printf("\nThere are %d nodes", number_of_nodes);
        for (ptr = first, i = 0; i < number_of_nodes; i++,ptr = ptr->next)
            printf("\n %s", ptr->val);
    }
}

//I am now inserting elements to the end with this function.
void insertAtEnd()
{

    char *data = malloc(sizeof(char));

    printf("\n Please enter the string that has to be inserted at the end :");
    scanf("%s", data);
    new = createnewnode(data);

    if (first == last && first == NULL)
    {
        printf("\n Rhe list was empty and the string was added");
        first = last = new;
        first->next = last->next = NULL;
        first->prev = last->prev = NULL;
    }
    else
    {
        last->next = new;
        new->prev = last;
        last = new;
        first->prev = last;
        last->next = first;
    }
}

// I am now deleting a node
void deleteNode()
{
    int position, count = 0, i;
    newnode temp, prevnode;

    printf("\nPleas enter the position of the node that needs to be deleted ");
    scanf("%d", &position);

    if (first == last && first == NULL)
        printf("\nEmpty linked list therefore not executable.");

    else
    {
        if (number_of_nodes < position)
            printf("\nNumber exceeds the length of the linked list. ");

        else
        {
            for (ptr = first,i = 1; i <= number_of_nodes; i++)
            {
                prevnode = ptr;
                ptr = ptr->next;
                if (position == 1)
                {
                    number_of_nodes--;
                    last->next = prevnode->next;
                    ptr->prev = prevnode->prev;
                    first = ptr;
                    printf("%s has been delete", prevnode->val);
                    free(prevnode);
                    break;
                }
                else if (i == position - 1)
                {
                    number_of_nodes--;
                    prevnode->next = ptr->next;
                    ptr->next->prev = prevnode;
                    printf("%s has been deleted.", ptr->val);
                    free(ptr);
                    break;
                }
            }
        }
    }
}

//Driver main function for the entire Program
void main()
{
    int ch;
    printf("\t\t0. Main Menu \n\t\t1. Insert at Beginning \n\t\t2. Insert at End\n\t\t3. Insert Before\n\t\t4. Insert After\n\t\t5. Delete Node at Position\n\t\t6. Search Element \n\t\t7. Display List\n\t\t8. Add to List\n\t\t9. Exit\n");
    while (1)
    {
        printf("\n\nEnter your selection:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 0 :
            main();
            break;
        case 1 :
            insertAtBeginning();
            break;
        case 2 :
            insertAtEnd();
            break;
        case 3 :
            insertbefore();
            break;
        case 4 :
            insertAfter();
            break;
        case 5 :
            deleteNode();
            break;
        case 6 :
            search();
            break;
        case 7 :
            display();
            break;
        case 9 :
            exit(0);
        case 8 :
            add_node();
            break;
        default:
            printf("\nYou have selected an invalid option.");
        }
    }
}
