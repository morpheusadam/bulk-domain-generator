import csv
import random
import subprocess
import platform
from typing import List
from concurrent.futures import ThreadPoolExecutor

# -------------------------------
# تنظیمات
# -------------------------------
DOMAIN_COUNT = 5000        # تعداد دامنه مورد نظر برای تولید
MAX_WORKERS = 50           # تعداد Thread برای بررسی
OUTPUT_FILE = "free_web_domains.csv"
PING_TIMEOUT = 1           # ثانیه
WHOIS_TIMEOUT = 2          # ثانیه

# -------------------------------
# تولید دامنه‌ها
# -------------------------------
def generate_persian_web_domains(count: int = DOMAIN_COUNT) -> List[str]:
    """
    تولید دامنه‌های web+keyword.com
    """
    domains = set()

    # کلمات کوتاه و خلاقانه فارسی و انگلیسی
    persian_keywords = [
        'saz','kar','yar','ban','fan','ray','pardaz','sanj','sabt',
        'negar','nevis','azar','afrin','amoz','baz','forush','kharid',
        'khadam','modir','mozu','nojavan','zib','pak','sabz','tiz',
        'por','kheili','khosh','bakht','naz','shad','shirin','gol',
        'mor','dar','abr','ava','bahar','baran','chesh','darya','fajr',
        'gav','gandom','hayat','aseman','mah','narenj','narges','nasim',
        'nay','persis','pouya','rang','raaz','roya','sadaf','simin','snow',
        'sorkh','talai','tarane','yashar','yas','zal','data','tech','ai',
        'code','soft','app','net','host'
    ]

    max_attempts = count * 10
    attempts = 0

    while len(domains) < count and attempts < max_attempts:
        attempts += 1
        keyword = random.choice(persian_keywords)
        # ترکیب هوشمند برای کوتاه و جذاب شدن دامنه
        if random.random() < 0.3:
            keyword += random.choice(persian_keywords[:10])  # اضافه کردن یک پسوند کوتاه
        domain_name = f"web{keyword}.com"

        if 6 <= len(domain_name.split('.')[0]) <= 12 and domain_name not in domains:
            domains.add(domain_name)

    return sorted(list(domains))[:count]

# -------------------------------
# بررسی آزاد بودن دامنه
# -------------------------------
def is_domain_free(domain: str) -> bool:
    """
    بررسی آزاد بودن دامنه با ping و whois سریع
    """
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        subprocess.run(["ping", param, "1", domain],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,
                       timeout=PING_TIMEOUT,
                       check=True)
        return False
    except Exception:
        pass  # اگر ping ناموفق بود، احتمالاً آزاد است

    try:
        result = subprocess.run(["whois", domain],
                                capture_output=True,
                                text=True,
                                timeout=WHOIS_TIMEOUT)
        output = result.stdout.lower()
        free_indicators = [
            "no match", "not found", "no data found",
            "no entries found", "domain not found",
            "status: free", "available"
        ]
        return any(ind in output for ind in free_indicators)
    except Exception:
        return True  # در صورت خطا، فرض می‌کنیم آزاد است

# -------------------------------
# فیلتر دامنه‌ها و ذخیره مستقیم
# -------------------------------
def filter_and_save(domains: List[str], output_file: str = OUTPUT_FILE):
    """
    بررسی آزاد بودن دامنه‌ها و ذخیره مستقیم در CSV
    """
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain Name', 'Length'])

        def check_and_write(domain):
            if is_domain_free(domain):
                writer.writerow([domain, len(domain)])
                return True
            return False

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            list(executor.map(check_and_write, domains))

# -------------------------------
# اجرای برنامه
# -------------------------------
if __name__ == "__main__":
    print("🚀 تولید دامنه‌ها...")
    all_domains = generate_persian_web_domains(DOMAIN_COUNT)
    print(f"✅ {len(all_domains)} دامنه تولید شد.")

    print("🔍 بررسی آزاد بودن دامنه‌ها و ذخیره در فایل...")
    filter_and_save(all_domains, OUTPUT_FILE)

    print(f"✅ فرآیند تکمیل شد. دامنه‌های آزاد در '{OUTPUT_FILE}' ذخیره شدند.")
