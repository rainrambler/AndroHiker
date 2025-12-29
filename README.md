# AndroHiker

AndroHiker is an Android security analysis toolkit that provides efficient tools for searching and analyzing permissions within APK files. It offers both aapt2-based and Androguard-based scanning methods, allowing you to choose the right tool for your needs.

## Features

- **Multi-threaded APK scanning** using `aapt2` for fast permission detection
- **In-depth APK analysis** using Androguard for detailed permission extraction
- **Batch processing** of APK files within directories
- **Configurable thread pool** for optimized performance
- **Verbose output option** for detailed processing information

## Prerequisites

- Python 3.7+
- Android SDK (for aapt2) or Androguard library
- For `aapt_find.py`: aapt2.exe available at the specified path (modify the script if needed)
- For `find_perm.py`: Androguard library installed

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rainrambler/AndroHiker.git
cd AndroHiker
```

2. Install required Python packages:
```bash
pip install androguard
```

3. For `aapt_find.py`, ensure aapt2 is available:
   - Update the `aapt_path` variable in `aapt_find.py` to point to your local aapt2 executable
   - Or install Android SDK and set the correct path

## Usage

### Option 1: Fast Permission Scanning with aapt2 (`aapt_find.py`)

This script uses aapt2 for quick permission scanning with multi-threading support.

```bash
python aapt_find.py <directory> <permission> [options]
```

**Examples:**
```bash
# Search for INTERNET permission in all APKs within ./apks folder
python aapt_find.py ./apks android.permission.INTERNET

# Search with verbose output and 8 threads
python aapt_find.py ./apks android.permission.CAMERA -v -t 8

# Search for ACCESS_FINE_LOCATION permission
python aapt_find.py ./samples android.permission.ACCESS_FINE_LOCATION
```

**Arguments:**
- `directory`: Path to the directory containing APK files
- `permission`: Permission name to search for (e.g., `android.permission.CAMERA`)
- `-v, --verbose`: Show detailed processing information
- `-t THREADS, --threads THREADS`: Number of threads to use (default: 4)

### Option 2: Detailed Analysis with Androguard (`find_perm.py`)

This script uses Androguard for more comprehensive APK analysis.

```python
from find_perm import find_permission_in_dir

# Search for permissions in a directory
find_permission_in_dir("android.permission.RECORD_AUDIO", "./apk_samples")
```

Or run as a module:
```bash
# Create a runner script or modify find_perm.py to accept command line arguments
```

## Script Comparison

| Feature | `aapt_find.py` | `find_perm.py` |
|---------|----------------|----------------|
| **Speed** | Fast (multi-threaded) | Slower (detailed parsing) |
| **Dependencies** | aapt2 tool | Androguard library |
| **Output** | Simple file list | Detailed permission info |
| **Use Case** | Bulk scanning | Deep analysis |

## Example Output

### aapt_find.py

```
找到 42 个APK文件
✓ 匹配: ./apks/com.example.app1.apk
✓ 匹配: ./apks/com.example.app2.apk

包含权限 'android.permission.CAMERA' 的APK: 2/42
  - ./apks/com.example.app1.apk
  - ./apks/com.example.app2.apk
```

### find_perm.py

```
找到: malicious_app.apk
  权限: android.permission.SEND_SMS
找到: tracker_app.apk  
  权限: android.permission.ACCESS_FINE_LOCATION
解析失败 corrupted_app.apk: Invalid APK file
```

## Common Android Permissions to Search For

- `android.permission.INTERNET`
- `android.permission.ACCESS_FINE_LOCATION`
- `android.permission.CAMERA`
- `android.permission.RECORD_AUDIO`
- `android.permission.READ_SMS`
- `android.permission.SEND_SMS`
- `android.permission.READ_CONTACTS`
- `android.permission.READ_CALENDAR`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and authorized security testing purposes only. Only use it on APK files you own or have permission to analyze. The developers are not responsible for any misuse of this tool.

## Support

For issues or questions, please open an Issue on the GitHub repository.