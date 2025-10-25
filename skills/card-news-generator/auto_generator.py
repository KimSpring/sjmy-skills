#!/usr/bin/env python3
"""
AI-Powered Auto Card News Generator
Creates multiple card news automatically from a topic using Claude API
"""

import argparse
import os
import sys
import json
from generate_card import create_card_news


def parse_card_content(content_text):
    """
    Parse the AI-generated content into individual cards
    Expected format:
    1. Title
    Description text
    
    2. Title
    Description text
    """
    cards = []
    current_card = None
    
    lines = content_text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_card and 'content' in current_card:
                cards.append(current_card)
                current_card = None
            continue
        
        # Check if line starts with a number
        if line[0].isdigit() and '. ' in line[:5]:
            # Save previous card
            if current_card and 'content' in current_card:
                cards.append(current_card)
            
            # Start new card
            parts = line.split('. ', 1)
            number = parts[0]
            title = parts[1] if len(parts) > 1 else ""
            
            current_card = {
                'number': int(number),
                'title': title,
                'content': ''
            }
        elif current_card is not None:
            # Add to content
            if current_card.get('content'):
                current_card['content'] += '\n' + line
            else:
                current_card['content'] = line
    
    # Add last card
    if current_card and 'content' in current_card:
        cards.append(current_card)
    
    return cards


def generate_cards_from_topic(topic, bg_color, text_color, output_dir, base_filename="card"):
    """
    Generate multiple cards from a topic
    
    This function expects Claude (the AI assistant) to have already generated
    the card content in the conversation context.
    """
    print(f"주제: {topic}")
    print(f"배경색: {bg_color}")
    print(f"텍스트색: {text_color}")
    print(f"출력 디렉토리: {output_dir}")
    print()
    print("=" * 60)
    print("Claude가 생성한 카드 내용을 입력하세요.")
    print("형식:")
    print("1. 제목")
    print("설명")
    print()
    print("2. 제목")
    print("설명")
    print()
    print("입력이 끝나면 Ctrl+D (Linux/Mac) 또는 Ctrl+Z (Windows)를 누르세요.")
    print("=" * 60)
    print()
    
    # Read all content from stdin
    content_text = sys.stdin.read()
    
    # Parse cards
    cards = parse_card_content(content_text)
    
    if not cards:
        print("❌ 카드 내용을 찾을 수 없습니다.")
        return []
    
    print(f"\n✓ {len(cards)}개의 카드를 찾았습니다.\n")
    
    # Generate images
    generated_files = []
    
    for card in cards:
        filename = f"{base_filename}_{card['number']:02d}.png"
        output_path = os.path.join(output_dir, filename)
        
        print(f"카드 {card['number']} 생성 중...")
        print(f"  제목: {card['title'][:30]}...")
        
        create_card_news(
            title=card['title'],
            content=card['content'],
            output_path=output_path,
            bg_color=bg_color,
            text_color=text_color,
            number=card['number']
        )
        
        generated_files.append(output_path)
        print(f"  ✓ 저장: {output_path}\n")
    
    return generated_files


def main():
    parser = argparse.ArgumentParser(
        description='Generate multiple card news from a topic using AI'
    )
    
    parser.add_argument('--topic', required=True, help='Main topic for the card series')
    parser.add_argument('--bg-color', default='#F5F3EE', help='Background color (hex)')
    parser.add_argument('--text-color', default='#1A1A1A', help='Text color (hex)')
    parser.add_argument('--output-dir', default='/mnt/user-data/outputs', help='Output directory')
    parser.add_argument('--base-filename', default='card', help='Base filename for cards')
    
    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Generate cards
    files = generate_cards_from_topic(
        topic=args.topic,
        bg_color=args.bg_color,
        text_color=args.text_color,
        output_dir=args.output_dir,
        base_filename=args.base_filename
    )
    
    if files:
        print("=" * 60)
        print(f"✅ 완료! {len(files)}개의 카드가 생성되었습니다.")
        print("=" * 60)
        for f in files:
            print(f"  📁 {f}")
    else:
        print("❌ 카드 생성 실패")
        sys.exit(1)


if __name__ == '__main__':
    main()
