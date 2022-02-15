# Merge Sort

## Zadání
Program provede setřídění čísel pomocí metody Merge Sort.

# Popis a rozbor problému
Merge Sort (Obr. 1) je třídící algoritmus vynalezený v roce 1945 Johnem von Neumannem. Samotný postup se skládá ze dvou kroků. V prvním dochází k postupnému rozdělování seznamu čísel na n podseznamů, z nichž každý obsahuje pouze jeden prvek. Přičemž jednotlivé podseznamy jsou rozdělovány na polovinu. V druhém kroku dochází naopak ke slučování dílčích podseznamů až do doby, kdy zůstane pouze jeden seznam. Zde dochází ke srovnávání jednotlivých čísel v podseznamu podle velikosti. Výsledkem je tedy seznam seřazených čísel o stejném rozsahu jako seznam vstupní.

![merge](https://user-images.githubusercontent.com/93740236/153936187-31f1be9d-11d3-4ba7-abfc-782754ed51c6.jpg)

## Popis algoritmu
	funkce merge_sort s parametrem arr

	  když počet znaků parametru arr bude větší než jedna
			ulož levou polovinu znaků parametru arr do proměnné left_arr
			ulož pravou polovinu znaků parametru arr do proměnné right_arr

			začni s rekurzí zavoláním funkce merge_sort se vstupem left_arr
			začni s rekurzí zavoláním funkce merge_sort se vstupem right_arr

			vytvoř proměnnou i s hodnotou nula (jako left_arr index)
			vytvoř proměnnou j s hodnotou nula (jako right_arr index)	
			vytvoř proměnnou k s hodnotou nula (jako merged_arr index)

			dokud hodnota v proměnné i nebude menší než je počet znaků v left_arr a hodnota v proměnné j nebude menší než je počet znaků v right_arr
				tak když hodnota na pozici left_arr určena pomocí proměnné i bude menší než hodnota na pozici right_arr určena pomocí proměnné j
					přiřad do seznamu arr na pozici s hodnotou proměnné k hodnotu left_arr na pozici hodnoty proměnné i
					a k proměnné i přičti 1
				nebo
					přiřad do seznamu arr na pozici s hodnotou proměnné k hodnotu right_arr na pozici hodnoty proměnné j
					a k proměnné j přičti 1
				nakonec k proměnné k přičti 1

			dokud hodnota proměnné i nebude menší než je počet znaků v left_arr 
				přiřad do seznamu arr na pozici s hodnotou proměnné k hodnotu left_arr na pozici hodnoty proměnné i
				a k proměnné i přičti 1
				a k proměnné k přičti 1

			dokud hodnota proměnné j nebude menší než je počet znaků v right_arr 
				přiřad do seznamu arr na pozici s hodnotou proměnné k hodnotu right_arr na pozici hodnoty proměnné j
				a k proměnné i přičti 1
				a k proměnné k přičti 1

	funkce load_data

		založ prázdný seznam

		započni cyklus
			zadej počet elementů do proměnné n, dokud nebude platit podmínka

			když n není numerický znak
				vytiskni: "Not number, try again"
				a pokračuj zpět k zadávání elementů

			převeď proměnnou n na integer

			když bude n menší než 2
				vytiskni: "Try again and enter positive integer larger than 2"
			v opačném případě
				ukonči cyklus

		započni cyklus v rozmezí od 0 do n
			dokud bude platit
				zadej číslo do proměnné ele

				zachyť případnou výjimku
					převeď proměnnou ele na float
					ukonči
				pokud nastane: ValueError
					vytiskni: "Not number, try again"

			připoj zadanou hodnotu do seznamu
		po dokončení cyklu vrať list

	funkce program

		do proměnné list zavolej funkci load_data
		zavolej funkci se vstupem list
		vytiskni list

	pokud se jméno bude rovnat 'main'
		zavolej funkci program	

Rekurze ve funkci merge_sort probíhá nejřívé na levé straně seznamu, tedy left_arr, a to přes uplné rozdělení až na úplné seřazení. Totéž se následně provede i na pravé straně, tedy right_arr. Na závěr je levá i pravá strana seznamu setříděna do jednoho finálního a tím je seřazení ukončeno.

## Problematické situace a jejich rozbor
Hlavní problematickou situací bylo ošetření vstupů před zadáním nesmyslných hodnot. K ošetření zadání počtu prvků byla využita řetězcová metoda isnumeric. Ta vrací True, pokud řetězec obsahuje čísla. Po splnění této podmínky byly vstupní čísla převedena na integer. Tato metoda však není všespásná kvůli tomu, že funkce integer potřebuje pouze jeden konkrétní druh číslic, které se ve všech případech neshodují s isnumeric (Nauč se Python 2014). Pro účely tohoto programu ale považuji toto řešení za dostatečné. K ošetření zadání jednotlivých prvků do seznamu bylo využito zachycení chyby pomocí příkazu try/except. Díky tomu je umožněno zadávat reálná čísla.   

## Vstupní data
Vstupem do programu je seznam libovolného počtu čísel. Podmínkou je, aby počet prvků v seznamu byl větší nebo rovný 2, a to kvůli možnosti porovnávání. A aby všechny prvky v seznamu byly reálná čísla.

## Výstupní data
Program po provedení výpočtu vrátí seznam čísel o stejném rozsahu a se stejnými prvky. Prvky v seznamu ale budou seřazeny od nejmenšího čísla do největšího.

## Závěr
Program je částečně interaktivní, a to díky možnosti výběru prvků uživatelem. Vstupy jsou dostatečně ošetřeny a tím pádem je minimalizována možnost pádu programu z důvodu nevhodných dat. Problém může nastat teoreticky u ošetření metodou isnumeric. 

## Zdroje
Wikipedia (2022): Merge Sort. https://en.wikipedia.org/wiki/Merge_sort (cit. 8. 2. 2022)

Nauč se Python (2014): Výjimky. https://naucse.python.cz/lessons/beginners/exceptions/ (cit. 8. 2. 2022)
