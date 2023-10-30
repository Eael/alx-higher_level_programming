#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 if there is no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head1 = list;
	listint_t *head2 = list;

	if (!list)
		return (0);
	while (head1 && head2 && head2->next)
	{
		head1 = head1->next;
		head2 = head2->next->next;

		if (head1 == head2)
			return (1);
	}
	return (0);
}
