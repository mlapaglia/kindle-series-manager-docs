# Back Up Your Database

This tool modifies your Kindle's content catalogue database (`/var/local/cc.db`) directly. If something goes wrong, a corrupt or incorrect database can cause books to disappear from your library until the database is fixed. **Always create a backup before making changes.**

## Using KUAL Backup/Restore

The KUAL menu includes **Backup Database** and **Restore Database** actions:

- **Backup Database** copies `/var/local/cc.db` to `/var/local/cc.db.bak`
- **Restore Database** stops `ccat`, copies the backup back over `cc.db`, and restarts `ccat`

Run **Backup Database** before your first series operation. If anything goes wrong, tap **Restore Database** to revert.
