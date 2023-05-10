#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - insert into sorted linked list
 * @head: head of list
 * @number: data to insert
 *
 * Return: pointer to linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *ptr;

	ptr = malloc(sizeof(listint_t));
	if (!ptr)
		return (NULL);
	ptr->n = number;
	ptr->next = NULL;
	if (*head == NULL || (*head)->n > number)
	{
		ptr->next = *head;
		*head = ptr;

	}
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < number)
			temp = temp->next;
		ptr->next = temp->next;
		temp->next = ptr;
	}

	return (*head);
}
