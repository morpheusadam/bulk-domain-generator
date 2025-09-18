import csv
import random
import subprocess
import platform
import time
import re
from typing import List, Tuple, Set
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===============================
# تنظیمات پیشرفته
# ===============================
DOMAIN_COUNT = 10000
MAX_WORKERS = 40
BATCH_SIZE = 150
PING_TIMEOUT = 1
WHOIS_TIMEOUT = 2
OUTPUT_FILE = "premium_web_domains.csv"
LOG_FILE = "domain_check.log"

# ===============================
# تولید دامنه‌های خلاقانه با پیشوند و پسوند web
# ===============================
def generate_web_domains(count: int = DOMAIN_COUNT) -> List[str]:
    """
    تولید دامنه‌های خلاقانه که با web شروع و به web ختم می‌شوند
    و حداکثر 8 کاراکتر دارند (بدون احتساب .com)
    """
    domains: Set[str] = set()
    
    # کلمات فارسی کوتاه و معنادار (2-4 حرفی)
    persian_keywords = [
        'saz', 'kar', 'yar', 'ban', 'fan', 'ray', 'zib', 'gol', 'mor', 'dar',
        'abr', 'ava', 'bar', 'bad', 'naz', 'shad', 'roz', 'ruz', 'noo', 'roo',
        'too', 'poo', 'koo', 'moo', 'soo', 'voo', 'zoo', 'foo', 'goo', 'hoo',
        'doo', 'boo', 'noo', 'roo', 'too', 'poo', 'koo', 'moo', 'soo', 'voo',
        'set', 'met', 'pet', 'ket', 'let', 'net', 'vet', 'zet', 'fet', 'get',
        'pan', 'tan', 'van', 'zan', 'fan', 'gan', 'han', 'jan', 'kan', 'lan',
        'mar', 'nar', 'par', 'rar', 'sar', 'tar', 'var', 'zar', 'far', 'gar',
        'ash', 'esh', 'ish', 'osh', 'ush', 'ash', 'esh', 'ish', 'osh', 'ush',
        'ali', 'eli', 'ili', 'oli', 'uli', 'api', 'epi', 'ipi', 'opi', 'upi'
    ]
    
    # الگوهای خلاقانه برای ترکیب با web
    creative_patterns = [
        # الگو: web + کلمه فارسی
        lambda: f"web{random.choice(persian_keywords)}",
        
        # الگو: web + کلمه فارسی + web
        lambda: f"web{random.choice(persian_keywords)}web",
        
        # الگو: کلمه فارسی کوتاه + web
        lambda: f"{random.choice([w for w in persian_keywords if len(w) <= 3])}web",
        
        # الگو: web + ترکیب دو حرفی
        lambda: f"web{random.choice(persian_keywords)}{random.choice(persian_keywords)}"[:8],
        
        # الگو: web + کلمه متقارن
        lambda: f"web{random.choice(['ana', 'elle', 'otto', 'assa', 'esse'])}",
        
        # الگو: web + تکرار حروف
        lambda: f"web{random.choice(['aa', 'ee', 'ii', 'oo', 'uu'])}",
        
        # الگو: web + اعداد معنادار
        lambda: f"web{random.choice(['24', '7', '360', '100', '500'])}",
        
        # الگو: web + پسوندهای خلاقانه
        lambda: f"web{random.choice(['ify', 'able', 'ious', 'ment', 'tion'])}"
    ]
    
    attempts = 0
    max_attempts = count * 10
    
    print("🎨 در حال تولید دامنه‌های وب خلاقانه...")
    print("📏 محدودیت: حداکثر 8 کاراکتر، شروع و پایان با web")
    
    while len(domains) < count and attempts < max_attempts:
        attempts += 1
        
        # انتخاب الگوی تصادفی
        pattern = random.choice(creative_patterns)
        domain_base = pattern()
        
        # اعمال فیلترهای سختگیرانه
        if (4 <= len(domain_base) <= 8 and  # طول 4-8 کاراکتر
            domain_base.startswith('web') and  # شروع با web
            (domain_base.endswith('web') or len(domain_base) <= 6) and  # پایان با web یا کوتاه
            re.match(r'^[a-z0-9]+$', domain_base) and  # فقط حروف و اعداد
            not any(c * 3 in domain_base for c in domain_base) and  # جلوگیری از تکرار بیش از حد
            domain_base not in domains):
            
            domain_name = f"{domain_base}.com"
            domains.add(domain_name)
        
        # نمایش پیشرفت
        if attempts % 500 == 0:
            print(f"📊 پیشرفت: {len(domains)}/{count} دامنه تولید شده")
    
    return sorted(list(domains), key=len)

# ===============================
# سیستم امتیازدهی پیشرفته
# ===============================
def advanced_domain_scoring(domain: str) -> int:
    """
    امتیازدهی هوشمند بر اساس معیارهای مختلف
    """
    domain_base = domain.split('.')[0]
    score = 0
    
    # امتیاز طول (بهینه: 5-7 کاراکتر)
    length = len(domain_base)
    if length == 5:
        score += 30
    elif length == 6:
        score += 25
    elif length == 4:
        score += 20
    elif length == 7:
        score += 15
    elif length == 8:
        score += 10
    
    # امتیاز الگوهای خاص
    if domain_base.startswith('web') and domain_base.endswith('web'):
        score += 50  # الگوی web___web بسیار پریمیوم
    elif domain_base.startswith('web'):
        score += 30  # الگوی web___ 
    elif domain_base.endswith('web'):
        score += 25  # الگوی ___web
    
    # امتیاز حروف متقارن و تلفظ آسان
    if re.match(r'^[aeiou]{2,}', domain_base[3:]):
        score += 15  # شروع با حروف صدادار پس از web
    if re.search(r'([aeiou])\1', domain_base):
        score -= 10  # کاهش امتیاز برای تکرار حروف صدادار
    
    # امتیاز اعداد معنادار
    if any(num in domain_base for num in ['24', '7', '360', '100']):
        score += 20
    
    # امتیاز کلمات کلیدی پرطرفدار
    premium_keywords = ['pro', 'max', 'plus', 'gold', 'vip', 'prime']
    for keyword in premium_keywords:
        if keyword in domain_base:
            score += 25
    
    return max(score, 0)  # امتیاز منفی نداشته باشیم

# ===============================
# بررسی فنی دامنه
# ===============================
def technical_domain_check(domain: str) -> Tuple[bool, int]:
    """
    بررسی فنی دامنه با روش‌های مختلف
    """
    try:
        # بررسی اولیه با Ping
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        ping_process = subprocess.run(
            ["ping", param, "1", domain],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=PING_TIMEOUT,
            check=False
        )
        
        if ping_process.returncode == 0:
            return False, 0  # دامنه فعال است
        
        # بررسی با WHOIS
        try:
            whois_process = subprocess.run(
                ["whois", domain],
                capture_output=True,
                text=True,
                timeout=WHOIS_TIMEOUT,
                check=False
            )
            
            if whois_process.returncode == 0:
                output = whois_process.stdout.lower()
                
                # الگوهای نشان‌دهنده دامنه آزاد
                free_patterns = [
                    r"no match", r"not found", r"available", r"free",
                    r"domain not found", r"no entries found", r"status: free"
                ]
                
                for pattern in free_patterns:
                    if re.search(pattern, output):
                        score = advanced_domain_scoring(domain)
                        return True, score
                
                return False, 0  # دامنه ثبت شده است
            
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            pass
        
        # اگر به اینجا رسیدیم، دامنه احتمالاً آزاد است
        score = advanced_domain_scoring(domain)
        return True, score
        
    except Exception as e:
        # در صورت بروز خطا، دامنه را آزاد در نظر می‌گیریم
        score = advanced_domain_scoring(domain)
        return True, score

# ===============================
# پردازش هوشمند دامنه‌ها
# ===============================
def intelligent_domain_processing(domains: List[str]) -> List[Tuple[str, int]]:
    """
    پردازش هوشمند دامنه‌ها با مدیریت پیشرفته
    """
    available_domains: List[Tuple[str, int]] = []
    total = len(domains)
    
    print(f"🔍 شروع بررسی {total} دامنه...")
    print("⚡ از روش‌های پیشرفته Ping و WHOIS استفاده می‌شود")
    
    # ایجاد فایل لاگ
    with open(LOG_FILE, 'w', encoding='utf-8') as log:
        log.write(f"🕒 شروع بررسی: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log.write("=" * 60 + "\n")
        
        for i in range(0, total, BATCH_SIZE):
            batch = domains[i:i + BATCH_SIZE]
            batch_number = (i // BATCH_SIZE) + 1
            total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
            
            print(f"📦 دسته {batch_number}/{total_batches} - {len(batch)} دامنه")
            
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                future_to_domain = {
                    executor.submit(technical_domain_check, domain): domain 
                    for domain in batch
                }
                
                for future in as_completed(future_to_domain):
                    domain = future_to_domain[future]
                    try:
                        is_available, score = future.result(timeout=10)
                        
                        if is_available and score > 0:
                            available_domains.append((domain, score))
                            log.write(f"✅ FREE: {domain} (Score: {score})\n")
                            print(f"✅ یافت شد: {domain}")
                        else:
                            log.write(f"❌ TAKEN: {domain}\n")
                            
                    except Exception as e:
                        log.write(f"⚠️ ERROR: {domain} - {str(e)}\n")
            
            # ذخیره موقت نتایج
            if available_domains:
                save_results(available_domains, "temp_results.csv")
            
            # استراحت بین دسته‌ها
            if i + BATCH_SIZE < total:
                time.sleep(0.5)
    
    return available_domains

# ===============================
# ذخیره‌سازی نتایج
# ===============================
def save_results(domains: List[Tuple[str, int]], filename: str):
    """
    ذخیره نتایج با فرمت پیشرفته
    """
    # مرتب‌سازی بر اساس امتیاز (نزولی) و سپس طول (صعودی)
    sorted_domains = sorted(
        domains, 
        key=lambda x: (-x[1], len(x[0]))
    )
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Domain', 'Score', 'Length', 'Pattern', 'Status', 'Timestamp'])
        
        for domain, score in sorted_domains:
            domain_base = domain.split('.')[0]
            length = len(domain_base)
            
            # تشخیص الگو
            if domain_base.startswith('web') and domain_base.endswith('web'):
                pattern = "web___web"
            elif domain_base.startswith('web'):
                pattern = "web___"
            elif domain_base.endswith('web'):
                pattern = "___web"
            else:
                pattern = "other"
            
            writer.writerow([
                domain, score, length, pattern, 
                'Available', time.strftime('%Y-%m-%d %H:%M:%S')
            ])

# ===============================
# گزارش نهایی حرفه‌ای
# ===============================
def generate_professional_report(domains: List[Tuple[str, int]]):
    """
    تولید گزارش حرفه‌ای از نتایج
    """
    if not domains:
        print("⚠️ هیچ دامنه آزادی یافت نشد!")
        return
    
    # مرتب‌سازی نهایی
    final_domains = sorted(
        domains, 
        key=lambda x: (-x[1], len(x[0]))
    )
    
    # ذخیره نتایج نهایی
    save_results(final_domains, OUTPUT_FILE)
    
    # تولید گزارش متنی
    with open('premium_domains_report.txt', 'w', encoding='utf-8') as report:
        report.write("🏆 گزارش دامنه‌های پریمیوم\n")
        report.write("=" * 50 + "\n")
        report.write(f"تاریخ تولید: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write(f"تعداد دامنه‌های آزاد: {len(final_domains)}\n")
        report.write("=" * 50 + "\n\n")
        
        report.write("🎯 20 دامنه برتر:\n")
        for i, (domain, score) in enumerate(final_domains[:20], 1):
            report.write(f"{i:2d}. {domain} (امتیاز: {score})\n")
    
    # نمایش در کنسول
    print(f"\n🎉 عملیات کامل شد!")
    print(f"✅ تعداد دامنه‌های آزاد یافت شده: {len(final_domains)}")
    print(f"💾 نتایج در {OUTPUT_FILE} ذخیره شد")
    print(f"📊 گزارش کامل در premium_domains_report.txt ذخیره شد")
    
    if final_domains:
        print("\n🏆 10 دامنه برتر:")
        for i, (domain, score) in enumerate(final_domains[:10], 1):
            print(f"{i:2d}. {domain} (امتیاز: {score})")

# ===============================
# اجرای اصلی
# ===============================
def main():
    start_time = time.time()
    
    try:
        print("=" * 60)
        print("🚀 سامانه تولید و بررسی دامنه‌های وب پریمیوم")
        print("=" * 60)
        
        # مرحله 1: تولید دامنه‌ها
        print("\n📝 مرحله 1: تولید دامنه‌های خلاقانه")
        domains = generate_web_domains(DOMAIN_COUNT)
        print(f"✅ {len(domains)} دامنه تولید شد")
        
        # مرحله 2: بررسی فنی
        print("\n🔍 مرحله 2: بررسی فنی دامنه‌ها")
        available_domains = intelligent_domain_processing(domains)
        
        # مرحله 3: گزارش نهایی
        print("\n📊 مرحله 3: تولید گزارش نهایی")
        generate_professional_report(available_domains)
        
        # آمار نهایی
        end_time = time.time()
        total_time = end_time - start_time
        print(f"\n⏱️ زمان کل اجرا: {total_time:.2f} ثانیه")
        print(f"📈 میانگین زمان بر هر دامنه: {total_time/len(domains):.3f} ثانیه")
        
    except KeyboardInterrupt:
        print("\n⏹️ عملیات توسط کاربر متوقف شد")
    except Exception as e:
        print(f"\n❌ خطا: {str(e)}")
    finally:
        print("\n✨ برنامه به پایان رسید")

if __name__ == "__main__":
    main()