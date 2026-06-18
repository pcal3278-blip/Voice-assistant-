# CP Command Center

A mobile-first iPhone PWA for Paul’s daily command dashboard.

## What this version does

- Opens on iPhone Safari and can be added to the Home Screen.
- Works from Netlify over Wi-Fi or 5G/cellular service.
- Does not require a Mac local server, Verizon Cloud, iCloud Drive, or AirDrop after deployment.
- Saves data locally on the device using `localStorage`.
- Keeps loading even when weather or network calls fail.
- Includes a service worker for offline startup.

## Sections included

- Daily Brief
- Weather
- LIRR / Commute
- Home Maintenance
- MPG Tracker
- Retirement Tracker
- Bird / Wildlife Sightings
- Vacation Deals
- Notes / Tasks
- Focus Modes

## Netlify deployment

This repository includes `netlify.toml` at the repo root.

Netlify should use:

- Build command: leave blank
- Publish directory: `cp-command-center`

## iPhone install steps

1. Open the deployed Netlify site in Safari on the iPhone.
2. Tap Share.
3. Tap Add to Home Screen.
4. Name it `CP Command`.
5. Open it from the new Home Screen icon.

## Test checklist

- App loads without a white screen.
- Home tab opens.
- Weather tab opens.
- West Babylon weather button does not crash the app.
- Add a task.
- Mark a task done.
- Save a note.
- Add MPG entry.
- Save retirement snapshot.
- Add home maintenance item.
- Add wildlife sighting.
- Refresh app and confirm data remains.
- Turn on Airplane Mode and confirm app shell still opens.

## Important note

This is a local-first app. Weather uses Open-Meteo when online. LIRR information is not live yet; it stores your regular commute plan and notes. Live MTA data can be added later through an API-backed function or Netlify serverless function.
