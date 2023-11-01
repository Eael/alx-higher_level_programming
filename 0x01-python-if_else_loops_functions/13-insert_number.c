#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts an integer into a sorted singly linked list
 * @head: pointer to pointer to head of linked list
 * @number: number to insert in linked list
 *
 * Return: address of new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number);
