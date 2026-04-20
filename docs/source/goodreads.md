# Goodreads Progress Sync

The extension can automatically sync your reading progress to Goodreads whenever you open or close a book, or when the Kindle goes to sleep. This uses Goodreads' internal progress update endpoint to set your current page.

![Progress Tracking UI](https://github.com/user-attachments/assets/7b5f7f91-c4a1-40bc-8bcf-27ad48051f5f)

## Setup

1. Start the web UI and go to the **Progress Tracking** tab
2. Enter your Goodreads email, password, and user ID, then click **Save Credentials**
   - Your Goodreads user ID is the number in your profile URL: `goodreads.com/user/show/183958037` → `183958037`
   - **Note:** Credentials are stored in plaintext on the device at `goodreads/gr_creds.json` (file permissions are restricted to root). Do not use this on a shared or untrusted device.
3. Click **Sign In to Goodreads** — the output panel shows the login flow. On success you'll see "Login successful!"
4. Click **Build Mapping** — this fetches your Goodreads "currently-reading" shelf and matches those books against your Kindle library by title. The results table shows which books were matched.
5. In KUAL, tap **Enable Goodreads Sync** to start the background sync daemon

## How It Works

A background daemon listens for two Kindle system events:

- `appActivating` from `com.lab126.appmgrd` — fires when you open or close a book
- `goingToScreenSaver` from `com.lab126.powerd` — fires when the Kindle goes to sleep

When either event fires, the daemon queries `cc.db` for the most recently accessed book, checks if it's in the Goodreads mapping, compares the current `p_percentFinished` against the last synced value, and if it changed, calculates the page number and pushes an update to Goodreads.

Page numbers are calculated as `round(percentFinished * totalPages / 100)` where `totalPages` comes from Goodreads' `finalPosition` field (fetched once per book and cached).

## Auto-Start on Boot

When you enable Goodreads Sync via KUAL, the extension installs an upstart job (`/etc/upstart/gr-sync.conf`) that starts the daemon automatically after the Kindle boots and WiFi connects. A flag file at `/mnt/us/ENABLE_GR_SYNC` controls whether the daemon runs — remove it to disable auto-start.

## Troubleshooting

- Check the **Sync Log** section in the Progress Tracking tab for error messages
- If login fails, check that your credentials are correct and that you're using email login (not Amazon SSO)
- If books don't match, make sure they're on your Goodreads "currently-reading" shelf with titles that closely match the Kindle book titles
- Session cookies may expire — if syncs start failing, click **Sign In to Goodreads** again from the web UI
- Log file location on the Kindle: `/mnt/us/extensions/kindle-series-manager/goodreads/gr_sync.log`
