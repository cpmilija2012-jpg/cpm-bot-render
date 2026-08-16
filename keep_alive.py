"""
Dodaj ovo u cpm_bot.py da bot ne "zaspije" na Render free tieru.

KORAK:
1. Spremi ovaj fajl kao keep_alive.py u isti folder
2. Na kraju cpm_bot.py (prije if __name__ == "__main__":), dodaj:

   from keep_alive import start_keep_alive
   start_keep_alive()

3. Na Renderu ćeš dobiti URL npr. https://cpm-bot.onrender.com
4. Registruj se na https://uptimerobot.com i postavi ping svakih 5 minuta na taj URL
"""
import asyncio
from aiohttp import web

async def health(request):
    return web.Response(text="CPM Bot OK")

async def start_server():
    app = web.Application()
    app.router.add_get("/", health)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render postavi PORT env var automatski
    import os
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Keep-alive server running on port {port}")

def start_keep_alive():
    loop = asyncio.get_event_loop()
    loop.create_task(start_server())
