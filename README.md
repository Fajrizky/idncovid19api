<div align="center">
  <h2 align="center">Covid Cases and Vaccination Rates In Indonesia</h2>
  <h3 align="center">Nodeflux</h3>
  <p align="center">
    Software Engineer Internship Technical Assessment - Batch 2
  </p>
</div>

## Route
* /: Entry point for all API, provide general information of covid cases.
* /yearly/[year]: Provide yearly data of total covid cases of the year provided in [year].
* /yearly?since=[year]&?upto=[year]: Provide yearly data of total covid cases.
* /monthly/[year.month]: Provide monthly data of total covid cases of the year provided in [month].
* /monthly?since=[year.month]&?upto=[year.month]: Provide monthly data of total covid cases.

<!-- INSTALASI -->
## Installation
Berikut ini cara instalasi project dengan server local, silahkan mengikuti cara dibawah ini.

### Persiapan
Dokumentasi resmi <a href="https://flask.palletsprojects.com/en/2.0.x/"> klik disini </a>
* Pastikan komputer anda telah terinstall python versi 3.

<!-- PENGGUNAAN -->
## Usage
* Menjalankan Server local dengan debug
  ```sh
   python app.py
   ```

* Buka browser untuk membuka project
   ```sh
   http://127.0.0.1:5005/
   ```
## License
[MIT](https://choosealicense.com/licenses/mit/)
