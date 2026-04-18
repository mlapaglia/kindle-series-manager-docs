# Kindle Series Manager

Group sideloaded books into series on jailbroken Kindle devices, just like Amazon-purchased books.

Amazon's "Group Series in Library" feature (firmware 5.13.4+) only works with store-purchased content. This KUAL extension lets you create, manage, and remove series groupings for sideloaded books through a web interface served from the Kindle itself.

## How It Works

The extension runs a lightweight HTTP server on the Kindle (a static busybox binary bundled with the extension). You access the web UI from your phone or PC browser. The web UI reads and modifies the Kindle's content catalogue database (`/var/local/cc.db`) through shell CGI scripts, creating the same database structures that Amazon uses for store-purchased series.

### Web UI Features

- **My Series** — view all series on the device with book lists; edit or remove series with one tap
- **Create Series** — two-panel interface: pick books from your library on the right, they appear in the reading order panel on the left. Drag to reorder. Optionally provide an Amazon series ASIN for better firmware integration. Control program badge display (KU/Prime Reading)
- **Progress Tracking** — configure Goodreads credentials, sign in, build book mappings, and monitor the sync service status and logs
- **Screensavers** — upload custom sleep screen images with drag-and-drop, auto-resize, grayscale conversion, and a crop editor. Manage active and disabled screensavers

```{toctree}
:maxdepth: 2
:caption: Contents

quickstart
series
goodreads
screensavers
cli
backup
```
