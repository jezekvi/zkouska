# Program pro generování hesel generující všechny kombinace k−písmenných slov

## Zadání
Program po výběru k−písmenného slova vygeneruje všechny jeho kombinace.

## Popis a rozbor problému
Základem pro vyřešení zadání je aplikace permutací. Permutace je speciálním případem variace, kdy máme množinu o velikosti n a chceme zjistit počet všech různých n-tic. Pokud máme množinu M o velikosti n, pak permutace je libovolná n-tice složená z prvků z množiny M, přičemž žádný prvek se nesmí opakovat. Příkladem může být množina M = {a, b, c, d}, pak permutace je například [a, b, d, c] nebo [d, b, a, c]. Počet všech různých permutací je roven: P(n) = V(n, n) = n! (MatWeb 2021).

## Popis algoritmu
### Algoritmus permutation
        Vstup: string k permutaci S, aktuální permutace P 
        Když počet znaků S = 0
            permutace P pro výstup

        Dokud neprojdeme všechny ch z S
            x = levá strana od ch
            y = pravá strana od ch	
            permutation(x+y, P + ch)
        Výstup: všechny permutace původního stringu

## Problematické situace a jejich rozbor
Problém může nastat, pokud by uživatel chtěl vypsat slovo, které obsahuje i jiná písmena, než jsou obsaženy v anglické abecedě. Ošetření vstupu pomocí regulárního výrazu porovnává pouze velká a malá písmena anglické abecedy. Zbylé znaky nejsou respektovány. V případě potřeby by ale algoritmus mohl být upraven pomocí doplnění znaků, které by program považoval za správné.

## Vstupní data
Vstupem do programu je string, který obsahuje uživatelem zvolené slovo. Slovo může obsahovat pouze malá a velká písmena anglické abecedy. Nesmí obsahovat číslice, mezery ani jiné znaky.

## Výstupní data
Program vypíše do terminálu veškeré kombinace vybraného slova podle pravidel permutace.

## Závěr
Program je částečně interaktivní, a to díky možnosti výběru slova uživatelem. Program by mohl fungovat s libovolnými hodnotami, ale pro splnění zadání byl vstup ošetřen tak, aby mohl obsahovat pouze písmena anglické abecedy.

## Zdroje
MatWeb (2021): Permutace. https://www.matweb.cz/permutace/ (cit. 8. 2. 2022)
