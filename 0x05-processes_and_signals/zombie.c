#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - infinite while loop
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Create 5  zombie process
 *
 * Return: 0
 */

int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %d", pid);
		sleep(1);
	}
	infinite_while();

	return (0);
}
