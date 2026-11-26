/* ticker.c
   Semplice ticker testuale per terminale (POSIX + Windows)
   Compila: gcc -o ticker ticker.c       (Linux/macOS)
           gcc -o ticker.exe ticker.c   (Windows, MinGW)
   Esempio: ./ticker "Ciao! Questo testo scorre..." 100
   Il secondo argomento (opzionale) è la velocità in millisecondi per passo.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
  #include <windows.h>
#else
  #include <unistd.h>
  #include <sys/ioctl.h>
  #include <termios.h>
#endif

/* Ottieni la larghezza del terminale (numero di colonne) */
int get_terminal_width(void) {
#ifdef _WIN32
    CONSOLE_SCREEN_BUFFER_INFO info;
    if (!GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info)) return 40;
    return info.srWindow.Right - info.srWindow.Left + 1;
#else
    struct winsize w;
    if (ioctl(1, TIOCGWINSZ, &w) == -1) return 40;
    return (w.ws_col > 0) ? w.ws_col : 40;
#endif
}

/* sleep in milliseconds */
void msleep(unsigned int ms) {
#ifdef _WIN32
    Sleep(ms);
#else
    usleep(ms * 1000);
#endif
}

int main(int argc, char *argv[]) {
    const char *msg = (argc > 1) ? argv[1] : " Esempio ticker: Hello world! ";
    int speed_ms = 100; // default 100 ms per step
    if (argc > 2) {
        int v = atoi(argv[2]);
        if (v > 0) speed_ms = v;
    }

    int termw = get_terminal_width();
    int msglen = (int)strlen(msg);

    /* Costruiamo un buffer che contiene il messaggio ripetuto + spazi per lo scorrimento */
    int pad = termw; /* spazio sufficiente per nascondere il testo quando scorre via */
    int buflen = msglen + pad;
    char *buf = malloc(buflen + 1);
    if (!buf) {
        fprintf(stderr, "Memoria insufficiente\n");
        return 1;
    }
    /* copia messaggio e poi pad di spazi */
    memcpy(buf, msg, msglen);
    for (int i = 0; i < pad; ++i) buf[msglen + i] = ' ';
    buf[buflen] = '\0';

    int pos = 0;
    /* ciclo infinito: scorri la finestra di larghezza 'termw' sul buffer circolare */
    while (1) {
        /* se il terminale è stato ridimensionato, aggiorniamo termw e pad (semplice) */
        int neww = get_terminal_width();
        if (neww != termw) {
            termw = neww;
            free(buf);
            pad = termw;
            buflen = msglen + pad;
            buf = malloc(buflen + 1);
            if (!buf) break;
            memcpy(buf, msg, msglen);
            for (int i = 0; i < pad; ++i) buf[msglen + i] = ' ';
            buf[buflen] = '\0';
            pos = 0;
        }

        /* costruiamo e stampiamo la finestra corrente */
        /* stampiamo due volte il buffer concatenato per semplificare il wrap */
        int take = termw;
        /* output con carriage return per restare sulla stessa riga */
        putchar('\r');
        fflush(stdout);

        if (pos + take <= buflen) {
            /* substring semplice */
            fwrite(buf + pos, 1, take, stdout);
        } else {
            /* avvolgimento: prima parte fino a fine, poi da inizio */
            int first = buflen - pos;
            fwrite(buf + pos, 1, first, stdout);
            fwrite(buf, 1, take - first, stdout);
        }
        fflush(stdout);

        /* avanzamento */
        pos++;
        if (pos >= buflen) pos = 0;

        msleep((unsigned int)speed_ms);
    }

    free(buf);
    return 0;
}
