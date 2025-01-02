## 🌐 Subdomain Wordlist Generator

### 🔍 **Overview**
This tool automates the process of generating a wordlist of real subdomain keywords by leveraging Subfinder. It takes an input list of domains, extracts valid subdomains using Subfinder, and compiles them into a clean and optimized text-based wordlist.

### ⚙️ **Features**
- **Automated Subdomain Discovery:** Uses Subfinder to identify subdomains efficiently.
- **Custom Wordlist Generation:** Filters and organizes discovered subdomains into a reusable wordlist.
- **Easy Integration:** Simple text output format for seamless integration with other tools.
- **Optimized Performance:** Processes large input lists with speed and accuracy.

### 🚀 **How It Works**
1. Provide a list of domains as input.
2. The tool runs Subfinder to gather all valid subdomains.
3. Extracted subdomains are processed and cleaned.
4. A final wordlist is generated and saved in a text file.

### 📦 **Installation**
```bash
git clone https://github.com/llMNMll/submaker.git
cd submaker
run with Command 
```

### 🛠️ **Usage**
```bash
python3 submaker.py -file-domain input_domains.txt -threads 10
```
- `-file-domain`: Path to the input file containing domains.
- `-threads`: Number of threads to use for parallel processing (optional).

### 📚 **Dependencies**
- Python 3.x
- Subfinder

### 🤝 **Contributions**
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

### 📜 **License**
This project is licensed under the MIT License.

### ⭐ **Support**
If you find this tool useful, don't forget to star the repository and share it with others!

**Happy Hunting! 🕵️‍♂️**

