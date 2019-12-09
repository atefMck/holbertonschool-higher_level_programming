#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - check for cycle
* @list: the list
* Return: has cycle or not
*/
int check_cycle(listint_t *list)
{
listint_t *fastp = list;
listint_t *slowp = list;
if (list == NULL || list->next == NULL)
return (0);
while (fastp && fastp->next && fastp->next->next)
{
slowp = slowp->next;
fastp = fastp->next->next;
if (slowp->n == fastp->n)
return (1);
}
return (0);
}
