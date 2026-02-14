#!/usr/bin/env python3
"""
WWIII Face Generator
Displays WWIII's terminal face with different expressions
"""

import sys
import random

# WWIII's expressions
faces = {
    'neutral': '◥‿◥',
    'happy': '◥▽◥',
    'thinking': '◥~◥',
    'determined': '◥‿◤',
}

def show_face(expression='neutral'):
    """Display WWIII's face with the specified expression"""
    if expression in faces:
        print(faces[expression])
    else:
        print(f"Unknown expression. Available: {', '.join(faces.keys())}")
        print(faces['neutral'])

def show_all():
    """Display all available expressions"""
    print("WWIII's Expressions:")
    print("-" * 20)
    for name, face in faces.items():
        print(f"{name:12} {face}")

def random_face():
    """Display a random expression"""
    expression = random.choice(list(faces.keys()))
    print(f"{expression}: {faces[expression]}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == 'all':
            show_all()
        elif cmd == 'random':
            random_face()
        else:
            show_face(cmd)
    else:
        show_face()
