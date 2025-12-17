#!/usr/bin/env python3
"""
Steam Offline Client - A tool for downloading Steam games for offline use
"""

import argparse
import json
import os
import sys
from pathlib import Path


class SteamOfflineClient:
    """Main Steam Offline Client class"""
    
    def __init__(self, config_file="config.json"):
        """Initialize the Steam Offline Client
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = self.load_config()
        
    def load_config(self):
        """Load configuration from file
        
        Returns:
            dict: Configuration dictionary
        """
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {self.config_file}")
                return {}
        return {}
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def set_download_path(self, path):
        """Set the download path for games
        
        Args:
            path: Path where games will be downloaded
        """
        download_path = Path(path).resolve()
        download_path.mkdir(parents=True, exist_ok=True)
        self.config['download_path'] = str(download_path)
        self.save_config()
        print(f"Download path set to: {download_path}")
    
    def list_games(self):
        """List available games in the library"""
        print("Available games in library:")
        if 'games' in self.config and self.config['games']:
            for game_id, game_info in self.config['games'].items():
                print(f"  [{game_id}] {game_info.get('name', 'Unknown')}")
        else:
            print("  No games configured yet.")
    
    def add_game(self, game_id, game_name):
        """Add a game to the library
        
        Args:
            game_id: Steam game ID
            game_name: Name of the game
        """
        if 'games' not in self.config:
            self.config['games'] = {}
        
        self.config['games'][game_id] = {
            'name': game_name,
            'downloaded': False
        }
        self.save_config()
        print(f"Added game: {game_name} (ID: {game_id})")
    
    def download_game(self, game_id):
        """Download a game for offline use
        
        Args:
            game_id: Steam game ID to download
        """
        if 'download_path' not in self.config:
            print("Error: Download path not set. Use --set-path to configure.")
            return False
        
        if 'games' not in self.config or game_id not in self.config['games']:
            print(f"Error: Game ID {game_id} not found in library.")
            return False
        
        game_info = self.config['games'][game_id]
        print(f"Downloading {game_info['name']} (ID: {game_id})...")
        print(f"To: {self.config['download_path']}")
        
        # In a real implementation, this would use Steam API/SteamCMD
        # For now, we'll simulate the download
        print("Note: This is a simulation. Real implementation would use SteamCMD.")
        
        game_info['downloaded'] = True
        self.save_config()
        print(f"Successfully downloaded {game_info['name']}")
        return True
    
    def show_status(self):
        """Show current client status and configuration"""
        print("=== Steam Offline Client Status ===")
        print(f"Config file: {self.config_file}")
        print(f"Download path: {self.config.get('download_path', 'Not set')}")
        
        if 'games' in self.config:
            total_games = len(self.config['games'])
            downloaded_games = sum(1 for g in self.config['games'].values() if g.get('downloaded', False))
            print(f"Total games: {total_games}")
            print(f"Downloaded games: {downloaded_games}")
        else:
            print("Total games: 0")


def main():
    """Main entry point for the Steam Offline Client"""
    parser = argparse.ArgumentParser(
        description='Steam Offline Client - Download Steam games for offline use',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--config', default='config.json',
                       help='Configuration file path (default: config.json)')
    parser.add_argument('--set-path', metavar='PATH',
                       help='Set download path for games')
    parser.add_argument('--add-game', nargs=2, metavar=('ID', 'NAME'),
                       help='Add a game to library (requires game ID and name)')
    parser.add_argument('--download', metavar='GAME_ID',
                       help='Download a game by ID')
    parser.add_argument('--list', action='store_true',
                       help='List all games in library')
    parser.add_argument('--status', action='store_true',
                       help='Show client status')
    parser.add_argument('--version', action='version', version='Steam Offline Client 1.0.0')
    
    args = parser.parse_args()
    
    # Create client instance
    client = SteamOfflineClient(config_file=args.config)
    
    # Execute commands
    if args.set_path:
        client.set_download_path(args.set_path)
    elif args.add_game:
        client.add_game(args.add_game[0], args.add_game[1])
    elif args.download:
        client.download_game(args.download)
    elif args.list:
        client.list_games()
    elif args.status:
        client.show_status()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
