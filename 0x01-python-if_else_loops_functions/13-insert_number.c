#include "lists.h"

/**
* insert_node - function that inserts a number
* into a sorted singly linked list.
* @head: pointer the head of the linked list
* @number: number to insert
* Return: the address of the new node, or
* NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	
	while (current->next && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
