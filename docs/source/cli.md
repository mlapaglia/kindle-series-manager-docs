# Standalone CLI Tool

The `kindle_series.py` script can be used independently on a PC for direct database manipulation. Copy `cc.db` from the Kindle, modify it locally, and push it back.

## Transferring the Database

```bash
# Copy cc.db from Kindle
scp root@<kindle-ip>:/var/local/cc.db ./cc.db
```

## Commands

### Inspect the database

```bash
python kindle_series.py diagnose
python kindle_series.py list --filter "Expanse"
python kindle_series.py dump B08BX5D4LC
```

### Create a series

```bash
python kindle_series.py add-series --name "The Expanse" --books "key1,key2,key3"

# With an Amazon series ASIN
python kindle_series.py add-series --name "The Expanse" --asin B09DD17H3N --books "key1,key2,key3"
```

### Remove a series

```bash
python kindle_series.py remove-series --series-id "urn:collection:1:asin-SL-THE-EXPANSE"
```

## Pushing Changes Back

After modifying the database, push it back and restart the content catalogue:

```bash
ssh root@<kindle-ip> "stop com.lab126.ccat"
scp cc.db root@<kindle-ip>:/var/local/cc.db
ssh root@<kindle-ip> "start com.lab126.ccat"
```
