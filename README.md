# simple-backup-script

Ein einfaches Python Backup Script zum erstellen eines Website Backups mit Files und DB Dump. Es wird ein Backup der letzten 7 Tage erstellt, sowie ein Archiv pro Woche.

# Config

im Config File muss das DB Login eingetragen werden. Anschliessend können eine oder mehrere Datenbanken eingetragen werden, die Gesichert werden sollen.
Weiter können die verschiedenen Ordner definiert werden, die im Backup enthalten sein sollen.

# Erzeuget Backups

* Es wird pro Wochentag ein Backup Order erstellt: '0-monday', '1-tuesday',...
* Es wird pro Woche ein Archiv erstellt: week-42.tar.gz, week-43.tar.gz,...


