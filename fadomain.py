import requests
import csv
from time import sleep

def check_domain_availability(domain_name, api_key, api_secret):
    """
    چک کردن وضعیت دامنه با استفاده از GoDaddy API
    """
    url = f"https://api.godaddy.com/v1/domains/available?domain={domain_name}"
    
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if response.status_code == 200:
            return data.get('available', False)
        else:
            print(f"خطا برای دامنه {domain_name}: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"خطا در بررسی {domain_name}: {str(e)}")
        return False

def filter_available_domains(input_csv, output_csv, api_key, api_secret, delay=1):
    """
    فیلتر کردن دامنه‌های آزاد از لیست CSV
    """
    available_domains = []
    
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  #跳过标题行
        
        for row in reader:
            if row:  # مطمئن شویم سطر خالی نیست
                domain_name = row[0].split('.')[0]  # فقط نام بدون پسوند
                full_domain = row[0]
                
                print(f"در حال بررسی: {full_domain}")
                
                if check_domain_availability(domain_name, api_key, api_secret):
                    available_domains.append(full_domain)
                    print(f"✅ آزاد: {full_domain}")
                else:
                    print(f"❌ ثبت‌شده: {full_domain}")
                
                sleep(delay)  # مکث برای جلوگیری از rate limiting
    
    # ذخیره دامنه‌های آزاد
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Available Domain Name'])
        for domain in available_domains:
            writer.writerow([domain])
    
    return available_domains

# اطلاعات احراز هویت API ( باید از GoDaddy بگیرید)
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

# فیلتر کردن دامنه‌ها
available_domains = filter_available_domains(
    input_csv="persian_web_domains.csv",
    output_csv="available_persian_domains.csv",
    api_key=API_KEY,
    api_secret=API_SECRET,
    delay=1  # مکث 1 ثانیه‌ای بین هر درخواست
)

print(f"✅ تکمیل شد! {len(available_domains)} دامنه آزاد پیدا شد.")