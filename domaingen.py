import csv
import random
from typing import List

def generate_high_quality_domains(seed_words: List[str], count: int = 500) -> List[str]:
    """
    تولید نام دامنه های با کیفیت بالا با رعایت اصول نامگذاری موثر
    """
    domains = set()
    
    # ساختارهای بهینه شده برای دامنه‌های کوتاه و موثر
    structures = [
        # ساختارهای ساده و کوتاه (2-3 بخشی)
        lambda w1, w2: f"{w1}{w2}",
        lambda w1, w2: f"{w1}{w2}",
        
        # ساختارهای با پیشوند/پسوند حرفه‌ای
        lambda w1, w2: f"{w1}ly",
        lambda w1, w2: f"{w1}fy",
        lambda w1, w2: f"{w1}io",
        lambda w1, w2: f"{w1}app",
        lambda w1, w2: f"{w1}pro",
        lambda w1, w2: f"get{w1}",
        lambda w1, w2: f"try{w1}",
        lambda w1, w2: f"my{w1}",
    ]
    
    # کلمات بسیار کوتاه برای ترکیبات بهینه
    short_prefixes = ["web", "net", "dig", "app", "pro", "max", "top", "new", "smart", "easy"]
    short_suffixes = ["ly", "fy", "io", "ex", "ax", "ox", "up", "pro", "hub", "lab"]
    
    # کلمات کلیدی مرتبط با فناوری
    tech_words = ["tech", "cloud", "data", "ai", "code", "dev", "soft", "cyber", "net", "web"]
    
    while len(domains) < count:
        # انتخاب دو کلمه کوتاه برای ترکیب
        word1 = random.choice(seed_words)
        word2 = random.choice(seed_words)
        
        # اطمینان از کوتاه بودن کلمات انتخابی
        if len(word1) > 4 or len(word2) > 4:
            continue
            
        # استفاده از ساختارهای اصلی
        for structure in structures:
            if len(domains) >= count:
                break
            
            domain = structure(word1, word2)
            
            # فیلترهای سختگیرانه برای کیفیت
            if (3 <= len(domain) <= 8 and  # بسیار کوتاه
                domain.isalpha() and        # فقط حروف
                not any(c in domain for c in 'aeiou') and  # حروف صدادار کم
                len(set(domain)) >= 3 and   # تنوع حروف
                domain not in domains):
                
                domains.add(domain)
        
        # ترکیبات ویژه با کلمات فناوری
        if random.random() < 0.2:
            tech_word = random.choice(tech_words)
            short_word = random.choice([w for w in seed_words if len(w) <= 3])
            
            combinations = [
                f"{tech_word}{short_word}",
                f"{short_word}{tech_word}",
                f"{random.choice(short_prefixes)}{tech_word}",
                f"{tech_word}{random.choice(short_suffixes)}",
            ]
            
            for combo in combinations:
                if (4 <= len(combo) <= 8 and 
                    combo.isalpha() and 
                    combo not in domains):
                    domains.add(combo)
    
    # مرتب‌سازی بر اساس طول (کوتاه‌ترین اول)
    sorted_domains = sorted(list(domains), key=len)
    return sorted_domains[:count]

def save_to_csv(domains: List[str], filename: str = "premium_domains.csv"):
    """
    ذخیره نام دامنه ها در فایل CSV
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain Name', 'Length', 'Type'])
        for domain in domains:
            writer.writerow([domain, len(domain), 'Premium'])

# لیست کلمات بسیار کوتاه و موثر فارسی
short_persian_words = [
    # کلمات بسیار کوتاه (2-4 حرفی)
    'ara', 'saz', 'kar', 'fan', 'ray', 'ban', 'sab', 'meh',
    'rav', 'kav', 'por', 'tiz', 'ram', 'min', 'lav', 'pou',
    'gol', 'mor', 'dar', 'kuh', 'sta', 'mah', 'bad', 'nar',
    'yal', 'yas', 'sib', 'ran', 'neg', 'baz', 'for', 'kha',
    'tej', 'san', 'ser', 'mar', 'mod', 'web', 'net', 'dig',
    'app', 'pro', 'max', 'top', 'new', 'get', 'try', 'my'
]

# تولید 500 نام دامنه با کیفیت بالا
premium_domains = generate_high_quality_domains(short_persian_words, 500)

# ذخیره در فایل CSV
save_to_csv(premium_domains)

print(f"تولید {len(premium_domains)} نام دامنه پریمیوم با موفقیت انجام شد!")
print("فایل 'premium_domains.csv' ایجاد شد.")

# نمایش نمونه‌ای از بهترین دامنه‌ها
print("\nنمونه‌هایی از بهترین دامنه‌های تولید شده:")
for i, domain in enumerate(premium_domains[:20]):
    print(f"{i+1}. {domain}.com (طول: {len(domain)})")