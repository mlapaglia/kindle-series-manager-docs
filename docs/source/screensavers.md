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

## FBInk Screensaver Mode

An alternative screensaver rendering method is available that uses [FBInk](https://github.com/NiLuJe/FBInk) to draw screensaver images directly to the e-ink framebuffer instead of relying on the Kindle's built-in `blanket` screensaver module.

### Why use it?

The stock screensaver module is strict about image format — a malformed PNG (wrong bit depth, incorrect resolution, bad encoding) can cause the Kindle to freeze on sleep, sometimes requiring a hard reboot or USB recovery. The FBInk method avoids this entirely because the image is rendered by FBInk rather than the firmware's blanket process. If an image fails to load, FBInk simply reports an error and the device sleeps with a blank screen instead of crashing.

This makes it **safer for user-uploaded screensavers**, especially when images are uploaded through the web UI or copied to the device manually.

### How to enable it

1. Open KUAL
2. Under "Kindle Series Manager", tap **Enable FBInk Screensaver**
3. The daemon starts in the background and takes over screensaver rendering

The daemon cycles through the same `bg_ss*.png` images in `/usr/share/blanket/screensaver/` that the stock screensaver uses, so uploading images through the Screensavers web UI tab works exactly the same way. The only difference is how the images are drawn to the screen.

To disable it, open KUAL and tap **Disable FBInk Screensaver**. The stock screensaver is restored immediately.

### How it works

When enabled, the daemon:

1. Unloads the stock `screensaver` module from the `blanket` process
2. Listens for `goingToScreenSaver` events from `com.lab126.powerd`
3. On sleep: raises a full-screen X11 shield window to block status bar repaints, then draws the next screensaver image with FBInk
4. On wake: removes the shield window and triggers an X11 refresh so the app repaints

The shield window (`ss_shield`) is a small statically-linked ARM binary that creates an override-redirect X11 window covering the entire screen. This prevents the system status bar (clock, wifi, battery indicators) from painting over the screensaver image during the period between sleep activation and device suspend. The stock screensaver achieves this by creating its window at the highest Z-order through the proprietary `libblanket` API; `ss_shield` accomplishes the same result using standard X11 override-redirect, which bypasses the window manager entirely.

The device still sleeps and wakes normally. Battery life is unaffected.

### Requirements

- A full-featured FBInk binary with image support must be available on the device (the version bundled with KOReader is a minimal build without image support — the version from `libkh` or MRInstaller works)
- Jailbroken Kindle with KUAL installed

### Using both features together

The recommended workflow is:

1. Use the **Screensavers** web UI tab to upload, crop, and manage your screensaver images
2. Enable **FBInk Screensaver** in KUAL for safer rendering

The web UI handles image conversion (resize, grayscale, proper PNG encoding) and places files in the screensaver folder. The FBInk daemon picks them up and draws them. You get the convenience of the web uploader with the stability of FBInk rendering.

## Important Notes

- **Disable "Show covers on lock screen"** in Kindle Settings > Screen & Brightness, otherwise custom screensavers won't appear (not required when using FBInk Screensaver mode)
- **Ads/Special Offers** must be removed first (paid removal or jailbreak ad-disable script)
- Images must be 8-bit grayscale PNG at the device's exact resolution — the upload tool handles this conversion automatically, but uploading malformed images manually can cause the Kindle to freeze on sleep when using the stock screensaver (the FBInk method is not affected)
- Factory screensavers (`bg_ss00.png` through `bg_ss06.png`) can be disabled and re-enabled without deleting them
