import requests
from bs4 import BeautifulSoup
import pandas as pd


"""class datacollection:
    def __init__(self):
            pass
    
    def data_collection(self):
            data = []

            for i in range(1, 4):  
                url = f'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&param=19873&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk1vdG9yb2xhIHNtYXJ0cGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=21.productCard.PMU_V2_16&sort=popularity&page={i}'

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
                }

                response = requests.get(url, headers=headers)

                if response.status_code != 200:
                    print(f"Failed to retrieve page {i}")
                    continue

                soup = BeautifulSoup(response.content, "html.parser")

                products = soup.find_all("div", class_="cPHDOP")  
                for product in products:
                    title = product.find("div", class_="KzDlHZ")
                    price = product.find("div", class_="Nx9bqj _4b5DiR")
                    actual_price = product.find("div", class_="yRaY8j ZYYwLA")
                    rating = product.find("div", class_="_5OesEi")
                    storage = product.find("div", class_="_6NESgJ")

                    if title and price:
                        product_data = {
                            "Product": title.text.strip(),
                            "Price": price.text.strip(),
                            "Actual Price": actual_price.text.strip() if actual_price else "N/A",
                            "Rating": rating.text.strip() if rating else "No rating",
                            "Storage": storage.text.strip() if storage else "N/A"
                        }
                        data.append(product_data)

                print(f"Page {i} scraped successfully")

            product_df = pd.DataFrame(data)

            product_df.to_csv(r"C:\Users\hp\Downloads\mlbootcamp\data\raw_data\flipkart_motorola_products.csv", index=False)

            print(f"Scraped {product_df.shape[0]} products.")
    
if __name__=='__main__':
    try:
        obj = datacollection()
        obj.data_collection()
    except Exception as e:
         raise e"""
    
