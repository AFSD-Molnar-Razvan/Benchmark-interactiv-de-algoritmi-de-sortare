# 📊 Benchmark Interactiv de Algoritmi de Sortare (Python / Pygame)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/Pygame-2.5-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-În_Dezvoltare-blue?style=for-the-badge)

## 📖 Despre Proiect

Acest proiect este o aplicație interactivă creată cu Python și Pygame pentru a testa, analiza și vizualiza performanța diferiților algoritmi de sortare. Scopul nostru este de a oferi un benchmark clar între algoritmii elementari ($O(n^2)$) și cei eficienți ($O(n \log n)$), evidențiind modul în care aceștia interacționează cu memoria prin operațiuni de interschimbare și comparare.

Aplicația se distinge prin faptul că permite vizualizarea animației de sortare pas cu pas, folosind conceptul de *generatori* (`yield`) din Python pentru a păstra interfața grafică responsivă în timpul calculelor.

**Aplicația măsoară și analizează:**
* ⏱️ **Timpul de execuție:** Măsurat precis la finalizarea sortării.
* 🔄 **Operațiunile interne:** Numărul total de comparații și interschimbări (swaps), actualizate live pe ecran.
* 📈 **Comportamentul pe seturi diverse de date:** Liste generate aleator, liste deja sortate, liste sortate invers.

---

## 👨‍💻 Echipa Proiectului

* **Molnar Răzvan** & **Roman Denis**
* **Specializare:** Informatică, Anul II

---

## 🚀 Jurnal de Activitate și Arhitectură Tehnică

✅ **Săptămâna 1-2: Setup și Arhitectura de Bază (Pygame Loop)**
* Am configurat fereastra principală Pygame (setare rezoluție, FPS, culori de bază).
* Am implementat bucla principală de evenimente (`main event loop`) pentru a gestiona închiderea aplicației și input-ul de la tastatură.
* Am creat clasa `DrawInformation` care gestionează padding-ul, lățimea și înălțimea barelor în funcție de dimensiunea ferestrei și a listei.
* Am scris funcția de generare a listei de numere aleatoare folosind modulul `random`.

✅ **Săptămâna 3-4: Vizualizarea și Primii Algoritmi (Generators)**
* Am implementat funcția de desenare a listei pe ecran (`draw_list`), unde fiecare număr devine un dreptunghi de o anumită înălțime.
* Am implementat **Bubble Sort** și **Selection Sort**.
* **Imbunătățire Tehnică:** Am transformat algoritmii de sortare în generatori (folosind `yield`). Astfel, după fiecare mutare, algoritmul cedează controlul înapoi către Pygame pentru a desena noul cadru, evitând blocarea ecranului.
* Am adăugat evidențierea vizuală: barele care sunt comparate la un moment dat devin roșii/verzi temporar.

⬜ **Săptămâna 5-6: UI On-Screen și Sistemul de Metrici**
* Vom adăuga text renderizat pe ecran (`pygame.font`) pentru a afișa controalele: *Apasă SPACE pentru Start, R pentru Reset, A pentru Ascendent*.
* Vom implementa contoarele interne. Algoritmii (generatorii) vor returna un dicționar sau un tuplu la fiecare pas, conținând starea listei + numărul curent de `comparisons` și `swaps`.
* Vom afișa aceste contoare live în partea de sus a ecranului.

⬜ **Săptămâna 7-8: Algoritmi Avansați și Cazuri de Testare**
* Vom implementa **Insertion Sort** și algoritmul recursiv **Quick Sort**. Pentru Quick Sort, adaptarea la formatul de generator (`yield from`) va fi o provocare tehnică pe care o vom rezolva.
* Vom adăuga controale pentru generarea specifică a cazurilor de test: Liste Sortate Invers (Worst Case pentru Quick Sort clasic) și Liste Aproape Sortate (Best Case pentru Insertion Sort).

⬜ **Săptămâna 9-10: Refactorizare (OOP) și Modul Benchmark Final**
* Vom curăța codul structurându-l în clase clare (Ex: `AlgorithmManager`, `UIManager`).
* Vom implementa un "Summary Screen" (Ecran de Rezultate) care apare la finalul sortării cu statistici detaliate.
* Vom optimiza logica de desenare (ștergerea doar a porțiunilor modificate din ecran în loc de tot fundalul, pentru performanță sporită la liste mari).
* Finalizarea documentației și adăugarea de comentarii pe funcțiile complexe.
