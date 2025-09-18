import csv
import random
from typing import List

def generate_new_3_4_letter_domains(seed_words: List[str], count: int = 2000) -> List[str]:
    domains = set()

    # ساختارهای ترکیبی کوتاه
    structures = [
        lambda w1, w2: (w1 + w2)[:4],
        lambda w1, w2: w1[:3] if len(w1) >= 3 else (w1 + w2[0]),
        lambda w1, w2: (w1[:2] + w2[:2])[:4],
        lambda w1, w2: (w1[0] + w2[:2])[:3],
        lambda w1, w2: (w1[:2] + w2[0])[:3]
    ]

    max_attempts = count * 50
    attempts = 0

    while len(domains) < count and attempts < max_attempts:
        word1 = random.choice(seed_words)
        word2 = random.choice(seed_words)
        added = False

        for structure in structures:
            if len(domains) >= count:
                break
            domain = structure(word1, word2).lower()
            if 3 <= len(domain) <= 4 and domain.isalpha() and domain not in domains:
                domains.add(domain)
                added = True

        attempts += 1
        if not added:
            continue

    return list(domains)

def save_to_csv(domains: List[str], filename: str = "new_short_web_domains.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain Name'])
        for domain in domains:
            writer.writerow([domain])

# **لیست جدید از کلمات کوتاه**
new_seed_words = [
    "bit", "bot", "tag", "pix", "dev", "app", "web", "net", "ux", "ui",
    "lab", "hub", "box", "pro", "it", "job", "gig", "cod", "dat", "sys",
    "api", "mod", "dig", "tec", "fun", "run", "go", "set", "fix", "map"
]

# تولید 2000 دامنه جدید 3 تا 4 حرفی
new_domains = generate_new_3_4_letter_domains(new_seed_words, 2000)
save_to_csv(new_domains)

print(f"تولید {len(new_domains)} دامنه کوتاه جدید انجام شد.")
print("فایل 'new_short_web_domains.csv' ساخته شد.\n")
print("نمونه‌ها:")
for d in new_domains[:20]:
    print(d)
