#!/bin/bash
# Start stringifybot

tmux new -ds stringifybot "python3 bot.py 2>&1 | tee log.txt"
