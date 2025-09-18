import random
import csv

# مسیر دیکشنری طولانی انگلیسی
dictionary_file = "english-words/words.txt"

# کلمات کلیدی مرتبط با وب و تکنولوژی
tech_keywords = ["web", "site", "dev", "code", "app", "data", "it", "net"]

# بارگذاری دیکشنری و فیلتر کلمات کوتاه و مرتبط
with open(dictionary_file, 'r', encoding='utf-8') as f:
    all_words = [word.strip().lower() for word in f.readlines() if 2 <= len(word.strip()) <= 6]

# فیلتر برای کلمات مرتبط با تکنولوژی
tech_words = [word for word in all_words if any(k in word for k in tech_keywords)]

# تولید لیست رندوم از دامنه‌ها
num_domains = 1999  # تعداد دلخواه، می‌توانید کمتر یا بیشتر کنید
random_domains = random.sample(tech_words, min(num_domains, len(tech_words)))

# دامنه‌ها در حافظه ذخیره شدند
# نمایش نمونه‌ها
print("نمونه دامنه کوتاه، رند و مرتبط با وب و تکنولوژی:")
for d in random_domains[:50]:
    print(d)

# ذخیره در CSV اگر خواسته باشید
with open("tech_short_memorable_domains.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Domain Name'])
    for domain in random_domains:
        writer.writerow([domain])

print(f"\nتعداد {len(random_domains)} دامنه کوتاه و به یادماندنی در فایل 'tech_short_memorable_domains.csv' ذخیره شد.")
