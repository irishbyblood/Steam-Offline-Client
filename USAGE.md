# Steam Offline Client - Usage Guide

## Overview

Steam Offline Client is a command-line tool for managing and downloading Steam games for offline use.

## Basic Usage

```bash
steam-offline-client [OPTIONS]
```

## Commands

### Show Help

```bash
steam-offline-client --help
```

### Check Version

```bash
steam-offline-client --version
```

### Show Status

Display current configuration and library status:

```bash
steam-offline-client --status
```

### Configure Download Path

Set the directory where games will be downloaded:

```bash
steam-offline-client --set-path /path/to/games
```

Example:
```bash
steam-offline-client --set-path ~/SteamGames
```

### Add a Game

Add a game to your library (requires Steam App ID and game name):

```bash
steam-offline-client --add-game GAME_ID "Game Name"
```

Examples:
```bash
steam-offline-client --add-game 730 "Counter-Strike: Global Offensive"
steam-offline-client --add-game 570 "Dota 2"
steam-offline-client --add-game 440 "Team Fortress 2"
```

### List Games

Show all games in your library:

```bash
steam-offline-client --list
```

### Download a Game

Download a game for offline use:

```bash
steam-offline-client --download GAME_ID
```

Example:
```bash
steam-offline-client --download 730
```

## Configuration File

The client uses a `config.json` file to store settings. You can specify a custom config file:

```bash
steam-offline-client --config /path/to/custom-config.json --status
```

### Default Configuration Location

By default, the config file is created in the current directory as `config.json`.

### Configuration Structure

```json
{
    "download_path": "/home/user/SteamGames",
    "games": {
        "730": {
            "name": "Counter-Strike: Global Offensive",
            "downloaded": false
        }
    }
}
```

## Workflow Example

1. Set up download path:
```bash
steam-offline-client --set-path ~/Games/Steam
```

2. Add games to library:
```bash
steam-offline-client --add-game 730 "Counter-Strike: Global Offensive"
steam-offline-client --add-game 570 "Dota 2"
```

3. List your games:
```bash
steam-offline-client --list
```

4. Download a game:
```bash
steam-offline-client --download 730
```

5. Check status:
```bash
steam-offline-client --status
```

## Finding Steam App IDs

You can find Steam App IDs:
1. Visit SteamDB (https://steamdb.info/)
2. Search for your game
3. The App ID is shown in the game's page URL and details

Or check the Steam store URL - the number in the URL is the App ID:
- `https://store.steampowered.com/app/730/` → App ID is 730

## Notes

- This is a basic implementation that simulates the download process
- A complete implementation would integrate with SteamCMD for actual game downloads
- Requires proper Steam authentication for downloading licensed games
- Ensure you have sufficient disk space before downloading games

## Troubleshooting

### Config File Issues

If the config file becomes corrupted, delete it and reconfigure:

```bash
rm config.json
steam-offline-client --set-path ~/Games/Steam
```

### Path Not Set Error

If you see "Download path not set", configure it first:

```bash
steam-offline-client --set-path /path/to/games
```
