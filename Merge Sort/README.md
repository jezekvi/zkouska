# Merge Sort

## Zadání
Program provede setřídění čísel pomocí metody Merge Sort.

# Popis a rozbor problému
Merge Sort (Obr. 1) je třídící algoritmus vynalezený v roce 1945 Johnem von Neumannem. Samotný postup se skládá ze dvou kroků. V prvním dochází k postupnému rozdělování seznamu čísel na n podseznamů, z nichž každý obsahuje pouze jeden prvek. Přičemž jednotlivé podseznamy jsou rozdělovány na polovinu. V druhém kroku dochází naopak ke slučování dílčích podseznamů až do doby, kdy zůstane pouze jeden seznam. Zde dochází ke srovnávání jednotlivých čísel v podseznamu podle velikosti. Výsledkem je tedy seznam seřazených čísel o stejném rozsahu jako seznam vstupní.

![merge](https://user-images.githubusercontent.com/93740236/153936187-31f1be9d-11d3-4ba7-abfc-782754ed51c6.jpg)

## Popis algoritmu

## Problematické situace a jejich rozbor
Hlavní problematickou situací bylo ošetření vstupů před zadáním nesmyslných hodnot. Je nutné, aby uživatel zadával pouze celá čísla. K tomu byla využita řetězcová metoda isnumeric. Ta vrací True, pokud řetězec obsahuje čísla. Po splnění této podmínky byly vstupní čísla převedena na integer. Tato metoda však není všespásná kvůli tomu, že funkce integer potřebuje pouze jeden konkrétní druh číslic, které se ve všech případech neshodují s isnumeric (Nauč se Python 2014). Pro účely tohoto programu ale považuji toto řešení za dostatečné.

## Vstupní data
Vstupem do programu je seznam libovolného počtu čísel. Podmínkou je, aby počet prvků v seznamu byl větší nebo rovný 2, a to kvůli možnosti porovnávání. A aby všechny prvky v seznamu byly celá čísla.

## Výstupní data
Program po provedení výpočtu vrátí seznam čísel o stejném rozsahu a se stejnými prvky. Prvky v seznamu ale budou seřazeny od nejmenšího čísla do největšího.

## Závěr
Program je částečně interaktivní, a to díky možnosti výběru prvků uživatelem. Vstupy jsou dostatečně ošetřeny a tím pádem je minimalizována možnost pádu programu z důvodu nevhodných dat. Problém může nastat teoreticky u ošetření metodou isnumeric. 

## Zdroje
Wikipedia (2022): Merge Sort. https://en.wikipedia.org/wiki/Merge_sort (cit. 8. 2. 2022)
Nauč se Python (2014): Výjimky. https://naucse.python.cz/lessons/beginners/exceptions/ (cit. 8. 2. 2022)
