# Bulk Domain Generator

A simple PHP script to generate bulk domain name lists (CSV) for **Namecheap Bulk Search** or other domain search tools.

## ✨ Features
- Generates domain names with the pattern `web + [a-z][a-z] + .com`  
  (e.g. `webaa.com`, `webzz.com`, `webaz.com`, etc.)
- Automatically splits output into multiple CSV files (5000 rows per file).
- CSV format is compatible with **Namecheap Bulk Domain Search**.

## 📂 Output
- Files will be created in the same directory:
domains_1.csv
domains_2.csv
...

- Each file starts with the required header:


Domain
webaa.com
webab.com
...


## 🚀 Usage
1. Clone this repo:
 ```bash
 git clone https://github.com/your-username/bulk-domain-generator.git
 cd bulk-domain-generator


Run the PHP script:

php generate.php


Check the generated CSV files in the project folder.

🔧 Requirements

PHP 7.4+ (CLI)

📜 License

This project is released under the MIT License
.


---

می‌خوای همین الان برات یک فایل `LICENSE` هم (مثل MIT) آماده کنم تا ریپوزیتوریت کامل‌تر بشه؟
