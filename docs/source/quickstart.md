# Quick Start

## Requirements

- Jailbroken Kindle with KUAL installed
- WiFi connection (Kindle and phone/PC on the same network)
- "Group Series in Library" enabled in Kindle Settings

## Installation

1. Copy the `kindle-series-manager` folder inside `kual-extension/` to your Kindle at:

   ```
   Internal Storage/extensions/kindle-series-manager/
   ```

2. Open KUAL, tap **Start Web UI** under "Kindle Series Manager"
3. Note the URL shown on the Kindle screen (e.g. `http://10.0.0.224:8080/`)
4. Open that URL on your phone or PC (same WiFi network)
5. Tap **Create Series**, name it, select your books, drag them into reading order, and hit Create

## Starting the Web UI

1. Make sure WiFi is on
2. Open KUAL, tap **Start Web UI**
3. The Kindle screen shows the URL (e.g. `http://10.0.0.224:8080/`)
4. Open that URL on your phone or PC

## Stopping the Server

Open KUAL and tap **Stop Web UI**. This kills the HTTP server and removes the firewall rule.
