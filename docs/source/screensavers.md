# Custom Screensavers

The **Screensavers** tab lets you upload, manage, and remove custom Kindle sleep screen images through the web UI.

![Screensavers UI](https://github.com/user-attachments/assets/b227f533-8dd7-4d6f-926f-6208b176d013)

## How It Works

1. Go to the **Screensavers** tab in the web UI
2. Your Kindle model and screen resolution are auto-detected from the device serial number
3. Drag and drop (or click to select) any image — color photos work fine
4. Use the crop editor to zoom and pan the image into position
5. Click **Upload Screensaver** — the image is automatically:
   - Resized to the exact device resolution
   - Converted to grayscale using luminance weighting
   - Encoded as a proper 8-bit grayscale PNG (color type 0) using @lunapaint/png-codec
   - Saved to `/usr/share/blanket/screensaver/` as `bg_ssNN.png`

## Managing Screensavers

- **Disable** moves a screensaver from the active directory to `/mnt/us/screensaver_disabled/` so it won't show on the lock screen but can be restored later
- **Enable** moves a disabled screensaver back to the active directory
- **Delete** permanently removes the image

## Supported Models

The tool auto-detects resolution from the Kindle serial number. Supported devices include all e-ink Kindles from Kindle 1 through Kindle Scribe Colorsoft (2025), covering resolutions from 600×800 to 1860×2480.

## Important Notes

- **Disable "Show covers on lock screen"** in Kindle Settings > Screen & Brightness, otherwise custom screensavers won't appear
- **Ads/Special Offers** must be removed first (paid removal or jailbreak ad-disable script)
- Images must be 8-bit grayscale PNG at the device's exact resolution — the upload tool handles this conversion automatically, but uploading malformed images manually can cause the Kindle to freeze on sleep
- Factory screensavers (`bg_ss00.png` through `bg_ss06.png`) can be disabled and re-enabled without deleting them
