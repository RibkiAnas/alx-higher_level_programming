#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head of list
 * Return: pointer to new head of list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
* check_cycle - function that checks if a
* singly linked list has a cycle in it.
* @list: pointer to head of list.
* Return: 0 if there is no cycle, 1 if there
* is a cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *rev_head;

	if (!list)
		return (0);

	rev_head = reverse_list(list);
	reverse_list(rev_head);

	if (rev_head == list)
		return (1);
	else
		return (0);
}
