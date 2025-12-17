# Quick Start Guide

Get started with Steam Offline Client in just a few commands!

## Installation

### Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/irishbyblood/Steam-Offline-Client.git
cd Steam-Offline-Client

# Install
pip install .

# Verify installation
steam-offline-client --version
```

### Alternative: Run Without Installation

```bash
# Clone the repository
git clone https://github.com/irishbyblood/Steam-Offline-Client.git
cd Steam-Offline-Client

# Run directly
python3 steam_offline_client.py --help
```

## First Steps

### 1. Configure Download Path

```bash
steam-offline-client --set-path ~/SteamGames
```

### 2. Add Your First Game

```bash
steam-offline-client --add-game 730 "Counter-Strike: Global Offensive"
```

### 3. Check Your Library

```bash
steam-offline-client --list
```

### 4. Download a Game

```bash
steam-offline-client --download 730
```

### 5. Check Status

```bash
steam-offline-client --status
```

## Building from Source

### Build Distribution Packages

```bash
# Using Makefile
make build

# Or manually
pip install build
python -m build
```

This creates:
- `dist/steam_offline_client-1.0.0-py3-none-any.whl` - Wheel package
- `dist/steam_offline_client-1.0.0.tar.gz` - Source distribution

### Install from Built Package

```bash
pip install dist/steam_offline_client-1.0.0-py3-none-any.whl
```

## Common Commands

```bash
# Show all available options
steam-offline-client --help

# Show version
steam-offline-client --version

# Show current status and configuration
steam-offline-client --status

# Set download path
steam-offline-client --set-path /path/to/games

# Add a game
steam-offline-client --add-game <GAME_ID> "Game Name"

# List all games
steam-offline-client --list

# Download a game
steam-offline-client --download <GAME_ID>

# Use custom config file
steam-offline-client --config my-config.json --status
```

## Finding Steam App IDs

Visit [SteamDB](https://steamdb.info/) and search for your game, or check the Steam store URL:
- Example: `https://store.steampowered.com/app/730/` → App ID is `730`

## Popular Game IDs

- 730 - Counter-Strike: Global Offensive
- 570 - Dota 2
- 440 - Team Fortress 2
- 4000 - Garry's Mod
- 271590 - Grand Theft Auto V

## Need Help?

- Full documentation: [USAGE.md](USAGE.md)
- Build instructions: [BUILD.md](BUILD.md)
- Report issues: [GitHub Issues](https://github.com/irishbyblood/Steam-Offline-Client/issues)

## Development

```bash
# Install in development mode
make install-dev
# Or: pip install -e .

# Make changes to the code
# Changes will take effect immediately without reinstalling
```

## Uninstall

```bash
pip uninstall steam-offline-client
```
