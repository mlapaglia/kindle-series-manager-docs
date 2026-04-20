# Calibre Integration

The **Calibre** tab lets you browse your [Calibre](https://calibre-ebook.com/) library from the web UI and download books directly to your Kindle over WiFi — no USB cable or email delivery needed.

![Calibre UI](https://github.com/user-attachments/assets/9dcf65c0-01e3-422e-a635-e1b5c4fd0eb6)

## Prerequisites

- Calibre installed on a computer on the same network as your Kindle
- The Calibre Content server running and accessible from the Kindle's network

### Starting the Calibre Content Server

1. Open Calibre on your computer
2. Click the **Connect/share** button in the toolbar
3. Click **Start Content server**
4. Note the IP address and port shown (e.g. `192.168.1.100, port 8080`)

You can verify it's working by visiting `http://192.168.1.100:8080` in a browser on any device on the same network. You should see the Calibre library interface.

For detailed configuration options (running as a service, HTTPS, authentication, reverse proxies), see the [official Calibre Content server documentation](https://manual.calibre-ebook.com/server.html).

## Using the Calibre Tab

1. Start the Kindle Series Manager web UI and go to the **Calibre** tab
2. Enter your Calibre server URL (e.g. `http://192.168.1.100:8080`) and click **Scan**
   - The URL is saved on the Kindle so you only need to enter it once
3. Your Calibre library appears with cover thumbnails, titles, authors, and file formats
4. Use the search box and sort/order dropdowns to find books
5. Pagination controls at the bottom let you navigate through large libraries

### Downloading Books

**Single book:** Click the **Download** button next to any book.

**Multiple books:** Check the boxes next to the books you want, then click **Download Selected**. Selections persist across pages, so you can check books on page 1, navigate to page 2, check more, and download them all at once.

Downloaded books are saved to `/mnt/us/documents/` on the Kindle. After downloading, the Kindle's content catalog is automatically refreshed so books appear in the library immediately.

## Supported Formats

The download accepts the same formats as the Upload Books tab: AZW3, AZW, MOBI, KFX, EPUB, and PDF. Calibre serves whichever format is available in your library — if you have multiple formats for a book, Calibre picks one automatically based on its configured output format preference.

If you need a specific format, convert the book in Calibre first (right-click → Convert books) and the Content server will serve the new format.

## Troubleshooting

- **"Failed to reach Calibre"** — Check that the Content server is running, the URL is correct, and your Kindle and computer are on the same network
- **Thumbnails not loading** — The Kindle proxies thumbnail requests through a CGI script. If covers don't appear, the Calibre server may be slow to respond or the thumbnail path may differ between Calibre versions. Books will still download correctly without thumbnails
- **Download fails** — Large files may time out over slow WiFi. Try downloading fewer books at once. The file size limit is the same as the Upload tab (50MB per file)
- **Books don't appear after download** — The library refresh restarts the `ccat` service. If books still don't appear, restart the Kindle
- **Authentication required** — If your Calibre server requires a username and password, include them in the URL: `http://username:password@192.168.1.100:8080`
