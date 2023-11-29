# Firma-Kamila
Projekt szkolny dotyczacy aplikacji dla firmy Kamila :D


Specyfikacja Algorytmu

Dane wejsciowe:

	monthly_sales_value_seller, value_payment, percentage_of_bonus - pobrane liczby całkowite od użytkownika
Wyniki: 

	seller_remuneration - liczba całkowita, reprezentująca wynagrodzenie sprzedawcy, po odliczeniu wszystkich 				rzeczy.
Zmienne pomocnicze:

	bonus_value - zmienna wysokosci premi zależna od wartości sprzedazy w biezacym miesiacu
			10% dla bonus_value < 10000
			12% dla bonus_value < 10000 - 14999.99
			14% dla bonus_value < 15000 - 17999.99
			16% dla bonus_value < 18000 - 21999.99
			18% dla bonus_value < 22000 lub wiecej 




Pseudokod
// getMonthly_sales_value_seller()

	pobieranie monthly_sales_value_seller;
	zwracanie monthly_sales_value_seller;
	
// getValue_payment()

	pobieranie value_payment;
	zwracanie value_payment;

// getValue_percentage()

	percentage_of_bonus = 0;
	pobieranie monthly_sales_value_seller  = getMonthly_sales_value_seller();
 
	jesli(monthly_sales_value_seller < 10000){
		percentage_of_bonus = 0.10;
	}
	jesli(monthly_sales_value_seller > 10000 && monthly_sales_value_seller < 14999.99){
		percentage_of_bonus = 0.12;
	}
	jesli(monthly_sales_value_seller > 10000 && monthly_sales_value_seller < 17999.99){
		percentage_of_bonus = 0.14;
	}
	jesli(monthly_sales_value_seller > 10000 && monthly_sales_value_seller < 21999.99){
		percentage_of_bonus = 0.16;
	}
	jesli(monthly_sales_value_seller > 22000){
		percentage_of_bonus = 0.18;
	}
	zwracanie percentage_of_bonus;
 
// Pobierz miesięczną wartość sprzedaży dla danego sprzedawcy: 

	 Ustawianie monthly_sales_value_seller = getMonthly_sales_value_seller(); 
  
//  Pobierz wartość pobranej zaliczki. 

	Ustawianie value_payment = getValue_payment();
 
// Na podstawie wartości sprzedaży pobierz procentową wysokość premii. 

	Ustawianie  percentage_of_bonus = getValue_percentage();
 
// Za pomocą przedstawionego wzoru oblicz wynagrodzenie sprzedawcy.

	Ustawianie seller_remuneration = 0;
	seller_remuneration = monthly_sales_value_seller * bonus_value - value_payment;



 
Pseudokod wszystkich funkcji przedstaw w postaci schematu blokowego

1.	getMonthly_sales_value_seller()



![image](https://github.com/Bigguizzo/Firma-Kamila/assets/87502153/4cb421e3-0efe-46cb-a347-fd1a3d1fd703)

2.	getValue_payment()




 ![image](https://github.com/Bigguizzo/Firma-Kamila/assets/87502153/76ee61a4-a777-465c-a82a-e40c249c3344)

3.	getValue_percentage()




 ![image](https://github.com/Bigguizzo/Firma-Kamila/assets/87502153/5b93aa40-e692-4eb4-a7c7-d9b08937121b)

4.	Main Program




![image](https://github.com/Bigguizzo/Firma-Kamila/assets/87502153/df9801ec-28d3-4ba3-ad13-41e79cb20ef8)
 


