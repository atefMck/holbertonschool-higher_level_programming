#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - insert new node in list
* @head: head of list
* @number: the number to add
* Return: pointer to node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *newNode;
listint_t *curr;
if (!head)
return (NULL);
if (!*head)
{
newNode = add_nodeint_end(head, number);
return (newNode);
}
curr = *head;
newNode = malloc(sizeof(listint_t));
if (!newNode)
return (NULL);
newNode->n = number;
if (curr->n > number) {
newNode->next = *head;
*head = newNode;
return(newNode);
}
while (curr->next && newNode->n > curr->next->n )
curr = curr->next;
newNode->next = curr->next;
curr->next = newNode;
return (newNode);
}
