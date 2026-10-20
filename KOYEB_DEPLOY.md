# Deploy on Koyeb (bot + ad verification website in ONE service)

The bot and the verification website run in the same app: the website is served on
Koyeb's port, the bot runs alongside it.

## 1. Put the code on GitHub
Upload this folder to a **private** GitHub repo.

## 2. Create the service on Koyeb
1. Koyeb dashboard -> **Create Service** -> **Web Service** -> **GitHub** -> pick your repo.
2. **Builder:** choose **Dockerfile** (the repo already has one).
3. **Instance:** see the note about the free instance below.
4. **Ports / Exposed ports:** `8080`, protocol **HTTP**, route path `/`.
5. **Health check:** HTTP, path `/health`, port `8080`.
6. Add the **Environment variables** below, then **Deploy**.

## 3. Environment variables

| Name | Value |
|---|---|
| `TG_BOT_TOKEN` | bot token from @BotFather |
| `APP_ID` | from my.telegram.org |
| `API_HASH` | from my.telegram.org |
| `CHANNEL_ID` | your DB channel id (-100...) |
| `OWNER_ID` | your Telegram user id |
| `ADMINS` | admin ids separated by spaces |
| `DATABASE_URL` | MongoDB url |
| `DATABASE_NAME` | e.g. `Emilia` |
| `FORCESUB_CHANNEL` / `FORCESUB_CHANNEL2` | channel ids, or `0` to disable |
| `PORT` | `8080` |
| `MONETAG_ZONE` | zone id, e.g. `10396377` (the `data-zone` value) |
| `MONETAG_SDK` | SDK function, e.g. `show_10396377` (the `data-sdk` value) |
| `MONETAG_SDK_URL` | optional, script link (default `//libtl.com/sdk.js`) |
| `MONETAG_SCRIPT` | optional shortcut: paste the whole `<script ...>` tag here instead of the 3 above |
| `WEBAPP_URL` | optional - leave empty, it is taken from Koyeb automatically. If you add a custom domain, put `https://yourdomain.com` |

## 4. Check it works
- Open `https://<your-app>.koyeb.app/health` -> should show `{"status": "ok"}`
- Open `https://<your-app>.koyeb.app/verify` -> shows the verification page
- Koyeb logs should show: `Ad verification ON -> https://<your-app>.koyeb.app/verify`
- Open a file link of your bot from a non-admin account -> you get **Verify Now**.

## 5. Monetag
In Monetag, add your Telegram Mini App and use `https://<your-app>.koyeb.app/verify`
as the app URL. Copy the zone id into `MONETAG_ZONE`.

## ⚠️ Free instance note
Koyeb's free instance goes to sleep after 1 hour without website visits. Telegram
messages do NOT count as visits, so a sleeping bot stops answering until someone opens
the website. Use a paid instance type (e.g. Eco nano) to keep the bot always online.
