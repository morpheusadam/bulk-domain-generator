import csv
import random
from typing import List

def generate_premium_domains(seed_words: List[str], count: int = 500) -> List[str]:
    """
    تولید نام دامنه های پریمیوم برای حوزه طراحی وب و توسعه
    """
    domains = set()
    
    # کلمات کلیدی پریمیوم برای حوزه وب و فناوری
    premium_keywords = [
        "web", "dev", "code", "design", "studio", "tech", "digital", "creative", 
        "pixel", "byte", "bit", "cloud", "host", "server", "api", "app", "ai", 
        "ml", "data", "smart", "fast", "clean", "pure", "sharp", "bright", "true",
        "core", "base", "meta", "neo", "ultra", "max", "pro", "prime", "elite",
        "vip", "gold", "silver", "platinum", "alpha", "beta", "gamma", "omega",
        "zen", "nova", "quantum", "flux", "wave", "sync", "flow", "grid", "stack"
    ]
    
    # پسوندهای حرفه‌ای و مدرن
    premium_suffixes = [
        "dev", "pro", "tech", "io", "ly", "fy", "hq", "lab", "hub", "studio", 
        "agency", "team", "works", "co", "xyz", "app", "cloud", "tools", "grid",
        "flow", "ai", "ml", "api", "net", "sys", "box", "zen", "nova", "wave",
        "flux", "sync", "art", "craft", "maker", "build", "create", "forge",
        "smith", "workshop", "factory", "center", "point", "spot", "base"
    ]
    
    # پیشوندهای حرفه‌ای
    premium_prefixes = [
        "web", "dev", "code", "design", "pixel", "byte", "bit", "smart", "fast",
        "clean", "pure", "sharp", "bright", "true", "core", "base", "meta", "neo",
        "ultra", "max", "pro", "prime", "elite", "vip", "alpha", "beta", "gamma",
        "zen", "nova", "quantum", "flux", "wave", "sync", "flow", "grid", "stack"
    ]
    
    # فعل‌ها و اصطلاحات خلاقانه
    action_words = [
        "build", "create", "make", "craft", "design", "develop", "code", "program",
        "launch", "start", "begin", "init", "generate", "produce", "form", "shape",
        "mold", "forge", "weld", "connect", "link", "join", "merge", "fusion",
        "mix", "blend", "combine", "unite", "sync", "match", "fit", "suit"
    ]
    
    # ساختارهای ترکیبی خلاقانه
    creative_structures = [
        # ترکیب ساده
        lambda w1, w2: f"{w1}{w2}",
        lambda w1, w2: f"{w2}{w1}",
        
        # ترکیب با کلمات کلیدی
        lambda w1, w2: f"{w1}{random.choice(premium_keywords)}",
        lambda w1, w2: f"{random.choice(premium_keywords)}{w1}",
        lambda w1, w2: f"{w1}{random.choice(action_words)}",
        lambda w1, w2: f"{random.choice(action_words)}{w1}",
        
        # ترکیب با پیشوند/پسوند
        lambda w1, w2: f"{w1}{random.choice(premium_suffixes)}",
        lambda w1, w2: f"{random.choice(premium_prefixes)}{w1}",
        lambda w1, w2: f"{random.choice(premium_prefixes)}{w2}",
        lambda w1, w2: f"{w1}{random.choice(premium_suffixes)}",
        
        # ساختارهای سه بخشی
        lambda w1, w2: f"{random.choice(premium_prefixes)}{w1}{random.choice(premium_suffixes)}",
        lambda w1, w2: f"{w1}{w2}{random.choice(premium_suffixes)}",
        lambda w1, w2: f"{random.choice(premium_prefixes)}{w1}{w2}",
        
        # ساختارهای خلاقانه
        lambda w1, w2: f"{w1}ly",
        lambda w1, w2: f"{w1}ify",
        lambda w1, w2: f"{w1}io",
        lambda w1, w2: f"{w1}ex",
        lambda w1, w2: f"{w1}ax",
        lambda w1, w2: f"{w1}up",
        lambda w1, w2: f"get{w1}",
        lambda w1, w2: f"try{w1}",
        lambda w1, w2: f"my{w1}",
        lambda w1, w2: f"the{w1}",
        lambda w1, w2: f"{w1}pro",
        lambda w1, w2: f"{w1}hub",
        lambda w1, w2: f"{w1}lab",
    ]
    
    # لیست گسترده‌تر از کلمات فارسی و بین‌المللی
    extended_words = seed_words + [
        # کلمات فارسی اضافی
        'rang', 'nagh', 'gol', 'set', 'noj', 'kho', 'zib', 'lat', 'naz', 'shir',
        'far', 'meh', 'abr', 'aft', 'shab', 'roo', 'soo', 'dor', 'chesh', 'del',
        'jan', 'rokh', 'gosh', 'dast', 'pa', 'sar', 'tan', 'joon', 'gham', 'shad',
        'khosh', 'bakht', 'naseeb', 'ghadar', 'vaght', 'saat', 'rooz', 'shab',
        'mah', 'sal', 'fasl', 'bahar', 'tabestan', 'paeez', 'zemestan', 'ab',
        'bad', 'hava', 'akas', 'ati', 'asem', 'zamin', 'khak', 'sang', 'ahan',
        
        # کلمات بین‌المللی
        'arc', 'apex', 'zen', 'nova', 'flux', 'wave', 'sync', 'flow', 'grid',
        'stack', 'node', 'link', 'mesh', 'net', 'web', 'cloud', 'data', 'ai',
        'ml', 'code', 'dev', 'pro', 'max', 'ultra', 'meta', 'neo', 'vortex',
        'pulse', 'rhythm', 'harmony', 'echo', 'aura', 'vibe', 'spark', 'flare',
        'glow', 'shine', 'beam', 'ray', 'light', 'dark', 'shadow', 'mirror',
        'crystal', 'gem', 'gold', 'silver', 'platinum', 'diamond', 'pearl'
    ]
    
    max_attempts = count * 10
    attempts = 0
    
    while len(domains) < count and attempts < max_attempts:
        attempts += 1
        
        # انتخاب دو کلمه تصادفی
        word1 = random.choice(extended_words)
        word2 = random.choice(extended_words)
        
        # استفاده از ساختارهای خلاقانه
        for structure in creative_structures:
            if len(domains) >= count:
                break
            
            try:
                domain = structure(word1, word2).lower()
                
                # فیلترهای سختگیرانه برای کیفیت
                if (3 <= len(domain) <= 15 and
                    domain.isalpha() and
                    len(set(domain)) >= 3 and
                    not any(domain.endswith(x) for x in ['aa', 'ee', 'ii', 'oo', 'uu']) and
                    not any(domain.startswith(x) for x in ['xx', 'zz', 'qq']) and
                    domain not in domains):
                    
                    domains.add(domain)
                    
            except:
                continue
        
        # ترکیبات ویژه با کلمات کلیدی
        if random.random() < 0.5 and len(domains) < count:
            try:
                keyword = random.choice(premium_keywords)
                action = random.choice(action_words)
                persian_word = random.choice([w for w in extended_words if len(w) <= 5])
                
                special_combinations = [
                    f"{keyword}{persian_word}",
                    f"{persian_word}{keyword}",
                    f"{action}{persian_word}",
                    f"{persian_word}{action}",
                    f"{random.choice(premium_prefixes)}{keyword}",
                    f"{keyword}{random.choice(premium_suffixes)}",
                    f"{action}{random.choice(premium_suffixes)}",
                    f"{random.choice(premium_prefixes)}{action}",
                    f"{persian_word}dev",
                    f"{persian_word}design",
                    f"{persian_word}studio",
                    f"{persian_word}tech",
                    f"dev{persian_word}",
                    f"code{persian_word}",
                    f"web{persian_word}",
                    f"pixel{persian_word}",
                    f"byte{persian_word}",
                    f"bit{persian_word}",
                    f"cloud{persian_word}",
                    f"ai{persian_word}",
                    f"ml{persian_word}",
                ]
                
                for combo in special_combinations:
                    if len(domains) >= count:
                        break
                    combo = combo.lower()
                    if (4 <= len(combo) <= 15 and 
                        combo.isalpha() and 
                        combo not in domains):
                        domains.add(combo)
                        
            except:
                continue
    
    return sorted(list(domains), key=len)[:count]

def save_to_csv(domains: List[str], filename: str = "premium_web_domains.csv"):
    """
    ذخیره نام دامنه ها در فایل CSV
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain Name'])
        for domain in domains:
            writer.writerow([domain])

# لیست گسترده کلمات فارسی و بین‌المللی
premium_words = [
    # کلمات فارسی
    'ara', 'saz', 'kar', 'fan', 'ray', 'ban', 'sab', 'meh', 'rav', 'kav',
    'por', 'tiz', 'ram', 'min', 'lav', 'pou', 'gol', 'mor', 'dar', 'kuh',
    'sta', 'mah', 'bad', 'nar', 'yal', 'yas', 'sib', 'ran', 'neg', 'baz',
    'for', 'kha', 'tej', 'san', 'ser', 'mar', 'mod', 'rang', 'nagh', 'noj',
    'zib', 'lat', 'naz', 'shir', 'far', 'abr', 'aft', 'shab', 'roo', 'soo',
    'dor', 'chesh', 'del', 'jan', 'rokh', 'gosh', 'dast', 'pa', 'sar', 'tan',
    
    # کلمات بین‌المللی
    'web', 'net', 'dig', 'app', 'pro', 'max', 'top', 'new', 'get', 'try',
    'my', 'zen', 'box', 'ex', 'ax', 'up', 'ly', 'fy', 'io', 'ai', 'tech',
    'data', 'cloud', 'code', 'dev', 'pixel', 'byte', 'bit', 'smart', 'fast',
    'clean', 'pure', 'sharp', 'bright', 'true', 'core', 'base', 'meta', 'neo',
    'ultra', 'arc', 'apex', 'zen', 'nova', 'flux', 'wave', 'sync', 'flow'
]

# تولید 500 نام دامنه پریمیوم
premium_domains = generate_premium_domains(premium_words, 1999)

# ذخیره در فایل CSV
save_to_csv(premium_domains)

print(f"✅ تولید {len(premium_domains)} نام دامنه پریمیوم با موفقیت انجام شد!")
print("📁 فایل 'premium_web_domains.csv' ایجاد شد.")

# نمایش نمونه‌ای از بهترین دامنه‌ها
print("\n🎯 نمونه‌هایی از بهترین دامنه‌های تولید شده:")
for i, domain in enumerate(premium_domains[:30]):
    print(f"{domain}")