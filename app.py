import logging
import os
import sys

import asyncio
import aiohttp

from zevercloud import ZeverCloud


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


try:
    API_KEY = os.environ["API_KEY"]
    APP_KEY = os.environ["APP_KEY"]
    APP_SECRET = os.environ["APP_SECRET"]
    HA_API_KEY = os.environ["HA_API_KEY"]
    HA_API_URL = os.environ["HA_API_URL"]
except KeyError:
    logger.exception("Make sure to set the required environment variables.")
    sys.exit(1)


async def main():
    zc = ZeverCloud(API_KEY, APP_KEY, APP_SECRET)
    async with aiohttp.ClientSession() as client:
        overview = zc.overview

        logger.info(f"Overview: {overview}")

        power_status = "on" if overview["online"] is True else "off"
        payload = {
            "state": overview["yield"]["today"],
            "attributes": {
                "unit_of_measurement": "kWh",
                "friendly_name": "Solar Yield Today",
                "power": f'{overview["power"]} kW',
                "power_status": power_status,
            },
        }
        headers = {
            "Authorization": f"Bearer {HA_API_KEY}",
            "Content-Type": "application/json",
        }
        resp = await client.post(
            f"{HA_API_URL}/states/sensor.zevercloud",
            json=payload,
            headers=headers
        )

        logger.info(f"HA API post status: {resp.status}")

        text = await resp.text()

        logger.info(f"HA API post resp text: {text}")

        resp.raise_for_status()
        await asyncio.sleep(60)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())