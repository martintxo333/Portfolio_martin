import webbrowser # URLak zuzenean sistemaren lehenetsitako nabigatzailean irekitzeko aukera ematen du (Chrome, Edge, Firefox, etab.).
import os # Sistema eragilearekin (windows) elkarreragiteko balio du. 
# Kasu honetan, sortuko den HTML fitxategiaren ibilbide absolutua lortzeko erabiltzen da.

# Hemen, portfolioaren HTML kode osoa duen kate multilineo bat definitzen da (komatxo hirukoitzen artean).

# Pythonen ikuspuntutik:
# Ez du HTML "ulertzen", hau da, testu lau gisa tratatzen du.

# Nabigatzailearen ikuspuntutik:
# Testu hau web orri oso bat da, egitura, estilo eta edukiarekin.

# <head>: konfigurazio nagusia
# <title> --> nabigatzailearen pestañan agertzen dena. 

# 26.lerroa: Inter iturria inportatzen du Google Fontsetik.
# 27.lerroa: Font Awesome iturria inportatzen du cloudflare-tik, ikonoak jartzen uzten dizkidanak.


html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"> 
    <title>Portfolioa - Martin Maiz Negredo</title>

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">

    <!-- Ikonoak -->
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <style>
        body {
             font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f2f4f7, #e5e7eb);
            margin: 0;
            padding: 0;
        }

        .overlay {
            background-color: rgba(242, 244, 247, 0.95);
            min-height: 100vh;
            padding: 40px 0;
        }

        .container {
            max-width: 900px;
            margin: auto;
            background-color: white;
            padding: 40px;
            border-radius: 14px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        }

        .header {
            display: flex;
            align-items: center;
            gap: 30px;
        }

        .header img {
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid #e0e0e0;
        }

        h1 {
            margin: 0;
            font-size: 32px;
            color: #1f2933;
        }

        h2 {
            margin-top: 40px;
            color: #374151;
            font-size: 22px;
        }

        p {
            font-size: 16px;
            line-height: 1.7;
            color: #4b5563;
        }

        .links {
            display: flex;
            gap: 30px;
            margin-top: 20px;
        }

        .links a {
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            font-weight: 600;
            color: #1a73e8;
            font-size: 18px;
        }

        .links a:hover {
            color: #0f4db8;
        }

        footer {
            margin-top: 50px;
            font-size: 14px;
            color: #6b7280;
            text-align: center;
            border-top: 1px solid #e5e7eb;
            padding-top: 20px;
        }
    </style>
</head>

<body>
    <div class="overlay">
        <div class="container">

            <div class="header">
                <img src="argazki_martin.jpg" alt="Martin Maiz-en argazkia">

                <div>
                    <h1>Martin Maiz Negredo</h1>
                    <p>
                        Industria Informatikako ikaslea
                    </p>
                </div>
            </div>

            <h2>Nere sare sozial profesionalak:</h2>
            <div class="links">
                <a href="https://github.com/martintxo333" target="_blank">
                    <i class="fab fa-github"></i> GitHub
                </a>

                <a href="https://www.linkedin.com/in/martin-maiz-negredo" target="_blank">
                    <i class="fab fa-linkedin"></i> LinkedIn
                </a>
            </div>

            <footer>
                Pythonekin automatikoki sortutako portfolio pertsonala.<br>
            </footer>

        </div>
    </div>
</body>
</html>
"""

file_name = "portfolio_martin.html"

with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_content)

file_path = os.path.abspath(file_name)
webbrowser.open(f"file://{file_path}")
