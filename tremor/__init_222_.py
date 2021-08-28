import asyncio
from concurrent.futures import ThreadPoolExecutor

from tremor.oauth import TwitchOauth2

# Revoke: https://id.twitch.tv/oauth2/revoke
# https://id.twitch.tv/oauth2/token


# clientId = id7s6oq6izzwlwu9y958eji7sw8uuu
# clientSecret = j586lrl10hktsc0j0sm9pig0hz39ma


async def ainput(prompt: str = ""):
    with ThreadPoolExecutor(1, "ainput") as executor:
        return (
            await asyncio.get_event_loop().run_in_executor(
                executor, input, prompt
            )
        ).rstrip()


async def myCoroutine():
    client = TwitchOauth2(
        "id7s6oq6izzwlwu9y958eji7sw8uuu", "j586lrl10hktsc0j0sm9pig0hz39ma"
    )
    x = await client.get_authorization_url(
        "http://localhost:8085/", scope=["chat:read"]
    )
    print(f"Result {x}")
    code = await ainput("Redirect code:")
    y = await client.get_access_token(code, "http://localhost:8085/")
    print(f"Result {y}")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myCoroutine())
    loop.close()


if __name__ == "__main__":
    main()
