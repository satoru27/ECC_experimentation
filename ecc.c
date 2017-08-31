#include <stdio.h>
#include <gmp.h>

int main(){
	printf("\tHello GMP \n");
	mpz_t rop;
	mpz_init_set_ui(rop,1); //inicializando rop com o valor de 1

	for(unsigned int i = 1; i < 6918; i++)
		mpz_mul_ui(rop,rop,i);

	mpz_sub_ui(rop,rop,1); //6917! - 1

	gmp_printf ("Calculated number:\n %Zd\n",rop);

	printf("Select the number of reps for Miller-Rabin probabilistic primality tests:\n> ");
	int reps = 1;
	scanf("%d",&reps);
	int result = mpz_probab_prime_p(rop,reps);
	//printf("\t RESULT: %d\n",result);
	
	switch(result){
		case 1: printf("\tProb Prime\n");break;
		case 2: printf("\tDef Prime\n");break;
		default: printf("\tNot Prime\n");break;
	}
	mpz_clear(rop);
	return 0;
}
