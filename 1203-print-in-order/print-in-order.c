#include <pthread.h>
typedef struct {
    // User defined data may be declared here.
    pthread_mutex_t lock;
    pthread_cond_t cond;
    int counter;
} Foo;

// Function Declaration, do not remove
void printFirst();
void printSecond();
void printThird();

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    
    // Initialize user defined data here.
    pthread_mutex_init(&(obj->lock), NULL);
    pthread_cond_init(&(obj->cond), NULL);

    obj->counter = 0;
    return obj;
}

void first(Foo* obj) {
    
    // printFirst() outputs "first". Do not change or remove this line.
    pthread_mutex_lock(&(obj->lock));
    printFirst();
    obj->counter +=1;
    pthread_cond_broadcast(&(obj->cond));
    pthread_mutex_unlock(&(obj->lock));
    
}

void second(Foo* obj) {
    
    // printSecond() outputs "second". Do not change or remove this line.
    pthread_mutex_lock(&(obj->lock));
    while(obj->counter != 1)
        pthread_cond_wait(&(obj->cond), &(obj->lock));

    printSecond();
    obj->counter +=1;
    pthread_cond_broadcast(&(obj->cond));
    pthread_mutex_unlock(&(obj->lock));
}

void third(Foo* obj) {
    
    // printThird() outputs "third". Do not change or remove this line.
    pthread_mutex_lock(&(obj->lock));
    while(obj->counter != 2)
        pthread_cond_wait(&(obj->cond), &(obj->lock));
    
    printThird();
    obj->counter+=1;
    pthread_cond_broadcast(&(obj->cond));
    pthread_mutex_unlock(&(obj->lock));

}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    pthread_mutex_destroy(&(obj->lock));
    pthread_cond_destroy(&(obj->cond));
    free(obj);
}