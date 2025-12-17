# Steam-Offline-Client

Your steam games Downloader for mobile download offline non streaming gameplay

## Overview

Steam Offline Client is a command-line tool that helps you download and manage Steam games for offline use. Perfect for mobile gaming scenarios where streaming isn't available or when you want local access to your games.

## Features

- 📥 Download Steam games for offline use
- 📚 Manage your game library
- ⚙️ Configurable download paths
- 💾 Track downloaded games
- 🖥️ Simple command-line interface

## Quick Start

### Building the Application

```bash
# Install the application
pip install .

# Or run directly
python3 steam_offline_client.py --help
```

For detailed build instructions, see [BUILD.md](BUILD.md)

### Basic Usage

```bash
# Set download path
steam-offline-client --set-path ~/SteamGames

# Add a game
steam-offline-client --add-game 730 "Counter-Strike: Global Offensive"

# List games
steam-offline-client --list

# Download a game
steam-offline-client --download 730

# Check status
steam-offline-client --status
```

For complete usage documentation, see [USAGE.md](USAGE.md)

## Requirements

- Python 3.6 or higher
- pip (Python package installer)

## Documentation

- [BUILD.md](BUILD.md) - Detailed build and installation instructions
- [USAGE.md](USAGE.md) - Complete usage guide with examples
- [LICENSE](LICENSE) - License information

## License

See [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
