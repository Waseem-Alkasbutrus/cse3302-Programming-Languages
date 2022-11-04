// Name         : Waseem Alkasbutrus
// ID           : 1001849127
// Lang Version : gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
// OS           : Ubuntu 20.04.5 LTS (Not on a virtual machine)

// NOTE: Check README.md for answer to questions 1 and 2

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>

#define MAX_PATH_LEN 1000

typedef struct dirent Entry;

long sumFileSizes(char *path)
{
    long size = 0;

    // open directory path
    DIR *dir = opendir(path);
    if (dir == NULL)
    {
        printf("[ERR] Couldn't open %s\n", path);
    }

    // get pointer to first entry in directory
    Entry *entry = readdir(dir);

    do
    {
        // if entry is a directory, and isn't "." nor ".."
        if (entry->d_type == DT_DIR && strcmp(entry->d_name, ".") && strcmp(entry->d_name, ".."))
        {
            // allocate space for curren working directory (as provided in path argument)
            char *cwd = malloc(sizeof(char) * MAX_PATH_LEN);
            strcpy(cwd, path);

            // append a "/" and add the entry directory name
            strcat(cwd, "/");
            strncat(cwd, entry->d_name, MAX_PATH_LEN - strlen(cwd));

            // call this function again for found directory
            size += sumFileSizes(cwd);

            // free previously allocated memory for new path
            free(cwd);
        }
        else if (entry->d_type == DT_REG)
        {
            // if entry is a regular file, add the record length to the size
            size += entry->d_reclen;
        }

        // update entry to point to next entry in directory
        entry = readdir(dir);

    } while (entry != NULL);

    return size;
}

int main(void)
{
    long size = sumFileSizes(".");
    printf("%ld\n", size);

    return 0;
}