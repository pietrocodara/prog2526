# Introduzione alla programmazione in Python
# (Brevi dispense del corso pomeridiano)

## Lezione 1

### Informazioni pratiche

- Docente: Pietro Codara
- Email: cognome.nome@issvigano.edu.it
- Server Discord: vedi https://www.vigainsider.it/giochi/
- Questo file è in formato markdown (estensione `md`); per vederlo *ben formattato* sul vostro PC potete aprirlo in VS Code (vedi di seguito), cliccare con il tasto destro sul nome del file e scegliere *Open Preview*. Se volete imparare ad usare markdown per scrivere i vostri appunti: https://www.markdownguide.org/basic-syntax/

\
Calendario del corso:
1) Giovedì 30/10/25, 14:20-16:20
2) Giovedì 06/11/25, 14:20-16:20
3) Giovedì 13/11/25, 14:20-16:20
4) Giovedì 20/11/25, 14:20-16:20
5) Giovedì 27/11/25, 14:20-16:20

Gli incontri si terranno nel Lab Triennio ITI, in Palazzina, al primo piano. In caso di assenza avvisate il docente per email.

### Configurazione ambiente di sviluppo

- Installazione Python: https://www.python.org/
- Scaricate l'ultima versione di Python per il vostro OS dalla sezione downloads del sito
- Installate come una normale applicazione, mantenendo le impostazioni di default
- Installazione Visual Studio Code, un noto editor utilizzato per la programmazione in diversi linguaggi: https://code.visualstudio.com/
- scaricate ed installate l'ultima versione stabile di VS Code per il vostro OS

- Ci sono diverse alternative al download da python.org: download da MS store (Win); usare gestori di pacchetti (Chocolatey, Scoop); installare Anaconda, Miniconda; etc.


### Scrivere ed eseguire un programma in VS code

*Visual Studio Code* (*VS Code*, in breve) è un editor di testo con funzionalità avanzate per la programmazione.  È utilizzato come ambiente di sviluppo per scrivere programmi in diversi linguaggi. Noi lo useremo per questo primo esercizio di programmazione in Python. Non è una scelta obbligata: potreste usare un qualsiasi altro editor già installato sul vostro sistema, come *Blocco Note* (scelta sconsigliata!), o l'ambiente di sviluppo *IDLE*, già compreso nel pacchetto di installazione di Python.

Per scrivere il nostro primo programma in Python, eseguiamo le seguenti operazioni.

1) Creiamo (ad esempio dallo strumento *Esplora file* di Windows) una cartella dove mettere i nostri programmi. Evitate di utilizzare sempre il Desktop ;)
2) Da VS Code, apriamo la cartella appena creata scegliendo *Open folder* nel menù *File*.
3) Nella barra *Explorer* di VS Code, che potete aprire/chiudere cliccando sul tasto in altro a destra, sotto il simbolo dell'applicazione, clicchiamo sul pulsante che si trova alla destra del nome della cartella (passandoci sopra compare la scritta *new file*) e creiamo un nuovo file con estensione `py`. Chiamiamo il file `ciao.py`. Se sbagliate a digitare il nome del file potete rinominarlo cliccandoci sopra con il tasto destro, oppure selezionandolo e premendo F2.
4) Apriamo, cliccandoci sopra, il file `ciao.py` ed *editiamolo* inserendo la seguente *linea di codice*. Dopo aver fatto le vostre modifiche ricordatevi di salvare il file!
    ```python
    print('Ciao mondo!')
    ```
5) Apriamo il *terminale*, cliccando sulla barra in basso oppure dal menù *View* scegliendo *Terminal*, e verifichiamo la presenza di Python digitando `py` (oppure `python` o `python3`). Dovrebbe aprirsi l'interfaccia a linea di comando dell'*interprete Python*. Da questa interfaccia possiamo eseguire comandi Python: provate a scrivere `2+3` e premete invio. Per uscire scriviamo `exit()` dopo il *prompt*, rappresentato dal simbolo  `>>>`.
6) Eseguiamo il file `ciao.py` dal terminale, digitando il comando `py ciao.py` (se non funziona `py`, usate `python` o `python3`, come avete fatto al punto precedente).

Nota: possiamo digitare i comandi da terminale più velocemente usando qualche trucchetto. Premendo `tab` dopo aver digitato qualche carattere viene completato automaticamente il nome del file. Premendo la freccia in alto si richiama l'ultimo comando (usando *freccia su* e *freccia giù* potete navigare lo storico dei comandi digitati).

### Alternativa: utilizzare l'ambiente Idle

Proviamo a eseguire lo stesso programma nell'ambiente *Idle*, incluso nell'installazione standard di Python. Cerchiamo e apriamo *Idle* sul nostro computer. Si aprirà una finestra con la *shell* che ci permette di inviare comandi direttamente all'interprete Python. Andiamo ora sul menù *file*, scegliamo *open* e apriamo il file *ciao.py* che abbiamo editato prima in VS Code. Si aprirà la finestra dell'editor, dove possiamo vedere e modificare il nostro programma. Accediamo da questa finestra al menù *Run* e selezioniamo *Run module*. Il programma verrà eseguito e l'output visualizzato sulla shell.


### Alternativa: usare Google Colab (senza installare Python)

Se non volete (o non potete) installare niente sul PC, potete svolgere gli esercizi del corso direttamente nel browser con Google Colab.

- Aprite Colab: https://colab.research.google.com/
- Create un nuovo notebook
- Verificate la versione di Python eseguendo in una cella
	```python
	import sys
	print(sys.version)
	```
- Aggiungete una nuova cella di codice, inserite il seguente testo ed eseguite mediante l'apposito pulsante
	```python
	print('Ciao mondo!')
	```
- Per caricare ed eseguire uno script `.py` (es. `ciao.py`):
	1. Cliccate sull'icona cartella a sinistra → Carica file → selezionate il vostro `.py`.
	2. Eseguite lo script:
    ```python
    %run ciao.py
    # oppure
    !python ciao.py
    ```



### La funzione `print()`

Prepariamo ora una seconda versione del nostro programma, che possiamo chiamare `ciao2.py`.
```python
print('Hello, world!')
print("Ciao mondo!")
```

Il programma esegue per due volte la *funzione* `print()` di Python. La funzione `print()` permette di stampare una *stringa*, ovvero una sequenza di caratteri di testo. Nel nostro programma la prima *invocazione* della funzione `print()` stamperà la stringa `Hello world!`. Una stringa in Python può essere delimitata in diversi modi: possiamo usare il simbolo `'` (apice), come in `'Hello world'` oppure il simbolo `"` (doppio apice o virgoletta), come in `"Ciao mondo!"`. 

Eseguendo il programma con il solito comando `py ciao2.py` viene visualizzato sul terminale il seguente *output*.

```
Hello world!
Ciao mondo!
```

Torniamo ora a "lavorare" sul nostro editor VS code. Premete il pulsante in basso della barra sinistra dei pulsanti (se ci passate sopra con il mouse compare la scritta *Extensions*). Viene visualizzato un elenco di *estensioni* che potete installare in VS code per aumentarne le funzionalità. Dal campo di ricerca in alto cercate *Python*. Dovreste trovare un'estensione chiamata Python, creata da Microsoft. Installatela premendo l'apposito pulsante. Dovrebbe comparirvi una schermata che conferma l'avvenuta installazione e descrive l'estensione, fornendo alcune istruzioni per configurarla e utilizzarla.

Tornate ora sul codice del programma `ciao2.py`. Cliccate sul tasto *play* (*run python file*) che si trova alla destra del nome del file che state editando. Vedrete comparire sul terminale il comando per eseguire il programma (in forma estesa e con tutti i percorsi assoluti completi) e, poco dopo, il risultato dell'esecuzione. Un terzo modo per eseguire il programma è accedere al menù *Run* e cliccare su *Run without debugging*. Un altro modo, equivalente al precedente, è premere `CTRL+F5`.


### Variabile

Una *variabile* è un riferimento a un *dato* che è salvato in memoria. Il nome dato a una variabile dal programmatore ricorda spesso (ma non sempre, dipende dalla scelta del programmatore) il significato del valore memorizzato: per esempio, si può usare il termine *nome* o il termine *name* per una variabile in cui è memorizzato il nome di una persona; si può usare il termine *eta* (meglio se senza accenti: non ci piace usare caratteri così strani come le lettere accentate nei nostri programmi) o il termine *age*, ad esempio, per una variabile dove è salvata l'età di una persona, e così via. La *variabile* è lo strumento più semplice e comodo che possiamo usare nei nostri programmi per memorizzare dati, recuperare valori memorizzati e manipolarli. Per introdurre una nuova variabile in Python e *assegnare* alla variabile un nuovo valore si usa l'istruzione:

```python
cognome = "Codara"
```

Questa istruzione *assegna* alla variabile `cognome` il valore `"Codara"`. 
Il simbolo `=` esegue un *assegnamento* (o *assegnazione*) di un valore a una variabile.

Nota: per dare un nome a una variabile potete usare tutti i caratteri dell'alfabeto ed eventualmente anche numero e il carattere `_` (underscore). Non usate un numero all'inizio del nome. Ad esempio, il nome `citta_1` è valido, ma il nome `76_forever` non lo è.

Possiamo riassegnare il valore a una variabile in un nostro programma. Apriamo nel nostro editor un nuovo file, chiamato `variabile.py` e scriviamo:

```python
stringa = "Pietro"
print(stringa)
stringa = "Casa"
print(stringa)
```

Analizziamo il programma scritto. La prima *riga* assegna il valore `"Pietro"` alla variabile chiamata `stringa`. La seconda riga stampa il valore della variabile. Notate che il testo dentro le parentesi della funzione `print()`, che si chiama *parametro* della funzione ed è un valore *passato* alla funzione in modo che questa possa utilizzarlo, non è racchiuso tra apici. Non si tratta infatti di una stringa, ma è piuttosto il nome di una variabile. Non commettete l'errore di scrivere `print('stringa')`: verrebbe stampato in output `stringa` e non, come desiderato, `Pietro`. Anzi, provate a commettere questo errore, eseguite il programma e osservate cosa succede!

Alla terza riga viene assegnato alla variabile un nuovo valore: la stringa `"Casa"`. Il valore memorizzato in precedenza, la stringa `"Pietro"` non sarà da questo momento più accessibile, perché il nuovo valore contenuto nella variabile `stringa` è la stringa `"Casa"`. 

Nell'ultima riga del programma viene salvato il nuovo valore di `stringa`, mostrando così ciò che è successo con l'assegnamento della riga 3.

Domanda: è possibile fare in modo che la funzione `print()` non vada a capo dopo aver stampato la stringa? Risposta: si, anche se di norma (di *default*) la funzione `print()` stampa *un carattere di a capo* dopo il testo ricevuto come parametro, è possibile modificare questo comportamento.
Per farlo, dobbiamo *passare* alla funzione `print()` un altro parametro, anche se "in un modo abbastanza strano", che capiremo più avanti:

```python
stringa = "Pietro"
print(stringa,end=" --- ")
stringa = "Casa"
print(stringa)
```

Eseguendo questo programma, immediatamente dopo la stringa `Pietro` viene stampato il testo ` --- ` (spazi iniziale e finale inclusi) e poi la stringa `Casa`. Come risultato, vedremo sul terminale la stampa: `Pietro --- Casa`.

Osservazione: spesso, quando si cita il nome di una *funzione* si mette in coda al nome una coppia di parentesi tonde, senza parametri all'interno, ad indicare che si tratta di una funzione e non di altro, ad esempio non di una variabile. Per esempio, abbiamo parlato nelle righe precedenti della funzione `print()`. 

Proviamo a modificare il programma  `variabile.py` che abbiamo scritto poco fa, scrivendo questa volta:

```python
stringa = "Pietro"
print(Stringa)
stringa = "Casa"
print(stringa)
```

Eseguiamo il programma dopo questa modifica. Dovremmo ottenere un output simile a questo:
```
Traceback (most recent call last):
  File "Z:\python\variabile.py", line 2, in <module>
    print(Stringa)
          ^^^^^^^
NameError: name 'Stringa' is not defined. Did you mean: 'stringa'?
```

L'interprete Python ci sta segnalando che la seconda riga (`"Z:\python\variabile.py", line 2`) contiene un errore. In particolare, si tratta di un `NameError` ed è dovuto al fatto che l'interprete non conosce il nome `Stringa` (`name 'Stringa' is not defined`). In effetti, il simbolo `Stringa` che chiediamo alla `print()` di stampare non esiste: l'unica variabile nel nostro programma è `stringa`, con l'iniziale minuscola, e per Python le lettere maiuscole e le lettere minuscole sono *diverse* (si dice che il linguaggio è *case sensitive*).

Questo messaggio dell'interprete è molto importante, perché ci permette di correggere il nostro programma. Commetterete molti errori nel programmare e molti di questi verranno segnalati in questo modo dall'interprete: leggete sempre il messaggio che viene stampato con attenzione! Non sarà sempre facile capire cosa vuole dirci, ma con l'esercizio imparerete a capire al volo ciò che sta dietro a tutti i messaggi d'errore più comuni.

### Metodi per le stringhe

Giochiamo un po' con le stringhe.

```py
nome = 'Alan'
print("Ciao " + nome + " Turing " + "!")
print("Ciao", nome, "Turing", "!")

nome_completo = nome + " Turing"
print(nome_completo)

saluto = "Ciao " + nome_completo
print(saluto)
```

Eseguendo il programma qui sopra otteniamo quanto segue.

```
Ciao Alan Turing !
Ciao Alan Turing !
Alan Turing
Ciao Alan Turing
```

Osserviamo che con la funzione `print()` è possibile stampare più valori, separando gli *argomenti* (le stringhe da stampare) che passiamo alla funzione con il carattere `,`. Nella stampa, le varie stringhe passate come argomento vengono separate da uno spazio. È questo il caso della seconda istruzione `print()` eseguita nel codice. Nella prima *chiamata* alla `print()`, invece, si passa un solo argomento alla funzione, una unica stringa ottenuta per concatenazione (utilizzando l'operatore `+`). Il risultato, come si può osservare, è in questo caso lo stesso.


Aggiungendo in coda al precedente programma la riga di codice `print(saluto*3)` otteniamo oltre al vecchio output il testo `Ciao Alan TuringCiao Alan TuringCiao Alan Turing`.

Eseguiamo ora il seguente programma:

```py
nome_cognome = "grace hopper"
print(nome_cognome.upper())
print(nome_cognome.lower())
print(nome_cognome.title())
print(nome_cognome)
```

otteniamo:
```
GRACE HOPPER
grace hopper
Grace Hopper
grace hopper
```

Le *funzioni* `upper()`, `lower()` e `title()` restituiscono la stringa `nome_cognome` modificata: nel primo caso tutti i caratteri diventano maiuscoli, nel secondo minuscoli, nel terzo diventa maiuscola ogni iniziale di parola e minuscolo il resto. Queste funzioni sono un po' "speciali" e lo vediamo perché si *invocano* in maniera diversa rispetto alle funzioni "tradizionali", come `print()`: scriviamo infatti il nome di un *oggetto*, nel nostro caso la stringa `nome_cognome`, poi un carattere `.`, infine il nome della funzioni (con tra parentesi eventuali argomenti). Funzioni di questo tipo si chiamano *metodi*. I metodi eseguono un'azione su un oggetto specifico, nel nostro caso la stringa `nome_cognome`.
Osservate che i metodi `upper()`, `lower()` e `title()` non modificano la stringa `nome_cognome` (è chiaro guardando l'ultima stampa!), ma ne restituiscono una copia modificata.

Esistono molti altri metodi per le stringhe. Ecco un esempio di codice che utilizza `removeprefix()` e `removesuffix()`. Entrambi i metodi ricevono un parametro tra parentesi: il prefisso (o il suffisso) da rimuovere.

```py
url = 'https://www.python.org/'
print(url)
url_senza_prefisso = (url.removeprefix("https://"))
print("Senza prefisso:",url_senza_prefisso)
url_senza_suffisso = (url_senza_prefisso.removesuffix("/"))
print("Senza suffisso:",url_senza_suffisso)
print()
print("Url originale:",url)
```

L'output sarà:
```
https://www.python.org/
Senza prefisso: www.python.org/
Senza suffisso: www.python.org

Url originale: https://www.python.org/
```

Notate che, anche in questo caso, i metodi non hanno modificato la stringa a cui sono stati applicati.

> #### Esercizio 1.1
>
> Aprite il file `ciao.py`. Modificate qualcosa nel codice, ad esempio eliminate un apice all'inizio o alla fine della stringa `Hello world!`. Eseguite il programma e leggete con attenzione il messaggio che viene visualizzato sul terminale. Correggete l'errore e introducetene un altro. Eseguite nuovamente il messaggio e, di nuovo, leggete attentamente ciò che vi viene segnalato. Riportate infine il programma nel suo stato originale ed eseguite.

> #### Esercizio 1.2
> Assegnate a una variabile il titolo della vostra canzone preferita. Fate poi in modo che il vostro programma stampi su terminale, mediante l'esecuzione di funzioni `print()`, il testo `La mia canzone preferita è: titolo`, dove titolo è il contenuto della variabile. Ad esempio, se avete memorizzato nella variabile il valore `Love Will Tear Us Apart` ed eseguite il vostro programma, otterrete sul terminale la stampa `La mia canzone preferita è: Love Will Tear Us Apart`.

> #### Esercizio 1.3
> Scrivete un programma contenente come unica istruzione `import this`. Eseguite il programma e leggete ciò che viene visualizzato sul terminale.
>