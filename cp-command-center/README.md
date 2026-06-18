# CP Command Center

CP Command Center is a static, iPhone-first personal dashboard PWA. It is designed to be deployed to a public HTTPS host and used from iPhone Safari or Add to Home Screen on Wi-Fi or 5G/cellular.

It does not require login, a MacBook server, localhost, 192.168.x.x, Verizon Cloud, iCloud file opening, or a backend server.

## Included Sections

- Daily Brief
- Weather
- LIRR Babylon Line / Commute
- Home Maintenance
- MPG Tracker
- Bird and Wildlife Sightings
- Retirement Tracker
- Work Notes
- Health Metrics
- Vacation Planner
- Settings
- Help / Troubleshooting

## Data

User-entered data is stored in this browser with `localStorage`. It stays on the phone/browser unless you export it or later add cloud sync.

The app does not fake live weather, LIRR, markets, or news. Weather and LIRR show clear setup messages until real API keys and providers are configured.

## Deploy To Netlify

Recommended host: Netlify, because this project is static and already includes `netlify.toml`.

1. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag the `CP Command Center` folder onto the Netlify deploy area.
3. Wait for Netlify to publish the site.
4. Open the `https://...netlify.app` URL on your iPhone using cellular service.
5. In Safari, tap Share, then Add to Home Screen.

Do not use `localhost`, a `192.168.x.x` address, AirDrop, Verizon Cloud, iCloud Drive, or direct `index.html` file opening as the final app path.

## Deploy To GitHub Pages

1. Put these files in a GitHub repository.
2. In repository Settings, open Pages.
3. Set the source to the branch and folder that contains `index.html`.
4. Open the generated `https://USERNAME.github.io/REPO/` URL.

All asset paths are relative, so subfolder hosting works.

## iPhone Test Steps

1. Open the public HTTPS URL in iPhone Safari.
2. Confirm visible dashboard content appears immediately.
3. Turn off Wi-Fi and confirm the same URL works over 5G/cellular.
4. Add a Home Maintenance task, close Safari, reopen, and confirm it persists.
5. Tap through every bottom navigation item.
6. Add the app to Home Screen from Safari.
7. Launch it from the Home Screen icon.
8. Put the phone in Airplane Mode and reopen the app; saved local content should still load after the first successful online visit.
9. Confirm Weather and LIRR say setup is required unless real API keys are saved.

## Troubleshooting

If the app ever opens blank, clear Safari website data for the deployed site and reload. The HTML includes visible fallback text before JavaScript starts, and runtime errors are shown in a banner instead of intentionally leaving a white screen.

Service worker registration uses `./sw.js`, not `/sw.js`, so hosting in a subfolder will not break the app. If service worker registration fails, the app logs the error and continues without offline cache.

## Files

- `index.html` - PWA metadata, static startup fallback, and app structure
- `styles.css` - iPhone-first layout with safe-area padding and touch-friendly controls
- `app.js` - Local data app, navigation, persistence, import/export, and safe service worker registration
- `manifest.json` - PWA manifest with relative start URL, scope, and PNG icons
- `sw.js` - Static asset cache with offline fallback
- `offline.html` - Offline fallback page
- `netlify.toml` - Netlify static deploy configuration
- `icons/` - Manifest and Apple touch PNG icons
