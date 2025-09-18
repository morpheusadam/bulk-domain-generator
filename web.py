import csv

# مسیر دیکشنری طولانی انگلیسی
dictionary_file = "english-words/words.txt"

# بارگذاری دیکشنری و فیلتر کلمات کوتاه
with open(dictionary_file, 'r', encoding='utf-8') as f:
    all_words = [word.strip().lower() for word in f.readlines() if 1 <= len(word.strip()) <= 3]

# دامنه‌ها در حافظه
domains = []

# ترتیب: ابتدا 4 حرفی، سپس 5، سپس 6
for length in [1, 2, 3]:  # طول x، چون web = 3 حرف → total = 3+len(x) ≤6
    words_x = [w for w in all_words if len(w) == length]
    
    for w in words_x:
        # web + x
        if len("web"+w) <= 6:
            domains.append("web"+w)
        # x + web
        if len(w+"web") <= 6:
            domains.append(w+"web")

# حذف تکراری‌ها و مرتب‌سازی بر اساس طول دامنه
domains = sorted(list(set(domains)), key=len)

# تقسیم دامنه‌ها به فایل‌های 1999 تایی
batch_size = 1999
for i in range(0, len(domains), batch_size):
    batch_domains = domains[i:i+batch_size]
    filename = f"web_domains_batch_{i//batch_size + 1}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain Name'])
        for domain in batch_domains:
            writer.writerow([domain])
    print(f"فایل '{filename}' ساخته شد با {len(batch_domains)} دامنه.")

print(f"\nکل {len(domains)} دامنه ساخته شد و در فایل‌ها ذخیره شد.")
