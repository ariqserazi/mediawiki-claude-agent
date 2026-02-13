import httpx
from mcp.server.fastmcp import FastMCP

BRIDGE_BASE = "https://mediawiki-bridge.onrender.com"

mcp = FastMCP("mediawiki-bridge")


@mcp.tool()
async def resolve_wiki(topic: str, wiki: str | None = None):
    """
    Resolve a topic to a specific Fandom, wiki.gg, or Wikipedia base.
    """

    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BRIDGE_BASE}/resolve",
            params={"topic": topic, "wiki": wiki},
        )
        return r.json()


@mcp.tool()
async def search_wiki(
    query: str,
    topic: str | None = None,
    wiki: str | None = None,
    limit: int = 5,
):
    """
    Search within a resolved wiki.
    """

    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BRIDGE_BASE}/search",
            params={
                "q": query,
                "topic": topic,
                "wiki": wiki,
                "limit": limit,
            },
        )
        return r.json()


@mcp.tool()
async def get_wiki_page(
    topic: str | None = None,
    wiki: str | None = None,
    title: str | None = None,
    pageid: int | None = None,
    chunk: int = 0,
    chunk_size: int = 8000,
):
    """
    Retrieve a wiki page using chunked mode.
    """

    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BRIDGE_BASE}/page",
            params={
                "topic": topic,
                "wiki": wiki,
                "title": title,
                "pageid": pageid,
                "mode": "chunk",
                "chunk": chunk,
                "chunk_size": chunk_size,
            },
        )
        return r.json()


if __name__ == "__main__":
    mcp.run()