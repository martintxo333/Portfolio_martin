# Portfolio pertsonala Python-ekin [EUS]

Python erabiliz egindako programa, **portfolio web orri bat** sortzen duena automatikoki eta **aurrez definitutako nabigatzailean** irekitzen duena.

---

# Automatic Python Portfolio [EN]

## Project Description

This project is a learning exercise developed for the subject **Industrial Informatics** at the **University of the Basque Country (EHU).**

The program was independently conceived and developed as a **personal initiative** with the objective of practicing **Python programming** while working with **file handling, HTML generation, CSS styling, and web browser automation.**

The script generates a **personal portfolio webpage** with structured content, including:

* Name and description
* Profile picture
* Links to professional social networks (GitHub, LinkedIn) with icons
* Modern styling using **CSS** and **Google Fonts**

The HTML page is automatically saved to a local file and opened in the **system’s default web browser**, providing an immediate visual preview.

The project is intended for **educational purposes** and to practice **Python file handling** and **web content generation**.

---

## Technologies Used

* **Python 3**
* **HTML5 & CSS**
* **Google Fonts**
* **Font Awesome icons**
* **Web Browser module** – opens the generated page automatically

---

## Features

* Creates a **personal portfolio page** dynamically.
* Uses **Python** to generate HTML and CSS content.
* Opens the portfolio automatically in the default browser.
* Clean and modern design with responsive layout.
* Easy to modify: just edit the HTML string in the script.

---

## File Description

### `blog_martin.py`

Main Python script that:

1. Defines the HTML content of the portfolio as a **multiline string**.
2. Writes the HTML content into a file named `portfolio_martin.html`.
3. Obtains the **absolute file path** of the HTML.
4. Opens the HTML file automatically in the **default web browser**.

⚠️ **Note:**
Make sure the image `argazki_martin.jpg` is in the same folder as the script, otherwise the profile picture won’t display.

---

## Usage

1. Place the script `portfolio_generator.py` and your profile image in the same folder.
2. Run the script:

```bash
python portfolio_generator.py
```

3. Your default browser will open automatically with the generated portfolio page.

---

## Author

**Martin Maiz Negredo**

---

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for license rights and limitations.
