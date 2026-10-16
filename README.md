# Crock Math

Slow cooker honesty. The recipe says six hours on low, and the half-full pot was never going to wait that long. Crock Math does the oven-to-slow-cooker conversion, the fill band and the serving arithmetic, with every norm labeled.

## What it computes

- **The conversion truth** - every 30 minutes of oven simmering becomes about 2 hours on high or 4.5 on low (a labeled kitchen norm).
- **The fill truth** - load against cooker size, judged on the rounded fill fraction: under half full (runs hot and fast), the half-to-three-quarter band, past three-quarters (crowds the lid), or more than the cooker holds (a labeled kitchen norm).
- **The serving truth** - servings to cups and quarts of stew at 1.5 cups each (a labeled kitchen norm).

## Boundary

Illustrative arithmetic only. Every norm is a labeled kitchen norm; your cooker's own manual wins every tie. Crock Math never judges doneness or food safety - follow your recipe's guidance.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (18 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/crockmath/
Repo: https://github.com/iLanis-agent/crockmath
