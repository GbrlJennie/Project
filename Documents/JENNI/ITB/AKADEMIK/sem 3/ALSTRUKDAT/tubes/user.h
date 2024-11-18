#ifndef ADT_USER_H
#define ADT_USER_H

#define MAX_USERS 100
#define MAX_LEN 256

typedef struct {
    char username[MAX_LEN];
    char password[MAX_LEN];
    int money;
} User;

// Global Variables
extern User users[MAX_USERS];
extern int num_users;

// Function Prototypes
int registerUser(const char *username, const char *password);
int loginUser(const char *username, const char *password);

#endif
