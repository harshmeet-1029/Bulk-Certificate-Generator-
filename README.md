# 🎓 Bulk Certificate Generator

Generate personalized certificates en masse with just a few lines of code! 🚀

## 🌟 Features

- **Bulk Generation**: Create hundreds of certificates in seconds!
- **Customizable**: Easily adjust text position and font size.
- **CSV Integration**: Import names and dates from a CSV file.
- **High-Quality Output**: Generate professional-looking certificates.

## 🛠️ Prerequisites

- Python 3.x
- Pillow library
- Pandas library

## 🚀 Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Bulk-Certificate-Generator.git
   ```

2. Install required libraries:
   ```
   pip install pillow pandas
   ```

3. Prepare your CSV file (`list.csv`) with columns: `name` and `date`.

4. Add your certificate template as `certificate.jpg`.

5. Run the script:
   ```
   python certificate_generator.py
   ```

6. Find your generated certificates in the `pictures/` directory.

## 🎨 Customization

Adjust these lines to customize text placement and appearance:

```python
draw.text(xy=(170,507), text='{}'.format(j['name']), fill=(247,111,23), font=font)
draw.text(xy=(539,739), text='{}'.format(j['date']), fill=(0,0,0), font=font1)
```

## 📊 CSV Format

Ensure your `list.csv` file follows this format:

```
name,date
John Doe,2023-09-15
Jane Smith,2023-09-16
```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Certificate Generating! 🎉
