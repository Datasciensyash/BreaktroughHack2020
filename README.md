# BreaktroughHack2020

---
Use-case of vk_parser

```python
from vk_parser import VkParser 

parser = VkParser(token='your token...')

parser.get_posts(count=10)

>>> [{'uid': 42342442, 'text': 'Отдам помидоры...', 'category': 'Vegetables', 'location': 'Moscow', 'imgs': 'https://sun1-83.userapi.com/GE_s8ISzKaFlWvxwf_BQcqdRCvqHWVEblEjuAQ/OAeJmAI3DcA.jpg https://sun1-90.userapi.com/D0hGvzNOvYSuC5i6Axfklcz5Eyh-phqaAyp-HA/EQzMeWUWQ54.jpg' ...}, {'uid': 55434, 'text': 'Отдам огурцы', ...} ...]

```
 
