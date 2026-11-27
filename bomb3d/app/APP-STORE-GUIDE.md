# Putting Bomb 3D Simulator on the App Store

This folder turns the game into a real iPhone and iPad app. Everything that can be prepared ahead of time is already here. The last steps need a grown-up, because Apple requires:

- an **Apple Developer account** (sign up at developer.apple.com; it costs $99 a year and the account holder must be 18+)
- a **Mac** with **Xcode** (free from the Mac App Store) and **Node.js** (free from nodejs.org)

## What's in this folder

| File | What it is |
|---|---|
| `www/` | The finished offline app: the game plus its 3D engine and fonts, so it needs no internet |
| `build.py` | Rebuilds `www/` from the game (`../index.html`). Run it after every game update |
| `package.json`, `capacitor.config.json` | Settings for **Capacitor**, the free tool that wraps the game in a real iOS app |
| `assets/icon-1024.png` | The App Store icon (plus smaller sizes) |
| `store/listing.md` | The name, subtitle, description, keywords, category and age-rating answers to paste in |
| `store/privacy-policy.html` | A privacy policy page (the app collects no data) |
| `store/screenshots/` | App Store screenshots for iPhone (1290 × 2796) and iPad (2048 × 2732) |

## Step 1: make the Xcode project (on the Mac, once)

Open Terminal in this `app` folder and run:

```
npm install
python3 build.py
npx cap add ios
npx cap open ios
```

Xcode opens the app project.

## Step 2: set it up in Xcode

1. Click **App** in the left sidebar, then the **Signing & Capabilities** tab. Choose your **Team** (your Apple Developer account).
2. Change the **Bundle Identifier** from `com.example.bomb3dsimulator` to your own, for example `com.yourname.bomb3d`. Use the same one in `capacitor.config.json`.
3. **App icon:** in the sidebar open `App › Assets › AppIcon` and drag in `assets/icon-1024.png`.
4. Under **General › Deployment Info**, tick iPhone and iPad, and allow Portrait and Landscape.
5. Plug in an iPhone or iPad, pick it at the top of the window, and press ▶ to try the game on the real device.

## Step 3: upload it

1. In Xcode choose **Product › Archive**. When it finishes, click **Distribute App › App Store Connect › Upload**.
2. Go to **appstoreconnect.apple.com**, click **My Apps › +** and create the app with the same bundle ID.
3. Fill in the page using `store/listing.md`, upload the screenshots from `store/screenshots/`, and paste the link to your hosted privacy policy.
4. Tip: try it with friends and family first using **TestFlight** (in App Store Connect).
5. Press **Submit for Review**. Apple usually answers within a day or two.

## Updating the app later

After the game changes, run:

```
python3 build.py
npx cap sync ios
```

Then raise the version number in Xcode, and Archive and upload again.

## Good to know

- **Multiplayer** (and photo saving) only works in the claude.ai version of the game, so the app is single-player. Everything else works offline.
- Progress is saved on each device separately.
- If Apple asks about it: the app has no ads, no in-app purchases, no accounts and collects no data.
