# shopify-export-transformer
Get a well formatted xlsx for the products export

Shopify is able to export products in csv format, but the format is not very convenient to use as HTML linebreaks are included in the csv. This script will remove all unwanted linebreaks and transforms the  to a xlsx for further processing.


## Installation & Usage

1. Make sure you have Python 3 installed
2. Install pandas and openpyxl: `pip install pandas openpyxl`
3. Clone this repository
4. Export your products from Shopify as csv and save it in the folder `input`
5. Open and run `python3 shopify-export-transformer.py` in Jupyter Notebook 
6. Find the xlsx in the folder `output`