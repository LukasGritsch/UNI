/* scanf7.c */
#include <stdio.h>

int main(void) {
   int a, b, check;

   printf("Bitte zwei Zahlen eingeben: ");
   check = scanf("%d %d",&a ,&b);
   getchar();    /* für Linux             */
   /* Ist check gleich 2, war die Eingabe richtig. */
   if(check == 2)
      printf("Beide Zahlen richtig %d und %d\n",a ,b);
   /* ... nicht richtig, also war die 2. Zahl falsch. */
   else if(check == 1) {
         printf("Die 2.Zahl hat das falsche Format!!\n");
         printf("Bitte Eingabe wiederholen: ");
         /* noch ein Versuch */
         check = scanf("%d",&b);
         if(check)
            printf("Eingabe Ok. Ihre Zahlen %d %d\n",a,b);
         else
            printf("Leider nochmals falsch\n");
      }
   else
      printf("Die erste oder beide Eingaben waren falsch!\n" );
   return 0;
}
