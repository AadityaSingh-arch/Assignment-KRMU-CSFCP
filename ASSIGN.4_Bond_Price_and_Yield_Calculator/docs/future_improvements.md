Ideas for next steps:

1. Implement exact YTM via a numerical root finder (Newton–Raphson or bisection) instead of the approximation.

2. Support semi‑annual coupon payments (split coupon cash flows).

3. Pull real bond price and yield data via a market data API for live pricing (requires API key and internet access).

4. Add unit tests and CI (GitHub Actions) to run them on push.

5. Add a small web UI (Flask or static HTML) to make the tool accessible to non‑technical users
