#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *next = NULL;
listint_t *second_half;
listint_t *temp1, *temp2;
int is_pal = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

/* Find middle of the list using slow and fast pointers */
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
slow = slow->next;
}

/* Reverse the second half of the list */
second_half = slow;
while (second_half != NULL)
{
next = second_half->next;
second_half->next = prev;
prev = second_half;
second_half = next;
}
second_half = prev;

/* Compare first half with reversed second half */
temp1 = *head;
temp2 = second_half;
while (temp2 != NULL)
{
if (temp1->n != temp2->n)
{
is_pal = 0;
break;
}
temp1 = temp1->next;
temp2 = temp2->next;
}

/* Restore the list to its original order (optional) */
prev = NULL;
while (second_half != NULL)
{
next = second_half->next;
second_half->next = prev;
prev = second_half;
second_half = next;
}

return (is_pal);
}
