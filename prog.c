#include<stdio.h>
#include<stdlib.h>
void insertbeg();

void traverse();
int option,n;
struct node 
{
    int info;
struct node *link;
};
struct node *start=NULL,*temp,*ptr;
void insertbeg()
{
temp=(struct node*)malloc(sizeof(struct node));
printf("Enter the data:\n");
scanf("%d",&temp->info);
temp->link=NULL;
if(start==NULL)
start=temp;
else
{
temp->link=start;
start=temp;
}
}
void traverse()
{
if(start==NULL)
printf("Linked list is empty\n");
else
{
ptr=start;
while (ptr!=NULL)
{
    printf("%d\t",ptr->info);
ptr=ptr->link;
}
}
}

int main()
{
int middle;
printf("enter the number of node:\n");
scanf("%d",&n);
 for(int i=0;i<n;i++)
insertbeg();
printf("Linked list:");
traverse();

middle=len(traverse())/2;
printf("%d\n",traverse(middle));
}