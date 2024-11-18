#include "user.h"

// Global Variables
User users[MAX_USERS];
int num_users = 0;

// Manual String Comparison
int str_compare(const char *s1, const char *s2) {
    while (*s1 && (*s1 == *s2)) {
        s1++;
        s2++;
    }
    return *(unsigned char *)s1 - *(unsigned char *)s2;
}

// Manual String Copy
void str_copy(char *dest, const char *src) {
    while (*src) {
        *dest++ = *src++;
    }
    *dest = '\0';
}

int registerUser(const char *username, const char *password) {
    for (int i = 0; i < num_users; i++) {
        if (str_compare(users[i].username, username) == 0) {
            return 0; // Username already exists
        }
    }

    if (num_users >= MAX_USERS) {
        return -1; // Array full
    }

    str_copy(users[num_users].username, username);
    str_copy(users[num_users].password, password);
    users[num_users].money = 0; // Initial money is 0
    num_users++;
    return 1; // Registration successful
}

int loginUser(const char *username, const char *password) {
    for (int i = 0; i < num_users; i++) {
        if (str_compare(users[i].username, username) == 0 &&
            str_compare(users[i].password, password) == 0) {
            return 1; // Login successful
        }
    }
    return 0; // Login failed
}
