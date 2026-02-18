# MediaWiki Claude Desktop MCP Tool

## Overview

This project connects **Claude Desktop** to a deployed **MediaWiki
Bridge API** using MCP (Model Context Protocol).

It allows Claude Desktop to:

-   Resolve fandom/wiki topics
-   Search wiki pages
-   Retrieve structured, chunked wiki content
-   Use external canonical knowledge directly inside Claude
    conversations

Claude Desktop cannot call REST APIs directly.\
This MCP server acts as a local adapter that connects Claude Desktop to
your deployed MediaWiki Bridge.

------------------------------------------------------------------------

## Architecture

Claude Desktop\
↓\
Local MCP Server (this project)\
↓\
MediaWiki Bridge (Render deployment)\
↓\
Fandom / wiki.gg / Wikipedia APIs

------------------------------------------------------------------------

## Requirements

-   Python 3.9+
-   Claude Desktop
-   MediaWiki Bridge deployed
    

------------------------------------------------------------------------

# Installation

## 1. Clone the Repository

    git clone https://github.com/YOUR_USERNAME/mediawiki-claude-agent.git
    cd mediawiki-claude-agent

------------------------------------------------------------------------

## 2. Create Virtual Environment

### macOS / Linux

    python3 -m venv venv
    source venv/bin/activate

### Windows

    python -m venv venv
    venv\Scripts\activate

------------------------------------------------------------------------

## 3. Install Dependencies

    pip install -r requirements.txt

This installs:

-   mcp
-   httpx
-   python-dotenv

------------------------------------------------------------------------

# Environment Configuration (.env)

This project uses environment variables to configure the MediaWiki
Bridge URL.

Inside the project root (same folder as `mcp_server.py`), create a file
named:

    .env

Add:

    BRIDGE_BASE=https://Your_Media_render_link.com

Do NOT use quotes.\
Do NOT add spaces around `=`.

If you deploy staging, production, or local bridge versions, simply
change this value without modifying code.

------------------------------------------------------------------------

# Connecting to Claude Desktop

Claude Desktop uses MCP servers defined in a configuration file.\
The location depends on your operating system.

------------------------------------------------------------------------

## macOS Setup

### 1. Create Config File

    touch ~/Library/Application\ Support/Claude/claude_desktop_config.json

Open it:

    open ~/Library/Application\ Support/Claude/claude_desktop_config.json

### 2. Add Configuration

Replace paths with your actual absolute paths:

``` json
{
  "mcpServers": {
    "mediawiki": {
      "command": "/Users/YOUR_USERNAME/path/to/project/venv/bin/python",
      "args": [
        "/Users/YOUR_USERNAME/path/to/project/mcp_server.py"
      ]
    }
  }
}
```

Important:

-   Use absolute paths
-   Do NOT use `~`
-   Do NOT use relative paths

Restart Claude Desktop after saving.

------------------------------------------------------------------------

## Windows Setup

### 1. Navigate to Claude Config Folder

    C:\Users\YOUR_USERNAME\AppData\Roaming\Claude\

Create:

    claude_desktop_config.json

### 2. Add Configuration

Use full Windows paths:

``` json
{
  "mcpServers": {
    "mediawiki": {
      "command": "C:\\Users\\YOUR_USERNAME\\path\\to\\project\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\YOUR_USERNAME\\path\\to\\project\\mcp_server.py"
      ]
    }
  }
}
```

Important:

-   Use double backslashes
-   Use full absolute paths
-   Do NOT use relative paths

Restart Claude Desktop.

------------------------------------------------------------------------

# Available Tools

Claude Desktop will now have access to:

-   resolve_wiki
-   search_wiki
-   get_wiki_page

------------------------------------------------------------------------

# Example Prompts

Inside Claude Desktop:

    Resolve Ouran High School Host Club and search for Haruhi Fujioka.

or

    Use the wiki tool to retrieve the Haruhi Fujioka page and analyze contradictions.

Claude will:

1.  Call the MCP tool
2.  Fetch data from your deployed MediaWiki Bridge
3.  Continue reasoning using structured external data

------------------------------------------------------------------------

# Project Structure

    agent/
    ├── venv/
    ├── mcp_server.py
    ├── requirements.txt
    ├── main.py
    ├── .env
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

# .gitignore

Ensure your `.gitignore` includes:

    venv/
    .env
    __pycache__/
    .DS_Store

------------------------------------------------------------------------

# Troubleshooting

If Claude says the tool failed to start:

-   Check Python path in config
-   Ensure venv is installed and dependencies installed
-   Ensure `.env` exists with `BRIDGE_BASE`
-   Test manually:

```{=html}
<!-- -->
```
    source venv/bin/activate
    python mcp_server.py

If it runs silently, it is working.

------------------------------------------------------------------------

# Summary

This project enables Claude Desktop to use external MediaWiki knowledge
via:

MCP → HTTP → MediaWiki Bridge → Canonical Wiki APIs

The MediaWiki Bridge URL is configured via `.env`, allowing flexible
environment switching without code changes.
----------------------------------------------------------------------------------
# MediaWiki Claude Desktop MCP Tool --- Windows Setup Guide

This guide explains how to correctly connect your MediaWiki MCP server
to Claude Desktop on Windows.

------------------------------------------------------------------------

## Important Note

Claude Desktop on Windows MSIX installs uses a sandboxed configuration
folder.\
The correct config path is:

C:`\Users`{=tex}`\YOUR`{=tex}\_USERNAME`\AppData`{=tex}`\Local`{=tex}`\Packages`{=tex}`\Claude`{=tex}\_pzs8sxrjxfjjc`\LocalCache`{=tex}`\Roaming`{=tex}`\Claude`{=tex}\

NOT:

C:`\Users`{=tex}`\YOUR`{=tex}\_USERNAME`\AppData`{=tex}`\Roaming`{=tex}`\Claude`{=tex}\

------------------------------------------------------------------------

## Step 1 --- Navigate to Claude Config Folder

Open File Explorer and paste:

%LOCALAPPDATA%`\Packages`{=tex}`\Claude`{=tex}\_pzs8sxrjxfjjc`\LocalCache`{=tex}`\Roaming`{=tex}`\Claude`{=tex}

Create a file named:

claude_desktop_config.json

------------------------------------------------------------------------

## Step 2 --- Add MCP Configuration

Paste this configuration and replace YOUR_USERNAME with your Windows
username:

``` json
{
  "mcpServers": {
    "mediawiki": {
      "command": "C:\\Users\\YOUR_USERNAME\\Tools\\mediawiki-claude-agent\\venv\\Scripts\\python.exe",
      "args": [
        "-u",
        "C:\\Users\\YOUR_USERNAME\\Tools\\mediawiki-claude-agent\\mcp_server.py"
      ]
    }
  }
}
```

Important:

-   Use full absolute paths
-   Use double backslashes
-   Do NOT use relative paths
-   Include "-u" for unbuffered stdio

------------------------------------------------------------------------

## Step 3 --- Create .env File

In your project folder:

C:`\Users`{=tex}`\YOUR`{=tex}\_USERNAME`\Tools`{=tex}`\mediawiki`{=tex}-claude-agent\

Create:

.env

Add:

BRIDGE_BASE=https://your-render-url.onrender.com

------------------------------------------------------------------------

## Step 4 --- Install Dependencies

Open Command Prompt:

cd
C:`\Users`{=tex}`\YOUR`{=tex}\_USERNAME`\Tools`{=tex}`\mediawiki`{=tex}-claude-agent

venv`\Scripts`{=tex}`\activate`{=tex}

pip install -r requirements.txt

------------------------------------------------------------------------

## Step 5 --- Test MCP Server

Run:

venv`\Scripts`{=tex}`\python`{=tex}.exe mcp_server.py

Expected result:

-   No output
-   Process stays running

Press Ctrl+C to stop.

------------------------------------------------------------------------

## Step 6 --- Restart Claude Desktop

Close Claude Desktop fully.

Open Task Manager.

End all Claude processes.

Restart Claude Desktop.

------------------------------------------------------------------------

## Step 7 --- Verify Connection

Open:

Settings → Developer

You should see:

mediawiki --- Connected

------------------------------------------------------------------------

## Step 8 --- Test Tool

Example prompt:

Resolve Haruhi Fujioka using the mediawiki tool.

Claude will retrieve data using your MediaWiki Bridge.

------------------------------------------------------------------------

## Project Structure

C:`\Users`{=tex}`\YOUR`{=tex}\_USERNAME`\Tools`{=tex}`\mediawiki`{=tex}-claude-agent\

├── venv  ├── mcp_server.py\
├── requirements.txt\
├── .env

Claude config lives separately in:

AppData`\Local`{=tex}`\Packages`{=tex}`\Claude`{=tex}\_pzs8sxrjxfjjc`\LocalCache`{=tex}`\Roaming`{=tex}`\Claude`{=tex}\

------------------------------------------------------------------------

## Summary

Your MCP server connects:

Claude Desktop → MCP Server → MediaWiki Bridge → Wiki APIs
