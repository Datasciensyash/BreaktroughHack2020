# BreaktroughHack2020

---

## Modules: VkParser (`vk_parser.py`)

Module for scraping and parsing vk for telegram bot.

#### City predicting.

Pipeline: Simple keyword search. Default city is Moscow, but if there are keywords (like `#СПб`, `м. Лиговский Проспект`, etc., stored in `spb.txt) related to Saint-Petersburg city we change it to Saint-Petersburg.

#### Predicting of product category.

Pipeline: 
- Vectorization by Tf-Idf (`./models/vectorizer.pkl`)
- Prediction with LogisticRegression (`./models/model.pkl`)
- Addiction: Classes stored in LabelEncoder (`./models/encoder.pkl`)

Class list: 
- Animal foods
- Aquantic foods
- Cereals and cereal products
- Cocoa and cocoa products
- Coffee and coffee products
- Fruits
- Gourds
- Herbs and Spices
- Nuts
- Pulses
- Soy
- Teas
- Vegetables

#### Usage example:

```python
from vk_parser import VkParser 

parser = VkParser(token='your token...')

parser.get_posts(count=10)

>>> [{'uid': 42342442, 'text': 'Отдам помидоры...', 'category': 'Vegetables', 'location': 'Moscow', 'imgs': 'https://sun1-83.userapi.com/GE_s8ISzKaFlWvxwf_BQcqdRCvqHWVEblEjuAQ/OAeJmAI3DcA.jpg https://sun1-90.userapi.com/D0hGvzNOvYSuC5i6Axfklcz5Eyh-phqaAyp-HA/EQzMeWUWQ54.jpg' ...}, {'uid': 55434, 'text': 'Отдам огурцы', ...} ...]

```
 
