#!/usr/bin/env python3
"""
Простой демо-скрипт, созданный Grok
"""

def greet(name: str = "мир") -> str:
    return f"Привет, {name}! 👋"

def main():
    print(greet("Anisa"))
    print("Этот проект был создан автоматически через Grok + GitHub.")
    print("Репозиторий: https://github.com/Anisa8998/hello-grok")

if __name__ == "__main__":
    main()
