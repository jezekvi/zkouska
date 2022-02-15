# Program pro generování hesel generující všechny kombinace k−písmenných slov

## Zadání
Program po výběru k−písmenného slova vygeneruje všechny jeho kombinace.

## Popis a rozbor problému
Základem pro vyřešení zadání je aplikace permutací. Permutace je speciálním případem variace, kdy máme množinu o velikosti n a chceme zjistit počet všech různých n-tic. Pokud máme množinu M o velikosti n, pak permutace je libovolná n-tice složená z prvků z množiny M, přičemž žádný prvek se nesmí opakovat. Příkladem může být množina M = {a, b, c, d}, pak permutace je například [a, b, d, c] nebo [d, b, a, c]. Počet všech různých permutací je roven: P(n) = V(n, n) = n! (MatWeb 2021).

## Popis algoritmu
  funkce permutation s parametry str a tmp (tmp je prázdný)
    když bude počet znaků v parametru str rovný 0
      vytiskni hodnoty z parametru tmp

    započni cyklus v rozmezí počtu znaků v parametru str (všechna písmena v zadaném slově)
      do proměnné ch ulož písmeno ze dananého slova na pozici hodnoty i
      do proměnné left_part ulož všechna písmena nalevo od písmena v proměnné ch
      do proměnné right_part ulož všechna písmena napravo od písmena v proměnné ch
      zavolej funkci permutation a do parametru str vlož spojení left_part a right part a do parametru tmp vlož spojení tmp a ch)

  funkce load_data
    započni cyklu
      zadej word dokud nebude platit podmínka

      když nebude word validováno (nebude obsahovat pouze malá a velká písmena EN abecedy)
        vytiskni: "Not a word, try again"
        a pokračuj zpět k zadávání slova
      po splnění ukonči
    a vrať slovo 


  funkce program
    do proměnné word zavolej funkci load_data
    zavolej funkci permutation se vstupem word

  pokud se jméno bude rovnat 'main'
    zavolej funkci program
  
Funkce funguje na principu rekurze. Rekurze se zanořuje až do té doby, kdy parametr str neobsahuje žádné hodnoty. V tu chvíli program vypíše hodnoty v tmp, která v tu chvíli obsahuje všechna písmena ze zvoleného slova. Rekurze postupně projde všechny kombinace až do chvíle, kdy se naplní for cyklus (všechna písmena ve slově byla použita jako písmeno počáteční).

## Problematické situace a jejich rozbor
Problém může nastat, pokud by uživatel chtěl vypsat slovo, které obsahuje i jiná písmena, než jsou obsaženy v anglické abecedě. Ošetření vstupu pomocí regulárního výrazu porovnává pouze velká a malá písmena anglické abecedy. Zbylé znaky nejsou respektovány. V případě potřeby by ale algoritmus mohl být upraven pomocí doplnění znaků, které by program považoval za správné.

## Vstupní data
Vstupem do programu je string, který obsahuje uživatelem zvolené slovo. Slovo může obsahovat pouze malá a velká písmena anglické abecedy. Nesmí obsahovat číslice, mezery ani jiné znaky.

## Výstupní data
Program vypíše do terminálu veškeré kombinace vybraného slova podle pravidel permutace.

## Závěr
Program je částečně interaktivní, a to díky možnosti výběru slova uživatelem. Program by mohl fungovat s libovolnými hodnotami, ale pro splnění zadání byl vstup ošetřen tak, aby mohl obsahovat pouze písmena anglické abecedy.

# Zdroje
MatWeb (2021): Permutace. https://www.matweb.cz/permutace/ (cit. 8. 2. 2022)
