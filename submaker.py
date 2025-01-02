import os
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor

# فایل خروجی شامل ورد لیست
OUTPUT_FILE = "wordlist.txt"

def run_subfinder(domain):
    """اجرای subfinder برای یک دامین و استخراج سابدامین‌ها"""
    try:
        result = subprocess.run(
            ["subfinder", "-d", domain, "-silent"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error while running subfinder for {domain}: {e}")
        return []

def extract_words(subdomains):
    """جدا کردن کلمات از سابدامین‌ها"""
    words = set()
    for subdomain in subdomains:
        words.update(subdomain.replace('-', '.').split('.'))
    return words

def process_domain(domain):
    """پردازش یک دامین: استخراج سابدامین‌ها و کلمات"""
    print(f"[INFO] Processing: {domain}")
    subdomains = run_subfinder(domain)
    words = extract_words(subdomains)
    print(f"[INFO] Done: {domain} - {len(subdomains)} subdomains, {len(words)} words")
    return words

def main(input_file, threads):
    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found.")
        return

    all_words = set()
    with open(input_file, "r") as f:
        domains = [line.strip() for line in f.readlines()]

    # مولتی‌تردینگ برای پردازش همزمان دامین‌ها
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(process_domain, domain): domain for domain in domains}
        for future in futures:
            words = future.result()
            all_words.update(words)

    # ذخیره ورد لیست در فایل خروجی
    with open(OUTPUT_FILE, "w") as f:
        for word in sorted(all_words):
            f.write(f"{word}\n")

    print(f"[INFO] Wordlist created: {OUTPUT_FILE} - {len(all_words)} unique words")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Wordlist Generator")
    parser.add_argument("-file-domain", required=True, help="Path to the input file containing domains")
    parser.add_argument("-threads", type=int, default=10, help="Number of threads to use (default: 10)")
    args = parser.parse_args()

    main(args.file_domain, args.threads)
