# Damus News

Event-driven geopolitical prediction dashboard. "Damus" is short for Nostradamus: the goal is to see ahead, just a little.

Every event carries a verification status, and the threat indicator moves only on what is confirmed or credibly reported.

**Live site:** https://thompsonryane-collab.github.io/Damus-News/ (GitHub Pages, served from `main`). Desktop browsers only.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | The built dashboard. One self-contained file; open it in a desktop browser. |
| `feed.json` | Daily updates: new events, status changes, forecast updates, run summaries. |
| `src/shell.html` | Page shell and styles (derived from the ANCCRai v1.8 shell). |
| `src/app.js` | Application code: ledger, verification, forecasts, threat model, map, Claude connection. |
| `apps/` | Standalone pages installed as hub tiles. Each ships unmodified and opens in its own frame. Currently the 90-Day Outage Checklist. |
| `icons/` | The Damus mark at every size the site needs: tab icon, Apple touch icon, installable-app icons. See `icons/README.md`. |
| `manifest.webmanifest` | Lets Chrome and Edge install Damus as a desktop app with its own icon. |
| `vendor/` | Leaflet 1.9.4 script and stylesheet. |
| `data/land.json` | Coarse world outline for the offline vector map. |
| `tools/build.py` | Assembles `index.html` from the parts above. |

## Build

```
python3 tools/build.py
```

Edit `src/` and rebuild. Do not edit `index.html` by hand.

## Claude connection

Claude only. Two ways in:

1. The published Claude page uses the built-in connection. No key; no web search.
2. Opened as a file or from a web host, it uses a Claude API key typed into Settings. The key stays in memory for the tab and is never saved. This mode adds live web search for validation.

## Statuses

- **Confirmed**: two or more independent outlets, or a primary source.
- **Reported**: credible reporting from one outlet or unnamed officials.
- **Unverified**: not checked yet.
- **Speculation**: opinion or theory.
- **Disputed**: contradicted by sources or by the people involved.

Only Confirmed (weight 1.0) and Reported (0.4) count toward the threat indicator.

## Daily update

A scheduled Claude task runs at about 4 pm Eastern each day. It researches global news, re-checks open claims and forecasts, and appends to `feed.json`. Each run commits `feed.json` to `main`. The dashboard reads the feed on open and applies each item once.

Feed ids: events `N-YYMMDD-nn`, changes `C-YYMMDD-nn`, forecasts `NF-YYMMDD-nn`, forecast updates `FU-YYMMDD-nn`. `seed_events` and `seed_forecasts` are a read-only index of the baseline ledger built into the page.
