import csv
import random
from typing import List

def generate_short_meaningful_domains(seed_words: List[str], count: int = 500) -> List[str]:
    """
    تولید دامنه‌های کوتاه (حدود 5 حرف) و معنی‌دار مرتبط با طراحی وب و فریلنسری
    """
    domains = set()

    # ترکیب‌های پیشنهادی برای دامنه کوتاه
    structures = [
        lambda w1, w2: f"{w1}{w2}"[:5],
        lambda w1, w2: f"{w1}{w2[0]}"[:5],
        lambda w1, w2: f"{w1[0]}{w2}{w2[1]}"[:5],
        lambda w1, w2: f"{w1[:2]}{w2[:3]}"[:5],
        lambda w1, w2: f"{w1[:3]}{w2[:2]}"[:5],
    ]

    while len(domains) < count:
        word1 = random.choice(seed_words)
        word2 = random.choice(seed_words)

        # سعی می‌کنیم ترکیبات کوتاه حدود 5 حرف داشته باشند
        for structure in structures:
            if len(domains) >= count:
                break
            domain = structure(word1, word2)
            if (3 <= len(domain) <= 5 and domain.isalpha() and domain not in domains):
                domains.add(domain.lower())

    return list(domains)[:count]

def save_to_csv(domains: List[str], filename: str = "short_web_domains.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain Name'])
        for domain in domains:
            writer.writerow([domain])

# کلمات کوتاه و معنی‌دار مرتبط با طراحی وب و فریلنسری
seed_words = [
    "web", "site", "dev", "code", "app", "ui", "ux", "pro", "job", "task",
    "gig", "team", "it", "lab", "net", "data", "cloud", "design"
]

# تولید 500 دامنه کوتاه و معنی‌دار
short_domains = generate_short_meaningful_domains(seed_words, 500)
save_to_csv(short_domains)

print(f"تولید {len(short_domains)} دامنه کوتاه و معنی‌دار انجام شد.")
print("فایل 'short_web_domains.csv' ساخته شد.\n")
print("نمونه‌ها:")
for d in short_domains[:20]:
    print(d)
