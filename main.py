import alien_invasion
import asyncio


# Run Alien Invasion Gradius-like game.
async def main():
    mygame = alien_invasion.AlienInvasion()
    mygame.run_game()
    await asyncio.sleep(0)

asyncio.run(main())
