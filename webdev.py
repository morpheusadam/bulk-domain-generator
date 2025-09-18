import csv
import random
from typing import List

def generate_web_domains(seed_words: List[str], count: int = 500) -> List[str]:
    """
    تولید نام دامنه‌های مرتبط با طراحی وبسایت، کدنویسی و فریلنسری
    """
    domains = set()
    
    structures = [
        lambda w1, w2: f"{w1}{w2}",
        lambda w1, w2: f"{w1}-{w2}",
        lambda w1, w2: f"{w1}{w2}pro",
        lambda w1, w2: f"{w1}{w2}dev",
        lambda w1, w2: f"{w1}{w2}lab",
        lambda w1, w2: f"{w1}{w2}hub",
        lambda w1, w2: f"{w1}{w2}code",
        lambda w1, w2: f"{w1}{w2}web",
        lambda w1, w2: f"my{w1}{w2}",
        lambda w1, w2: f"get{w1}{w2}",
    ]
    
    short_prefixes = ["web", "net", "dev", "code", "pro", "site", "app", "soft"]
    short_suffixes = ["hub", "lab", "box", "up", "it", "dev", "io"]
    
    tech_words = ["web", "site", "code", "dev", "app", "soft", "net", "ui", "ux", "cloud", "ai", "data", "it"]
    
    while len(domains) < count:
        word1 = random.choice(seed_words)
        word2 = random.choice(seed_words)
        
        if len(word1) > 6 or len(word2) > 6:
            continue
        
        for structure in structures:
            if len(domains) >= count:
                break
            domain = structure(word1, word2)
            if (3 <= len(domain) <= 12 and 
                domain.replace("-", "").isalpha() and 
                domain not in domains):
                domains.add(domain)
        
        if random.random() < 0.4:
            tech_word = random.choice(tech_words)
            short_word = random.choice([w for w in seed_words if len(w) <= 5])
            combos = [
                f"{tech_word}{short_word}",
                f"{short_word}{tech_word}",
                f"{random.choice(short_prefixes)}{tech_word}",
                f"{tech_word}{random.choice(short_suffixes)}",
                f"{random.choice(short_prefixes)}{short_word}",
                f"{short_word}{random.choice(short_suffixes)}",
            ]
            for combo in combos:
                if (4 <= len(combo) <= 12 and combo.isalpha() and combo not in domains):
                    domains.add(combo)
    
    return list(domains)[:count]

def save_to_csv(domains: List[str], filename: str = "web_domains.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain Name'])
        for domain in domains:
            writer.writerow([domain])

# کلمات پایه مرتبط با طراحی سایت و فریلنسری
seed_words = [
    "web", "site", "net", "dev", "code", "app", "soft", "ui", "ux", "design", "team", "pro", "work",
    "task", "job", "free", "lance", "gig", "project", "cloud", "data", "it"
]

premium_domains = generate_web_domains(seed_words, 500)
save_to_csv(premium_domains)

print(f"تولید {len(premium_domains)} دامنه مرتبط با طراحی وب و فریلنسری انجام شد.")
print("فایل 'web_domains.csv' ساخته شد.\n")
print("نمونه‌ها:")
for d in premium_domains[:20]:
    print(d)
