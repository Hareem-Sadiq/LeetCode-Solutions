#include <pthread.h>
#include <stdio.h>

// void printNumber(int x){
//     printf("%d",x);
// }

void printNumber(int a);

typedef struct {
    int n;
    pthread_mutex_t lock;
    pthread_cond_t cond;
    int turn;
} ZeroEvenOdd;

ZeroEvenOdd* zeroEvenOddCreate(int n) {
    ZeroEvenOdd* obj = (ZeroEvenOdd*) malloc(sizeof(ZeroEvenOdd));
    obj->n = n;
    pthread_mutex_init(&(obj->lock), NULL);
    pthread_cond_init(&(obj->cond), NULL);
    obj->turn = -1;
    return obj;
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.

void zero(ZeroEvenOdd* obj) {
    for(int i=0; i< obj->n; i++){
        pthread_mutex_lock(&(obj->lock));
        while(obj->turn !=-1)
            pthread_cond_wait(&(obj->cond), &(obj->lock));
        printNumber(0);
        obj->turn = i%2;
        pthread_cond_broadcast(&(obj->cond));
        pthread_mutex_unlock(&(obj->lock));
    }
}

void even(ZeroEvenOdd* obj) {
    for(int i=2; i<=obj->n; i+=2){
        pthread_mutex_lock(&(obj->lock));
        while(obj->turn != 1)
            pthread_cond_wait(&(obj->cond), &(obj->lock));
        printNumber(i);
        obj->turn = -1;
        pthread_cond_broadcast(&(obj->cond));
        pthread_mutex_unlock(&(obj->lock));
    }
}

void odd(ZeroEvenOdd* obj) {
    for(int i=1; i<=obj->n; i+=2){
        pthread_mutex_lock(&(obj->lock));
        while(obj->turn != 0)
            pthread_cond_wait(&(obj->cond), &(obj->lock));
        printNumber(i);
        obj->turn = -1;
        pthread_cond_broadcast(&(obj->cond));
        pthread_mutex_unlock(&(obj->lock));
    }
}

void zeroEvenOddFree(ZeroEvenOdd* obj) {
    pthread_mutex_destroy(&(obj->lock));
    pthread_cond_destroy(&(obj->cond));
    free(obj);
}