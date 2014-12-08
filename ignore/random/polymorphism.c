
#include <stdio.h>

int sum(int i, int k){
	printf("int sum\n");
	printf("%d\n", i);
	printf("%d\n", k);
	return 0;
}


int sum(float i, float k){
	printf("Float sum\n");
	printf("%f\n", i );
	printf("%f\n", k);
	return 0;
}


int main(){

	float i = 1.1;
	float k = 2.2;
	sum(i, k);

	return 0;
}


