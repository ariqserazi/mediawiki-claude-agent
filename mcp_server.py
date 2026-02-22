import os
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

BRIDGE_BASE = os.getenv("BRIDGE_BASE")

if not BRIDGE_BASE:
    raise ValueError("BRIDGE_BASE not set in environment")

mcp = FastMCP("mediawiki-bridge")


@mcp.tool()
async def resolve_wiki(topic: str) -> dict:
    """
    Resolve a topic name to its wiki base URL.
    Use this first to get the correct wiki URL before searching or fetching pages.
    - topic: if the user provided a wiki URL (e.g. 'https://my-wiki.fandom.com'), 
      pass it here directly. Otherwise pass the name of the show, game, or subject 
      (e.g. 'Ouran High School Host Club')
    Returns the base wiki URL to use in subsequent calls.
    """
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BRIDGE_BASE}/resolve",
            params={"topic": topic},
        )
        return r.json()


@mcp.tool()
async def search_wiki(query: str, wiki: str, limit: int = 5) -> dict:
    """
    Search for pages within a wiki.
    - query: search terms (e.g. 'Haruhi Fujioka gender')
    - wiki: base wiki URL from resolve_wiki (e.g. 'https://ouran.fandom.com')
    - limit: number of results to return, default 5, max 20
    Returns a list of matching page titles and their pageids.
    """
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BRIDGE_BASE}/search",
            params={
                "q": query,
                "wiki": wiki,
                "limit": limit,
            },
        )
        return r.json()


@mcp.tool()
async def get_page(title: str, wiki: str, chunk: int = 0, chunk_size: int = 8000) -> dict:
    """
    Retrieve the text content of a wiki page in chunks.
    - title: exact page title (e.g. 'Haruhi Fujioka')
    - wiki: base wiki URL (e.g. 'https://ouran.fandom.com')
    - chunk: chunk index starting at 0; increment to get subsequent chunks
    - chunk_size: characters per chunk, default 8000
    Always start at chunk=0. Check 'total_chunks' in the response to know how many chunks exist.
    Increment chunk and call again to retrieve the next portion of the page.
    """
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BRIDGE_BASE}/page",
            params={
                "title": title,
                "wiki": wiki,
                "mode": "chunk",
                "chunk": chunk,
                "chunk_size": chunk_size,
            },
        )
        return r.json()


if __name__ == "__main__":
    mcp.run()