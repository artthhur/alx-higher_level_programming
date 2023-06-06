#include "lists.h"
/**
 * check_cylce - if a singly likned list has a cycle in it
 * @list: head
 * Return: 0 if no cycle, 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *b, *a = list;

	if (list == NULL || list->next == NULL)
		return (0);
	b = list->next;
	while (a && b && b->next)
	{
		if (a == b)
			return (1);
		b = b->next->next;
		a = a->next;
	}
	return (0);
}
