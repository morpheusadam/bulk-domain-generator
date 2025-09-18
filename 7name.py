import csv
import itertools
import math

# بارگذاری دیکشنری از فایل
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f.readlines())

# تولید دامنه‌های معنی‌دار
def generate_meaningful_domains(chars, dictionary, add_prefix="7"):
    domains = set()

    # ترکیبات طول 3 و 4 بدون پیشوند
    for length in [3, 4]:
        for combo in itertools.product(chars, repeat=length):
            domain = "".join(combo)
            if domain in dictionary:
                domains.add(domain)

    # ترکیبات با پیشوند add_prefix
    for length in [2, 3]:  # طول با پیشوند <=4
        for combo in itertools.product(chars, repeat=length):
            domain = add_prefix + "".join(combo)
            if domain[1:] in dictionary:
                domains.add(domain)

    # تبدیل به لیست و مرتب‌سازی
    domains_list = list(domains)
    
    # مرتب‌سازی: ابتدا طول کلمه، سپس دامنه‌های با پیشوند '7' آخر
    domains_list.sort(key=lambda x: (len(x), x.startswith(add_prefix)))
    
    return domains_list

# ذخیره دامنه‌ها در فایل CSV (با تقسیم به دسته‌ها)
def save_domains_in_batches(domains, batch_size=1999, base_filename="domains_batch"):
    total_domains = len(domains)
    num_batches = math.ceil(total_domains / batch_size)
    
    for i in range(num_batches):
        start = i * batch_size
        end = start + batch_size
        batch_domains = domains[start:end]
        filename = f"{base_filename}_{i+1}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Domain Name'])
            for domain in batch_domains:
                writer.writerow([domain])
        print(f"فایل '{filename}' ذخیره شد با {len(batch_domains)} دامنه.")

# تنظیمات
chars = "abcdefghijklmnopqrstuvwxyz"
dictionary_file = "english-words/words.txt"  # مسیر فایل دیکشنری

# بارگذاری دیکشنری
dictionary = load_dictionary(dictionary_file)

# تولید دامنه‌ها
meaningful_domains = generate_meaningful_domains(chars, dictionary)

# ذخیره دامنه‌ها در دسته‌های 1999 تایی
save_domains_in_batches(meaningful_domains, batch_size=1999, base_filename="meaningful_domains")

print(f"کل {len(meaningful_domains)} دامنه معنی‌دار تولید شد و در فایل‌ها ذخیره شد.")
