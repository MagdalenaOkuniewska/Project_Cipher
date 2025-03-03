# Projekt
# CIPHER

1. ROT13, ROT47 (SZYFR CEZARA) -> [https://pl.wikipedia.org/wiki/Szyfr_Cezara](https://pl.wikipedia.org/wiki/Szyfr_Cezara)
   a -> n itd. 

4. Funkcjonalności
    - FileHandler odczyt, zapis do pliku, user podaje nazwe tego pliku, obsługa wyjątków, Gdy chce zapisać do tego samego pliku to append(dodanie do pliku), - Ja polecam rozszerzenie / format JSON
    - Szyfrowanie i Odszyfrowywanie.
    - Buffer / Memory Buffer  czyli taka lista, która sobie istnieje podczas działania programu, Trzyma zaszyfrowane, odszyfrowane wczytane z pliku, z niego zapisujemy do pliku. 
    - Menu
    - Uruchamianie wybranych funkcji w managerze mozna rozwiązac za pomocą Dict'a lub structural pattern matching [https://peps.python.org/pep-0636/]  (Na pewno nie przy użyciu if / elif itd...)
    - Manager
    - run/main.py # zeby dalo sie uruchomic plik za pomoca python run.py / python main.py 
        if __name__ == '__main__': ... 
    - Exit
    - Wzorzec projektowy: Facade
    - Testy Jednostkowe (Na końcu) 
3. Funkcjonalności (Ogólne) (Na końcu) 
    - README do projektu. 

   
### struktura obiekt
- Obiekt Text zaszyfrowany/odszyfrowany to dataclasss.  Ten, który byłby umieszczany w bufferze. 
- {"text"": xyz, "rot_type": rot13/rot47, "status": encrypted/decrypted}

1. Dodatkowe rzeczy:
    - FactoryMethod/AbstractFactory

2. Stylistyka
    - PEP 8
    - GithubFlow
    - Czeste commity 
    - Conventional commits
      - NOK -> add new way of handling files
      - OK -> feat: add new way of handling files
      - BEST OK -> feat(filehandler): add new way of handling files
      - NOK -> update .gitignore
      - OK -> chore: update .gitignore
      - BEST OK -> chore(git): update .gitignore
      - NOK -> create unit tests for file handling
      - OK -> test: create unit tests for file handling 
      - BEST OK -> test(filehandler): create unit tests for file handling
      - NOK -> update readme.md about file_handling feature
      - OK -> docs: update readme.md about file_handling feature
      - BEST -> docs(readme): update readme.md about file_handling feature
      example: git commit -m "feat: xyz"
      TYPES: 
        - feat - nowa funkcjonalność
        - fix - naprawa błędu 
        - build - commit dot. budowania projektu np. skryptów itd. 
        - chore - zmiana nie dotyczaca kodu aplikacji np. zmiana w gitignore, zmiana w configu czegos itd. 
        - ci - zmiana dot continues integration 
        - docs - zmiana dot. dokumentacji / readme itd. 
        - style - zmiana dot. np. formatowania kodu, ale nie zmieniajaca jego logiki 
        - refactor - refactor jakies funkcji itd. 
        - perf - zmiana usprawniajaca performance aplikacji 
        - test - testy jednostkowe / e2e / functional itd
    - Typing (mypy*)
    - Docstring (na końcu)


3. Tools (Ze Stachem)
   - Pre-commit (black, flake8) odpala lintery i formatery przy commicie (dokładnie przed)
   - ew. CI na GithubActions* 