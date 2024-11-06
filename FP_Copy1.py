{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2593dd2e-d029-48d6-acdf-c1101fcf2e74",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from scipy.stats import ttest_1samp\n",
    "import scipy.stats as st\n",
    "from statsmodels.stats.proportion import proportions_ztest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9c590015-77c0-4da5-ad22-d5a12e568bb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01e43225-86e2-4790-a97b-87d16d3b6d4f",
   "metadata": {},
   "source": [
    "## FOOTLOCKER"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "79a00482-cf99-4327-a3b3-e59b6064d72d",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>department_name</th>\n",
       "      <th>category_name</th>\n",
       "      <th>sub_category_name</th>\n",
       "      <th>best_sell_rank</th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_name</th>\n",
       "      <th>titled_brands</th>\n",
       "      <th>retail_price</th>\n",
       "      <th>current_price</th>\n",
       "      <th>url</th>\n",
       "      <th>listing_url</th>\n",
       "      <th>SCAN_DATE</th>\n",
       "      <th>TID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>1</td>\n",
       "      <td>BB550LSB</td>\n",
       "      <td>New Balance BB550 - Men's</td>\n",
       "      <td>New Balance</td>\n",
       "      <td>110.0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/BB550LSB....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>775802</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>2</td>\n",
       "      <td>37758401</td>\n",
       "      <td>PUMA MB2 x Slime - Men's</td>\n",
       "      <td>PUMA</td>\n",
       "      <td>140.0</td>\n",
       "      <td>140.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/37758401....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>775803</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>3</td>\n",
       "      <td>M990GL6</td>\n",
       "      <td>New Balance 990V6 D - Men's</td>\n",
       "      <td>New Balance</td>\n",
       "      <td>200.0</td>\n",
       "      <td>200.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/M990GL6.html</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>775804</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>4</td>\n",
       "      <td>W2288111</td>\n",
       "      <td>Nike Air Force 1 '07 LE - Men's</td>\n",
       "      <td>Nike</td>\n",
       "      <td>110.0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/W2288111....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>775805</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>5</td>\n",
       "      <td>5950CHE</td>\n",
       "      <td>UGG Tasman - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>110.0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/5950CHE.html</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>775806</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3004</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>9999</td>\n",
       "      <td>1870DDWN</td>\n",
       "      <td>UGG Tasman LTA TOPO - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>100.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/1870DDWN....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>778806</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3005</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>9999</td>\n",
       "      <td>1870FRSN</td>\n",
       "      <td>UGG Tasman LTA TOPO - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>100.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/1870FRSN....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>778807</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3006</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>9999</td>\n",
       "      <td>7735BTOL</td>\n",
       "      <td>UGG Tasman Puff - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>100.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/7735BTOL....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>778808</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3007</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>9999</td>\n",
       "      <td>27735BLK</td>\n",
       "      <td>UGG Tasman Puff - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>100.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/27735BLK....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>778809</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3008</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>Shop All</td>\n",
       "      <td>9999</td>\n",
       "      <td>1324BLK</td>\n",
       "      <td>UGG Scuff Logo - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>100.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/1324BLK.html</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>2023/1/30 2:00</td>\n",
       "      <td>778810</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3009 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     department_name category_name sub_category_name  best_sell_rank  \\\n",
       "0              Men's         Shoes          Shop All               1   \n",
       "1              Men's         Shoes          Shop All               2   \n",
       "2              Men's         Shoes          Shop All               3   \n",
       "3              Men's         Shoes          Shop All               4   \n",
       "4              Men's         Shoes          Shop All               5   \n",
       "...              ...           ...               ...             ...   \n",
       "3004           Men's         Shoes          Shop All            9999   \n",
       "3005           Men's         Shoes          Shop All            9999   \n",
       "3006           Men's         Shoes          Shop All            9999   \n",
       "3007           Men's         Shoes          Shop All            9999   \n",
       "3008           Men's         Shoes          Shop All            9999   \n",
       "\n",
       "     product_id                     product_name titled_brands  retail_price  \\\n",
       "0      BB550LSB        New Balance BB550 - Men's   New Balance         110.0   \n",
       "1      37758401         PUMA MB2 x Slime - Men's          PUMA         140.0   \n",
       "2       M990GL6      New Balance 990V6 D - Men's   New Balance         200.0   \n",
       "3      W2288111  Nike Air Force 1 '07 LE - Men's          Nike         110.0   \n",
       "4       5950CHE               UGG Tasman - Men's           UGG         110.0   \n",
       "...         ...                              ...           ...           ...   \n",
       "3004   1870DDWN      UGG Tasman LTA TOPO - Men's           UGG         100.0   \n",
       "3005   1870FRSN      UGG Tasman LTA TOPO - Men's           UGG         100.0   \n",
       "3006   7735BTOL          UGG Tasman Puff - Men's           UGG         100.0   \n",
       "3007   27735BLK          UGG Tasman Puff - Men's           UGG         100.0   \n",
       "3008    1324BLK           UGG Scuff Logo - Men's           UGG         100.0   \n",
       "\n",
       "      current_price                                                url  \\\n",
       "0             110.0  https://www.footlocker.com/product/~/BB550LSB....   \n",
       "1             140.0  https://www.footlocker.com/product/~/37758401....   \n",
       "2             200.0  https://www.footlocker.com/product/~/M990GL6.html   \n",
       "3             110.0  https://www.footlocker.com/product/~/W2288111....   \n",
       "4             110.0  https://www.footlocker.com/product/~/5950CHE.html   \n",
       "...             ...                                                ...   \n",
       "3004          100.0  https://www.footlocker.com/product/~/1870DDWN....   \n",
       "3005          100.0  https://www.footlocker.com/product/~/1870FRSN....   \n",
       "3006          100.0  https://www.footlocker.com/product/~/7735BTOL....   \n",
       "3007          100.0  https://www.footlocker.com/product/~/27735BLK....   \n",
       "3008          100.0  https://www.footlocker.com/product/~/1324BLK.html   \n",
       "\n",
       "                                            listing_url       SCAN_DATE  \\\n",
       "0     https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "1     https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "2     https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "3     https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "4     https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "...                                                 ...             ...   \n",
       "3004  https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "3005  https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "3006  https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "3007  https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "3008  https://www.footlocker.com/category/mens/shoes...  2023/1/30 2:00   \n",
       "\n",
       "         TID  \n",
       "0     775802  \n",
       "1     775803  \n",
       "2     775804  \n",
       "3     775805  \n",
       "4     775806  \n",
       "...      ...  \n",
       "3004  778806  \n",
       "3005  778807  \n",
       "3006  778808  \n",
       "3007  778809  \n",
       "3008  778810  \n",
       "\n",
       "[3009 rows x 13 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "footlocker_df = pd.read_csv(\"Footlocker_Product.csv\")\n",
    "footlocker_df.isnull().sum()\n",
    "footlocker_df = footlocker_df.drop(columns=['rating', 'additional_data'])\n",
    "footlocker_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9b7e3b51-eca0-4878-9298-fc41cd3b53c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "footlocker_df.to_csv(\"Footlocker.csv\", index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "97ce3fbb-c9e3-48c3-a40d-71141a49182b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "footlocker_df[\"current_price\"].dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "88479278-4326-4707-8957-3ec45a49bd45",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_footlocker_df = footlocker_df[\"current_price\"].mean().round(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ed55853-a224-49ca-a21c-1a5b916d6fe0",
   "metadata": {},
   "source": [
    "## ASOS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3cbbd9e8-7215-4b79-85b0-7186c062512d",
   "metadata": {
    "scrolled": True
   },
   "outputs": [],
   "source": [
    "asos_df = pd.read_csv(\"products_asos.csv\")\n",
    "asos_df = asos_df.dropna(subset=['url'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "98bdaca0-54a3-4e1d-93f7-c524e384c134",
   "metadata": {},
   "outputs": [],
   "source": [
    "color_mapping = {\n",
    "    'black': ['black', 'BLACK', 'Black', 'jet black', 'charcoal', 'graphite'],\n",
    "    'white': ['white', 'WHITE', 'White', 'ivory', 'cream', 'off white'],\n",
    "    'red': ['red', 'RED', 'Red', 'maroon', 'burgundy', 'crimson'],\n",
    "    'blue': ['blue', 'BLUE', 'Blue', 'navy', 'sky blue', 'azure', 'cobalt'],\n",
    "    'green': ['green', 'GREEN', 'Green', 'olive', 'lime', 'mint', 'emerald'],\n",
    "    'yellow': ['yellow', 'YELLOW', 'Yellow', 'gold', 'mustard', 'amber'],\n",
    "    'pink': ['pink', 'PINK', 'Pink', 'fuchsia', 'rose', 'magenta'],\n",
    "    'purple': ['purple', 'PURPLE', 'Purple', 'lavender', 'violet', 'plum'],\n",
    "    'orange': ['orange', 'ORANGE', 'Orange', 'peach', 'apricot', 'coral'],\n",
    "    'brown': ['brown', 'BROWN', 'Brown', 'beige', 'tan', 'chocolate'],\n",
    "    'grey': ['grey', 'GREY', 'Grey', 'gray', 'charcoal'],\n",
    "    'neutral': ['neutral', 'Neutral', 'beige', 'taupe', 'camel', 'sand'],\n",
    "}\n",
    "\n",
    "def map_to_basic_color(color, color_mapping):\n",
    "    color = color.lower()\n",
    "    for basic_color, variants in color_mapping.items():\n",
    "        if color in variants:\n",
    "            return basic_color\n",
    "    return 'printed' \n",
    "    \n",
    "asos_df['basic_color'] = asos_df['color'].apply(lambda x: map_to_basic_color(str(x), color_mapping))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "db0e1eaa-889b-42e8-95f4-df3f13e73bdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "asos_df = asos_df.drop(columns=[\"color\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f560cae8-f48f-4efe-b297-213d91c9f174",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>url</th>\n",
       "      <th>name</th>\n",
       "      <th>size</th>\n",
       "      <th>category</th>\n",
       "      <th>price</th>\n",
       "      <th>sku</th>\n",
       "      <th>description</th>\n",
       "      <th>images</th>\n",
       "      <th>basic_color</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://www.asos.com/stradivarius/stradivarius...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>49.99</td>\n",
       "      <td>126704571.0</td>\n",
       "      <td>[{'Product Details': 'Coats &amp; Jackets by New L...</td>\n",
       "      <td>['https://images.asos-media.com/products/new-l...</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://www.asos.com/stradivarius/stradivarius...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>49.99</td>\n",
       "      <td>126704571.0</td>\n",
       "      <td>[{'Product Details': 'Coats &amp; Jackets by New L...</td>\n",
       "      <td>['https://images.asos-media.com/products/new-l...</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://www.asos.com/asos-design/asos-design-l...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>49.99</td>\n",
       "      <td>126704571.0</td>\n",
       "      <td>[{'Product Details': 'Coats &amp; Jackets by New L...</td>\n",
       "      <td>['https://images.asos-media.com/products/new-l...</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://www.asos.com/new-look/new-look-trench-...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...</td>\n",
       "      <td>New Look trench coat in camel</td>\n",
       "      <td>49.99</td>\n",
       "      <td>126704571.0</td>\n",
       "      <td>[{'Product Details': 'Coats &amp; Jackets by New L...</td>\n",
       "      <td>['https://images.asos-media.com/products/new-l...</td>\n",
       "      <td>neutral</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://www.asos.com/stradivarius/stradivarius...</td>\n",
       "      <td>Stradivarius double breasted wool coat in grey</td>\n",
       "      <td>XS - UK 6,S - UK 8,M - UK 10,L - UK 12,XL - UK 14</td>\n",
       "      <td>Stradivarius double breasted wool coat in grey</td>\n",
       "      <td>59.99</td>\n",
       "      <td>123650194.0</td>\n",
       "      <td>[{'Product Details': 'Coats &amp; Jackets by Strad...</td>\n",
       "      <td>['https://images.asos-media.com/products/strad...</td>\n",
       "      <td>grey</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30840</th>\n",
       "      <td>https://www.asos.com/urban-revivo/urban-revivo...</td>\n",
       "      <td>Urban Revivo square neck mini dress in floral ...</td>\n",
       "      <td>XS - UK 6 - Out of stock,S - UK 8 - Out of sto...</td>\n",
       "      <td>Urban Revivo square neck mini dress in floral ...</td>\n",
       "      <td>44.00</td>\n",
       "      <td>116745746.0</td>\n",
       "      <td>[{'Product Details': 'Mini dress by Urban Revi...</td>\n",
       "      <td>['https://images.asos-media.com/products/urban...</td>\n",
       "      <td>printed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30841</th>\n",
       "      <td>https://www.asos.com/asos-design/asos-design-l...</td>\n",
       "      <td>ASOS DESIGN long sleeve maxi t-shirt dress in ...</td>\n",
       "      <td>UK 4 - Out of stock,UK 6 - Out of stock,UK 8 -...</td>\n",
       "      <td>ASOS DESIGN long sleeve maxi t-shirt dress in ...</td>\n",
       "      <td>24.00</td>\n",
       "      <td>1444255.0</td>\n",
       "      <td>[{'Product Details': 'Dress by ASOS DESIGN Act...</td>\n",
       "      <td>['https://images.asos-media.com/products/asos-...</td>\n",
       "      <td>black</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30842</th>\n",
       "      <td>https://www.asos.com/asyou/asyou-layered-t-shi...</td>\n",
       "      <td>ASYOU layered t-shirt dress with focus graphic...</td>\n",
       "      <td>UK 4 - Out of stock,UK 6,UK 8 - Out of stock,U...</td>\n",
       "      <td>ASYOU layered t-shirt dress with focus graphic...</td>\n",
       "      <td>22.99</td>\n",
       "      <td>110783769.0</td>\n",
       "      <td>[{'Product Details': 'Dress by ASYOU Exclusive...</td>\n",
       "      <td>['https://images.asos-media.com/products/asyou...</td>\n",
       "      <td>printed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30843</th>\n",
       "      <td>https://www.asos.com/miss-selfridge/miss-selfr...</td>\n",
       "      <td>Miss Selfridge Petite rib knit frill hem funne...</td>\n",
       "      <td>UK 4 - Out of stock,UK 6 - Out of stock,UK 8 -...</td>\n",
       "      <td>Miss Selfridge Petite rib knit frill hem funne...</td>\n",
       "      <td>32.99</td>\n",
       "      <td>116363729.0</td>\n",
       "      <td>[{'Product Details': 'Petite by Miss Selfridge...</td>\n",
       "      <td>['https://images.asos-media.com/products/miss-...</td>\n",
       "      <td>black</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30844</th>\n",
       "      <td>https://www.asos.com/other-stories/other-stori...</td>\n",
       "      <td>&amp; Other Stories plisse mesh midi dress in blac...</td>\n",
       "      <td>XS - UK 4-6 - Out of stock,S - UK 8-10,M - UK ...</td>\n",
       "      <td>&amp; Other Stories plisse mesh midi dress in blac...</td>\n",
       "      <td>65.00</td>\n",
       "      <td>124159122.0</td>\n",
       "      <td>[{'Product Details': 'Dresses by &amp; Other Stori...</td>\n",
       "      <td>['https://images.asos-media.com/products/other...</td>\n",
       "      <td>printed</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>30827 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                     url  \\\n",
       "0      https://www.asos.com/stradivarius/stradivarius...   \n",
       "1      https://www.asos.com/stradivarius/stradivarius...   \n",
       "2      https://www.asos.com/asos-design/asos-design-l...   \n",
       "3      https://www.asos.com/new-look/new-look-trench-...   \n",
       "4      https://www.asos.com/stradivarius/stradivarius...   \n",
       "...                                                  ...   \n",
       "30840  https://www.asos.com/urban-revivo/urban-revivo...   \n",
       "30841  https://www.asos.com/asos-design/asos-design-l...   \n",
       "30842  https://www.asos.com/asyou/asyou-layered-t-shi...   \n",
       "30843  https://www.asos.com/miss-selfridge/miss-selfr...   \n",
       "30844  https://www.asos.com/other-stories/other-stori...   \n",
       "\n",
       "                                                    name  \\\n",
       "0                          New Look trench coat in camel   \n",
       "1                          New Look trench coat in camel   \n",
       "2                          New Look trench coat in camel   \n",
       "3                          New Look trench coat in camel   \n",
       "4         Stradivarius double breasted wool coat in grey   \n",
       "...                                                  ...   \n",
       "30840  Urban Revivo square neck mini dress in floral ...   \n",
       "30841  ASOS DESIGN long sleeve maxi t-shirt dress in ...   \n",
       "30842  ASYOU layered t-shirt dress with focus graphic...   \n",
       "30843  Miss Selfridge Petite rib knit frill hem funne...   \n",
       "30844  & Other Stories plisse mesh midi dress in blac...   \n",
       "\n",
       "                                                    size  \\\n",
       "0      UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...   \n",
       "1      UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...   \n",
       "2      UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...   \n",
       "3      UK 4,UK 6,UK 8,UK 10,UK 12,UK 14 - Out of stoc...   \n",
       "4      XS - UK 6,S - UK 8,M - UK 10,L - UK 12,XL - UK 14   \n",
       "...                                                  ...   \n",
       "30840  XS - UK 6 - Out of stock,S - UK 8 - Out of sto...   \n",
       "30841  UK 4 - Out of stock,UK 6 - Out of stock,UK 8 -...   \n",
       "30842  UK 4 - Out of stock,UK 6,UK 8 - Out of stock,U...   \n",
       "30843  UK 4 - Out of stock,UK 6 - Out of stock,UK 8 -...   \n",
       "30844  XS - UK 4-6 - Out of stock,S - UK 8-10,M - UK ...   \n",
       "\n",
       "                                                category  price          sku  \\\n",
       "0                          New Look trench coat in camel  49.99  126704571.0   \n",
       "1                          New Look trench coat in camel  49.99  126704571.0   \n",
       "2                          New Look trench coat in camel  49.99  126704571.0   \n",
       "3                          New Look trench coat in camel  49.99  126704571.0   \n",
       "4         Stradivarius double breasted wool coat in grey  59.99  123650194.0   \n",
       "...                                                  ...    ...          ...   \n",
       "30840  Urban Revivo square neck mini dress in floral ...  44.00  116745746.0   \n",
       "30841  ASOS DESIGN long sleeve maxi t-shirt dress in ...  24.00    1444255.0   \n",
       "30842  ASYOU layered t-shirt dress with focus graphic...  22.99  110783769.0   \n",
       "30843  Miss Selfridge Petite rib knit frill hem funne...  32.99  116363729.0   \n",
       "30844  & Other Stories plisse mesh midi dress in blac...  65.00  124159122.0   \n",
       "\n",
       "                                             description  \\\n",
       "0      [{'Product Details': 'Coats & Jackets by New L...   \n",
       "1      [{'Product Details': 'Coats & Jackets by New L...   \n",
       "2      [{'Product Details': 'Coats & Jackets by New L...   \n",
       "3      [{'Product Details': 'Coats & Jackets by New L...   \n",
       "4      [{'Product Details': 'Coats & Jackets by Strad...   \n",
       "...                                                  ...   \n",
       "30840  [{'Product Details': 'Mini dress by Urban Revi...   \n",
       "30841  [{'Product Details': 'Dress by ASOS DESIGN Act...   \n",
       "30842  [{'Product Details': 'Dress by ASYOU Exclusive...   \n",
       "30843  [{'Product Details': 'Petite by Miss Selfridge...   \n",
       "30844  [{'Product Details': 'Dresses by & Other Stori...   \n",
       "\n",
       "                                                  images basic_color  \n",
       "0      ['https://images.asos-media.com/products/new-l...     neutral  \n",
       "1      ['https://images.asos-media.com/products/new-l...     neutral  \n",
       "2      ['https://images.asos-media.com/products/new-l...     neutral  \n",
       "3      ['https://images.asos-media.com/products/new-l...     neutral  \n",
       "4      ['https://images.asos-media.com/products/strad...        grey  \n",
       "...                                                  ...         ...  \n",
       "30840  ['https://images.asos-media.com/products/urban...     printed  \n",
       "30841  ['https://images.asos-media.com/products/asos-...       black  \n",
       "30842  ['https://images.asos-media.com/products/asyou...     printed  \n",
       "30843  ['https://images.asos-media.com/products/miss-...       black  \n",
       "30844  ['https://images.asos-media.com/products/other...     printed  \n",
       "\n",
       "[30827 rows x 9 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asos_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fbd73bcf-671c-4742-bbe0-f965ce87bd58",
   "metadata": {},
   "outputs": [],
   "source": [
    "asos_df['price'] = asos_df['price'].replace({'€': '', ',': '.', 'From': '', '[^\\d\\.]+': ''}, regex=True).astype(float)\n",
    "\n",
    "asos_df['price'] = pd.to_numeric(asos_df['price'], errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e6aa3d94-9074-4178-a473-ee12c9df8594",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asos_df['price'].dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "52bd01d8-7f47-4ab5-93e0-4cae99006733",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_asos_df = asos_df[\"price\"].mean().round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "58b1db5d-2dfc-49f6-948f-9f820f860b7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "asos_df.to_csv(\"Asos.csv\", index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "318d7ffd-653c-40f3-bed6-fa1f1d299e19",
   "metadata": {},
   "source": [
    "## H&M"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e4accccc-8347-4064-a083-e4344596c732",
   "metadata": {},
   "outputs": [],
   "source": [
    "HM = pd.read_csv(\"HM_articles.csv\")\n",
    "HM4 = pd.read_csv(\"HM_transactions_train.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9ab4c950-16ce-4588-a753-d49f022db1e7",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>article_id</th>\n",
       "      <th>section_name</th>\n",
       "      <th>detail_desc</th>\n",
       "      <th>price€</th>\n",
       "      <th>product_name</th>\n",
       "      <th>category</th>\n",
       "      <th>color</th>\n",
       "      <th>brand</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>108775015</td>\n",
       "      <td>Womens Everyday Basics</td>\n",
       "      <td>Jersey top with narrow shoulder straps.</td>\n",
       "      <td>8.457627</td>\n",
       "      <td>Jersey Basic</td>\n",
       "      <td>Vest top</td>\n",
       "      <td>Black</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>108775015</td>\n",
       "      <td>Womens Everyday Basics</td>\n",
       "      <td>Jersey top with narrow shoulder straps.</td>\n",
       "      <td>8.457627</td>\n",
       "      <td>Jersey Basic</td>\n",
       "      <td>Vest top</td>\n",
       "      <td>Black</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>108775015</td>\n",
       "      <td>Womens Everyday Basics</td>\n",
       "      <td>Jersey top with narrow shoulder straps.</td>\n",
       "      <td>8.457627</td>\n",
       "      <td>Jersey Basic</td>\n",
       "      <td>Vest top</td>\n",
       "      <td>Black</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>108775015</td>\n",
       "      <td>Womens Everyday Basics</td>\n",
       "      <td>Jersey top with narrow shoulder straps.</td>\n",
       "      <td>8.457627</td>\n",
       "      <td>Jersey Basic</td>\n",
       "      <td>Vest top</td>\n",
       "      <td>Black</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>108775015</td>\n",
       "      <td>Womens Everyday Basics</td>\n",
       "      <td>Jersey top with narrow shoulder straps.</td>\n",
       "      <td>8.457627</td>\n",
       "      <td>Jersey Basic</td>\n",
       "      <td>Vest top</td>\n",
       "      <td>Black</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>63175</th>\n",
       "      <td>944506001</td>\n",
       "      <td>Womens Nightwear, Socks &amp; Tigh</td>\n",
       "      <td>Hoodie in organic cotton sweatshirt fabric wit...</td>\n",
       "      <td>42.355932</td>\n",
       "      <td>Under-, Nightwear</td>\n",
       "      <td>Bra</td>\n",
       "      <td>Blue</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>63176</th>\n",
       "      <td>946748003</td>\n",
       "      <td>Womens Everyday Collection</td>\n",
       "      <td>Top in soft sweatshirt fabric made from a cott...</td>\n",
       "      <td>25.406780</td>\n",
       "      <td>Jersey Fancy</td>\n",
       "      <td>Sweater</td>\n",
       "      <td>Light Grey</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>63177</th>\n",
       "      <td>946748004</td>\n",
       "      <td>Womens Everyday Collection</td>\n",
       "      <td>Top in soft sweatshirt fabric made from a cott...</td>\n",
       "      <td>25.406780</td>\n",
       "      <td>Jersey Fancy</td>\n",
       "      <td>Sweater</td>\n",
       "      <td>Light Pink</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>63178</th>\n",
       "      <td>946748004</td>\n",
       "      <td>Womens Everyday Collection</td>\n",
       "      <td>Top in soft sweatshirt fabric made from a cott...</td>\n",
       "      <td>25.406780</td>\n",
       "      <td>Jersey Fancy</td>\n",
       "      <td>Sweater</td>\n",
       "      <td>Light Pink</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>63179</th>\n",
       "      <td>946748004</td>\n",
       "      <td>Womens Everyday Collection</td>\n",
       "      <td>Top in soft sweatshirt fabric made from a cott...</td>\n",
       "      <td>25.406780</td>\n",
       "      <td>Jersey Fancy</td>\n",
       "      <td>Sweater</td>\n",
       "      <td>Light Pink</td>\n",
       "      <td>H&amp;M</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>63180 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       article_id                    section_name  \\\n",
       "0       108775015          Womens Everyday Basics   \n",
       "1       108775015          Womens Everyday Basics   \n",
       "2       108775015          Womens Everyday Basics   \n",
       "3       108775015          Womens Everyday Basics   \n",
       "4       108775015          Womens Everyday Basics   \n",
       "...           ...                             ...   \n",
       "63175   944506001  Womens Nightwear, Socks & Tigh   \n",
       "63176   946748003      Womens Everyday Collection   \n",
       "63177   946748004      Womens Everyday Collection   \n",
       "63178   946748004      Womens Everyday Collection   \n",
       "63179   946748004      Womens Everyday Collection   \n",
       "\n",
       "                                             detail_desc     price€  \\\n",
       "0                Jersey top with narrow shoulder straps.   8.457627   \n",
       "1                Jersey top with narrow shoulder straps.   8.457627   \n",
       "2                Jersey top with narrow shoulder straps.   8.457627   \n",
       "3                Jersey top with narrow shoulder straps.   8.457627   \n",
       "4                Jersey top with narrow shoulder straps.   8.457627   \n",
       "...                                                  ...        ...   \n",
       "63175  Hoodie in organic cotton sweatshirt fabric wit...  42.355932   \n",
       "63176  Top in soft sweatshirt fabric made from a cott...  25.406780   \n",
       "63177  Top in soft sweatshirt fabric made from a cott...  25.406780   \n",
       "63178  Top in soft sweatshirt fabric made from a cott...  25.406780   \n",
       "63179  Top in soft sweatshirt fabric made from a cott...  25.406780   \n",
       "\n",
       "            product_name  category       color brand  \n",
       "0           Jersey Basic  Vest top       Black   H&M  \n",
       "1           Jersey Basic  Vest top       Black   H&M  \n",
       "2           Jersey Basic  Vest top       Black   H&M  \n",
       "3           Jersey Basic  Vest top       Black   H&M  \n",
       "4           Jersey Basic  Vest top       Black   H&M  \n",
       "...                  ...       ...         ...   ...  \n",
       "63175  Under-, Nightwear       Bra        Blue   H&M  \n",
       "63176       Jersey Fancy   Sweater  Light Grey   H&M  \n",
       "63177       Jersey Fancy   Sweater  Light Pink   H&M  \n",
       "63178       Jersey Fancy   Sweater  Light Pink   H&M  \n",
       "63179       Jersey Fancy   Sweater  Light Pink   H&M  \n",
       "\n",
       "[63180 rows x 8 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "HM_df = pd.merge(HM, HM4, on='article_id', how='inner')\n",
    "HM_df['price€'] = HM_df['price'] * 1000\n",
    "HM_df = HM_df.drop(columns=[\"price\", \"prod_name\", \"product_code\", \"product_type_no\", \"product_group_name\", \"graphical_appearance_no\", \"graphical_appearance_name\", \"colour_group_code\", \"perceived_colour_value_id\", \"perceived_colour_value_name\", \"perceived_colour_master_id\", \"perceived_colour_master_name\", \"department_no\", \"department_name\", \"index_code\", \"index_name\", \"index_group_no\", \"index_group_name\", \"section_no\", \"garment_group_no\", \"t_dat\", \"customer_id\", \"sales_channel_id\", \"month\", \"year\"])\n",
    "HM_df[\"product_name\"] = HM_df[\"garment_group_name\"]\n",
    "HM_df[\"category\"] = HM_df[\"product_type_name\"]\n",
    "HM_df[\"color\"] = HM_df[\"colour_group_name\"]\n",
    "HM_df = HM_df.drop(columns=[\"product_type_name\", \"colour_group_name\", \"garment_group_name\"])\n",
    "HM_df['brand'] = 'H&M'\n",
    "HM_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8426f37b-c5f2-45ea-b66c-5ffae6538d11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "HM_df[\"price€\"].dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "14ce8765-f094-4ff2-93d4-e27857f96db4",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_HM_df = HM_df[\"price€\"].mean().round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c56371f2-b798-4de4-b122-e0751bdcca1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "HM_df.to_csv('H&M.csv', index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c029dde-0ffb-422c-ad8f-99def2451a45",
   "metadata": {},
   "source": [
    "## MANGO"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "89a03831-640e-4249-adb5-e71bcb4c2686",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>brand</th>\n",
       "      <th>url</th>\n",
       "      <th>sku</th>\n",
       "      <th>name</th>\n",
       "      <th>description</th>\n",
       "      <th>price</th>\n",
       "      <th>currency</th>\n",
       "      <th>category</th>\n",
       "      <th>images</th>\n",
       "      <th>scraped_at</th>\n",
       "      <th>terms</th>\n",
       "      <th>section</th>\n",
       "      <th>image_downloads</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/jackets-and-su...</td>\n",
       "      <td>67050682</td>\n",
       "      <td>chaqueta lana cinturón</td>\n",
       "      <td>wool mix fabric, straight design, crossover de...</td>\n",
       "      <td>69.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>chaquetas y americanas</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T6/fot...</td>\n",
       "      <td>2024-02-21T12:51:19.171380</td>\n",
       "      <td>jackets</td>\n",
       "      <td>H</td>\n",
       "      <td>['db68f55d-92f1-43e5-b038-f1708dd75daf', '0c1c...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/jackets-and-su...</td>\n",
       "      <td>67044062</td>\n",
       "      <td>chaqueta punto botones</td>\n",
       "      <td>cotton-blend fabric, medium knit, straight des...</td>\n",
       "      <td>49.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>chaquetas y americanas</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T6/fot...</td>\n",
       "      <td>2024-02-21T12:51:30.009099</td>\n",
       "      <td>jackets</td>\n",
       "      <td>H</td>\n",
       "      <td>['3f64f51b-d437-4ae8-89f5-7da1adcb4f4e', 'aee6...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/jackets-and-su...</td>\n",
       "      <td>67074074</td>\n",
       "      <td>chaqueta tweed detalle contraste</td>\n",
       "      <td>tweed fabric, cotton-blend fabric, straight de...</td>\n",
       "      <td>69.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>chaquetas y americanas</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T6/fot...</td>\n",
       "      <td>2024-02-21T12:51:31.719633</td>\n",
       "      <td>jackets</td>\n",
       "      <td>H</td>\n",
       "      <td>['76c2fa43-be2b-4d5a-b6a8-04900e32335c', '873f...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/jackets-and-su...</td>\n",
       "      <td>57035980</td>\n",
       "      <td>cazadora vaquera cordón ajustable</td>\n",
       "      <td>denim style cotton fabric, 100% cotton fabric,...</td>\n",
       "      <td>29.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>chaquetas y americanas</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T5/fot...</td>\n",
       "      <td>2024-02-21T12:51:32.478754</td>\n",
       "      <td>jackets</td>\n",
       "      <td>H</td>\n",
       "      <td>['512ab173-7474-4d2a-8597-5a73429f3ff6', '0d49...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/jackets-and-su...</td>\n",
       "      <td>57068270</td>\n",
       "      <td>chaqueta acolchada denim</td>\n",
       "      <td>denim style cotton fabric, straight design, ro...</td>\n",
       "      <td>34.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>chaquetas y americanas</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T5/fot...</td>\n",
       "      <td>2024-02-21T12:51:33.032029</td>\n",
       "      <td>jackets</td>\n",
       "      <td>H</td>\n",
       "      <td>['622ffabe-2e0e-4f4a-a98f-61a774704501', '73dd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2023</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/hats-and-caps/...</td>\n",
       "      <td>57055786</td>\n",
       "      <td>gorro punto cashmere</td>\n",
       "      <td>selection collection, cashmere fabric, recycle...</td>\n",
       "      <td>22.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>sombreros y gorras</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T5/fot...</td>\n",
       "      <td>2024-02-21T13:05:48.557874</td>\n",
       "      <td>knitwear</td>\n",
       "      <td>M,S,I,T,V</td>\n",
       "      <td>['b9c36fd4-9df6-43b7-873c-15864c1ee2dc', '09ea...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2024</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/more-accessori...</td>\n",
       "      <td>67040259</td>\n",
       "      <td>calcetines largos canalé</td>\n",
       "      <td>cotton-blend fabric, long design, cable knit d...</td>\n",
       "      <td>12.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>mas accesorios</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T6/fot...</td>\n",
       "      <td>2024-02-21T13:05:48.770103</td>\n",
       "      <td>knitwear</td>\n",
       "      <td>M,S,I,T,V</td>\n",
       "      <td>['b21e584b-74d0-4cf1-bfa6-79fe5d6e630a', '37e3...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2025</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/shirts-shirts/...</td>\n",
       "      <td>67064012</td>\n",
       "      <td>camisa punto algodón</td>\n",
       "      <td>cotton-blend fabric, fine knit fabric, straigh...</td>\n",
       "      <td>18.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>camisas</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T6/fot...</td>\n",
       "      <td>2024-02-21T13:05:48.998161</td>\n",
       "      <td>knitwear</td>\n",
       "      <td>M,S,I,T,V</td>\n",
       "      <td>['3c1ca171-adfe-4905-a93b-cecbbc40e430', 'cfee...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2026</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/more-accessori...</td>\n",
       "      <td>67062009</td>\n",
       "      <td>calcetines canalé</td>\n",
       "      <td>wool mix fabric, cable knit fabric</td>\n",
       "      <td>12.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>mas accesorios</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T6/fot...</td>\n",
       "      <td>2024-02-21T13:05:49.339167</td>\n",
       "      <td>knitwear</td>\n",
       "      <td>M,S,I,T,V</td>\n",
       "      <td>['23aa238b-58d4-4d33-9c38-881bee6942a4', 'a9e6...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2027</th>\n",
       "      <td>Mango</td>\n",
       "      <td>https://shop.mango.com/fi/women/shirts-shirts/...</td>\n",
       "      <td>57075809</td>\n",
       "      <td>camisa punto canalé</td>\n",
       "      <td>cable knit fabric, fine knit fabric, shirt-sty...</td>\n",
       "      <td>15.99</td>\n",
       "      <td>EUR</td>\n",
       "      <td>camisas</td>\n",
       "      <td>['https://st.mngbcn.com/rcs/pics/static/T5/fot...</td>\n",
       "      <td>2024-02-21T13:05:49.560565</td>\n",
       "      <td>knitwear</td>\n",
       "      <td>M,S,I,T,V</td>\n",
       "      <td>['9ca94b0e-49ee-4922-b896-e3c691eced7b', '9605...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2028 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      brand                                                url       sku  \\\n",
       "0     Mango  https://shop.mango.com/fi/women/jackets-and-su...  67050682   \n",
       "1     Mango  https://shop.mango.com/fi/women/jackets-and-su...  67044062   \n",
       "2     Mango  https://shop.mango.com/fi/women/jackets-and-su...  67074074   \n",
       "3     Mango  https://shop.mango.com/fi/women/jackets-and-su...  57035980   \n",
       "4     Mango  https://shop.mango.com/fi/women/jackets-and-su...  57068270   \n",
       "...     ...                                                ...       ...   \n",
       "2023  Mango  https://shop.mango.com/fi/women/hats-and-caps/...  57055786   \n",
       "2024  Mango  https://shop.mango.com/fi/women/more-accessori...  67040259   \n",
       "2025  Mango  https://shop.mango.com/fi/women/shirts-shirts/...  67064012   \n",
       "2026  Mango  https://shop.mango.com/fi/women/more-accessori...  67062009   \n",
       "2027  Mango  https://shop.mango.com/fi/women/shirts-shirts/...  57075809   \n",
       "\n",
       "                                   name  \\\n",
       "0                chaqueta lana cinturón   \n",
       "1                chaqueta punto botones   \n",
       "2      chaqueta tweed detalle contraste   \n",
       "3     cazadora vaquera cordón ajustable   \n",
       "4              chaqueta acolchada denim   \n",
       "...                                 ...   \n",
       "2023               gorro punto cashmere   \n",
       "2024           calcetines largos canalé   \n",
       "2025               camisa punto algodón   \n",
       "2026                  calcetines canalé   \n",
       "2027                camisa punto canalé   \n",
       "\n",
       "                                            description  price currency  \\\n",
       "0     wool mix fabric, straight design, crossover de...  69.99      EUR   \n",
       "1     cotton-blend fabric, medium knit, straight des...  49.99      EUR   \n",
       "2     tweed fabric, cotton-blend fabric, straight de...  69.99      EUR   \n",
       "3     denim style cotton fabric, 100% cotton fabric,...  29.99      EUR   \n",
       "4     denim style cotton fabric, straight design, ro...  34.99      EUR   \n",
       "...                                                 ...    ...      ...   \n",
       "2023  selection collection, cashmere fabric, recycle...  22.99      EUR   \n",
       "2024  cotton-blend fabric, long design, cable knit d...  12.99      EUR   \n",
       "2025  cotton-blend fabric, fine knit fabric, straigh...  18.99      EUR   \n",
       "2026                 wool mix fabric, cable knit fabric  12.99      EUR   \n",
       "2027  cable knit fabric, fine knit fabric, shirt-sty...  15.99      EUR   \n",
       "\n",
       "                    category  \\\n",
       "0     chaquetas y americanas   \n",
       "1     chaquetas y americanas   \n",
       "2     chaquetas y americanas   \n",
       "3     chaquetas y americanas   \n",
       "4     chaquetas y americanas   \n",
       "...                      ...   \n",
       "2023      sombreros y gorras   \n",
       "2024          mas accesorios   \n",
       "2025                 camisas   \n",
       "2026          mas accesorios   \n",
       "2027                 camisas   \n",
       "\n",
       "                                                 images  \\\n",
       "0     ['https://st.mngbcn.com/rcs/pics/static/T6/fot...   \n",
       "1     ['https://st.mngbcn.com/rcs/pics/static/T6/fot...   \n",
       "2     ['https://st.mngbcn.com/rcs/pics/static/T6/fot...   \n",
       "3     ['https://st.mngbcn.com/rcs/pics/static/T5/fot...   \n",
       "4     ['https://st.mngbcn.com/rcs/pics/static/T5/fot...   \n",
       "...                                                 ...   \n",
       "2023  ['https://st.mngbcn.com/rcs/pics/static/T5/fot...   \n",
       "2024  ['https://st.mngbcn.com/rcs/pics/static/T6/fot...   \n",
       "2025  ['https://st.mngbcn.com/rcs/pics/static/T6/fot...   \n",
       "2026  ['https://st.mngbcn.com/rcs/pics/static/T6/fot...   \n",
       "2027  ['https://st.mngbcn.com/rcs/pics/static/T5/fot...   \n",
       "\n",
       "                      scraped_at     terms    section  \\\n",
       "0     2024-02-21T12:51:19.171380   jackets          H   \n",
       "1     2024-02-21T12:51:30.009099   jackets          H   \n",
       "2     2024-02-21T12:51:31.719633   jackets          H   \n",
       "3     2024-02-21T12:51:32.478754   jackets          H   \n",
       "4     2024-02-21T12:51:33.032029   jackets          H   \n",
       "...                          ...       ...        ...   \n",
       "2023  2024-02-21T13:05:48.557874  knitwear  M,S,I,T,V   \n",
       "2024  2024-02-21T13:05:48.770103  knitwear  M,S,I,T,V   \n",
       "2025  2024-02-21T13:05:48.998161  knitwear  M,S,I,T,V   \n",
       "2026  2024-02-21T13:05:49.339167  knitwear  M,S,I,T,V   \n",
       "2027  2024-02-21T13:05:49.560565  knitwear  M,S,I,T,V   \n",
       "\n",
       "                                        image_downloads  \n",
       "0     ['db68f55d-92f1-43e5-b038-f1708dd75daf', '0c1c...  \n",
       "1     ['3f64f51b-d437-4ae8-89f5-7da1adcb4f4e', 'aee6...  \n",
       "2     ['76c2fa43-be2b-4d5a-b6a8-04900e32335c', '873f...  \n",
       "3     ['512ab173-7474-4d2a-8597-5a73429f3ff6', '0d49...  \n",
       "4     ['622ffabe-2e0e-4f4a-a98f-61a774704501', '73dd...  \n",
       "...                                                 ...  \n",
       "2023  ['b9c36fd4-9df6-43b7-873c-15864c1ee2dc', '09ea...  \n",
       "2024  ['b21e584b-74d0-4cf1-bfa6-79fe5d6e630a', '37e3...  \n",
       "2025  ['3c1ca171-adfe-4905-a93b-cecbbc40e430', 'cfee...  \n",
       "2026  ['23aa238b-58d4-4d33-9c38-881bee6942a4', 'a9e6...  \n",
       "2027  ['9ca94b0e-49ee-4922-b896-e3c691eced7b', '9605...  \n",
       "\n",
       "[2028 rows x 13 columns]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mango_df = pd.read_csv(\"store_mango.csv\")\n",
    "mango_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "981e46f7-27d5-4c54-ac43-0e5a5ef03e80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mango_df[\"price\"].dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "df30544f-61bf-4efd-8b7c-122785f8f352",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_mango_df = mango_df[\"price\"].mean().round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "8038f183-13d2-4d28-9267-cd6f58b9c81e",
   "metadata": {},
   "outputs": [],
   "source": [
    "mango_df.to_csv(\"Mango.csv\", index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "edf7b3b7-48c6-4cf0-a36c-52e101d4b0af",
   "metadata": {},
   "source": [
    "## ZARA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "55f40e63-439d-4840-bab5-c2363e95fb48",
   "metadata": {
    "scrolled": True
   },
   "outputs": [],
   "source": [
    "zara_df = pd.read_csv(\"zara.csv\", delimiter=',')\n",
    "zara_df = zara_df.dropna(subset=['description'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b96e5dcf-c4db-4821-b8b5-751d1b380b97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zara_df[\"price€\"].dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5b5725bd-0d86-4bb8-8667-40998a37e3e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_zara_df = zara_df[\"price€\"].mean().round(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "32b3496e-fffb-43e8-ad41-d1fe64eceaf2",
   "metadata": {},
   "outputs": [],
   "source": [
    "zara_df.to_csv(\"Zara.csv\", index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b53992e6-6fac-477d-b4c8-4388781db6b4",
   "metadata": {},
   "source": [
    "## MASSIMO DUTI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "6320653a-6d78-4c15-bc6f-63c066081ab8",
   "metadata": {
    "scrolled": True
   },
   "outputs": [],
   "source": [
    "massimo_dutti_df = pd.read_csv(\"massimo_dutti.csv\")\n",
    "massimo_dutti_df['price'] = massimo_dutti_df['price'].replace({'€': '', ',': '.'}, regex=True).astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9deb28b4-af17-45bf-b655-8deed32b71a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>url</th>\n",
       "      <th>price</th>\n",
       "      <th>name</th>\n",
       "      <th>section</th>\n",
       "      <th>category</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://www.massimodutti.com/es/jeans-slim-fit...</td>\n",
       "      <td>49.95</td>\n",
       "      <td>JEANS SLIM FIT</td>\n",
       "      <td>woman</td>\n",
       "      <td>JEANS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://www.massimodutti.com/es/jeans-slim-fit...</td>\n",
       "      <td>49.95</td>\n",
       "      <td>JEANS SLIM FIT MEZCLA ALGODÓN</td>\n",
       "      <td>woman</td>\n",
       "      <td>JEANS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://www.massimodutti.com/es/jeans-slim-fit...</td>\n",
       "      <td>49.95</td>\n",
       "      <td>JEANS SLIM FIT</td>\n",
       "      <td>woman</td>\n",
       "      <td>JEANS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://www.massimodutti.com/es/jeans-slim-fit...</td>\n",
       "      <td>49.95</td>\n",
       "      <td>JEANS SLIM FIT</td>\n",
       "      <td>woman</td>\n",
       "      <td>JEANS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://www.massimodutti.com/es/jeans-mezcla-a...</td>\n",
       "      <td>49.95</td>\n",
       "      <td>JEANS MEZCLA ALGODÓN SLIM FIT</td>\n",
       "      <td>woman</td>\n",
       "      <td>JEANS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2151</th>\n",
       "      <td>https://www.massimodutti.com/es/americana-mezc...</td>\n",
       "      <td>129.00</td>\n",
       "      <td>AMERICANA MEZCLA ALGODÓN\\n+1\\n\\n\\n-35% *</td>\n",
       "      <td>man</td>\n",
       "      <td>AMERICANA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2152</th>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-de...</td>\n",
       "      <td>89.95</td>\n",
       "      <td>SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...</td>\n",
       "      <td>man</td>\n",
       "      <td>SOBRECAMISA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2153</th>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-de...</td>\n",
       "      <td>89.95</td>\n",
       "      <td>SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...</td>\n",
       "      <td>man</td>\n",
       "      <td>SOBRECAMISA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2154</th>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-po...</td>\n",
       "      <td>69.95</td>\n",
       "      <td>SOBRECAMISA POPELÍN DETALLE BOLSILLOS\\n+1\\n\\n\\...</td>\n",
       "      <td>man</td>\n",
       "      <td>SOBRECAMISA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2155</th>\n",
       "      <td>https://www.massimodutti.com/es/chaqueta-100-a...</td>\n",
       "      <td>129.00</td>\n",
       "      <td>CHAQUETA 100% ALGODÓN BOLSILLOS\\n\\n\\n-50% *</td>\n",
       "      <td>man</td>\n",
       "      <td>CHAQUETA</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2156 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    url   price  \\\n",
       "0     https://www.massimodutti.com/es/jeans-slim-fit...   49.95   \n",
       "1     https://www.massimodutti.com/es/jeans-slim-fit...   49.95   \n",
       "2     https://www.massimodutti.com/es/jeans-slim-fit...   49.95   \n",
       "3     https://www.massimodutti.com/es/jeans-slim-fit...   49.95   \n",
       "4     https://www.massimodutti.com/es/jeans-mezcla-a...   49.95   \n",
       "...                                                 ...     ...   \n",
       "2151  https://www.massimodutti.com/es/americana-mezc...  129.00   \n",
       "2152  https://www.massimodutti.com/es/sobrecamisa-de...   89.95   \n",
       "2153  https://www.massimodutti.com/es/sobrecamisa-de...   89.95   \n",
       "2154  https://www.massimodutti.com/es/sobrecamisa-po...   69.95   \n",
       "2155  https://www.massimodutti.com/es/chaqueta-100-a...  129.00   \n",
       "\n",
       "                                                   name section     category  \n",
       "0                                        JEANS SLIM FIT   woman        JEANS  \n",
       "1                         JEANS SLIM FIT MEZCLA ALGODÓN   woman        JEANS  \n",
       "2                                        JEANS SLIM FIT   woman        JEANS  \n",
       "3                                        JEANS SLIM FIT   woman        JEANS  \n",
       "4                         JEANS MEZCLA ALGODÓN SLIM FIT   woman        JEANS  \n",
       "...                                                 ...     ...          ...  \n",
       "2151           AMERICANA MEZCLA ALGODÓN\\n+1\\n\\n\\n-35% *     man    AMERICANA  \n",
       "2152  SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...     man  SOBRECAMISA  \n",
       "2153  SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...     man  SOBRECAMISA  \n",
       "2154  SOBRECAMISA POPELÍN DETALLE BOLSILLOS\\n+1\\n\\n\\...     man  SOBRECAMISA  \n",
       "2155        CHAQUETA 100% ALGODÓN BOLSILLOS\\n\\n\\n-50% *     man     CHAQUETA  \n",
       "\n",
       "[2156 rows x 5 columns]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "massimo_dutti_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d7db062e-9926-4f79-ac39-4448661fb9d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "massimo_dutti_df[\"price\"].dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "ddb0b121-af29-408e-8957-c71d45b6394a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "96.88"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_massimo_dutti_df = massimo_dutti_df['price'].mean().round(2)\n",
    "mean_massimo_dutti_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "445c2482-3076-4e1d-8f05-e854a70d4c0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "massimo_dutti_df.to_csv(\"massimo_dutti.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "f70f5bc8-66b9-4e39-a564-f1375a3935e7",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>department_name</th>\n",
       "      <th>category_name</th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_name</th>\n",
       "      <th>titled_brands</th>\n",
       "      <th>retail_price</th>\n",
       "      <th>current_price</th>\n",
       "      <th>url</th>\n",
       "      <th>listing_url</th>\n",
       "      <th>name</th>\n",
       "      <th>...</th>\n",
       "      <th>detail_desc</th>\n",
       "      <th>price€</th>\n",
       "      <th>color</th>\n",
       "      <th>brand</th>\n",
       "      <th>section</th>\n",
       "      <th>Product ID</th>\n",
       "      <th>Promotion</th>\n",
       "      <th>Product Category</th>\n",
       "      <th>Seasonal</th>\n",
       "      <th>Sales Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>BB550LSB</td>\n",
       "      <td>New Balance BB550 - Men's</td>\n",
       "      <td>New Balance</td>\n",
       "      <td>110.0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/BB550LSB....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>37758401</td>\n",
       "      <td>PUMA MB2 x Slime - Men's</td>\n",
       "      <td>PUMA</td>\n",
       "      <td>140.0</td>\n",
       "      <td>140.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/37758401....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>M990GL6</td>\n",
       "      <td>New Balance 990V6 D - Men's</td>\n",
       "      <td>New Balance</td>\n",
       "      <td>200.0</td>\n",
       "      <td>200.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/M990GL6.html</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>W2288111</td>\n",
       "      <td>Nike Air Force 1 '07 LE - Men's</td>\n",
       "      <td>Nike</td>\n",
       "      <td>110.0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/W2288111....</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Men's</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>5950CHE</td>\n",
       "      <td>UGG Tasman - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>110.0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>https://www.footlocker.com/product/~/5950CHE.html</td>\n",
       "      <td>https://www.footlocker.com/category/mens/shoes...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101445</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://www.massimodutti.com/es/americana-mezc...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>AMERICANA MEZCLA ALGODÓN\\n+1\\n\\n\\n-35% *</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>man</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101446</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-de...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>man</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101447</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-de...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>man</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101448</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-po...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>SOBRECAMISA POPELÍN DETALLE BOLSILLOS\\n+1\\n\\n\\...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>man</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101449</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://www.massimodutti.com/es/chaqueta-100-a...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>CHAQUETA 100% ALGODÓN BOLSILLOS\\n\\n\\n-50% *</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>man</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>101450 rows × 27 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       department_name category_name product_id  \\\n",
       "0                Men's         Shoes   BB550LSB   \n",
       "1                Men's         Shoes   37758401   \n",
       "2                Men's         Shoes    M990GL6   \n",
       "3                Men's         Shoes   W2288111   \n",
       "4                Men's         Shoes    5950CHE   \n",
       "...                ...           ...        ...   \n",
       "101445             NaN           NaN        NaN   \n",
       "101446             NaN           NaN        NaN   \n",
       "101447             NaN           NaN        NaN   \n",
       "101448             NaN           NaN        NaN   \n",
       "101449             NaN           NaN        NaN   \n",
       "\n",
       "                           product_name titled_brands  retail_price  \\\n",
       "0             New Balance BB550 - Men's   New Balance         110.0   \n",
       "1              PUMA MB2 x Slime - Men's          PUMA         140.0   \n",
       "2           New Balance 990V6 D - Men's   New Balance         200.0   \n",
       "3       Nike Air Force 1 '07 LE - Men's          Nike         110.0   \n",
       "4                    UGG Tasman - Men's           UGG         110.0   \n",
       "...                                 ...           ...           ...   \n",
       "101445                              NaN           NaN           NaN   \n",
       "101446                              NaN           NaN           NaN   \n",
       "101447                              NaN           NaN           NaN   \n",
       "101448                              NaN           NaN           NaN   \n",
       "101449                              NaN           NaN           NaN   \n",
       "\n",
       "        current_price                                                url  \\\n",
       "0               110.0  https://www.footlocker.com/product/~/BB550LSB....   \n",
       "1               140.0  https://www.footlocker.com/product/~/37758401....   \n",
       "2               200.0  https://www.footlocker.com/product/~/M990GL6.html   \n",
       "3               110.0  https://www.footlocker.com/product/~/W2288111....   \n",
       "4               110.0  https://www.footlocker.com/product/~/5950CHE.html   \n",
       "...               ...                                                ...   \n",
       "101445            NaN  https://www.massimodutti.com/es/americana-mezc...   \n",
       "101446            NaN  https://www.massimodutti.com/es/sobrecamisa-de...   \n",
       "101447            NaN  https://www.massimodutti.com/es/sobrecamisa-de...   \n",
       "101448            NaN  https://www.massimodutti.com/es/sobrecamisa-po...   \n",
       "101449            NaN  https://www.massimodutti.com/es/chaqueta-100-a...   \n",
       "\n",
       "                                              listing_url  \\\n",
       "0       https://www.footlocker.com/category/mens/shoes...   \n",
       "1       https://www.footlocker.com/category/mens/shoes...   \n",
       "2       https://www.footlocker.com/category/mens/shoes...   \n",
       "3       https://www.footlocker.com/category/mens/shoes...   \n",
       "4       https://www.footlocker.com/category/mens/shoes...   \n",
       "...                                                   ...   \n",
       "101445                                                NaN   \n",
       "101446                                                NaN   \n",
       "101447                                                NaN   \n",
       "101448                                                NaN   \n",
       "101449                                                NaN   \n",
       "\n",
       "                                                     name  ... detail_desc  \\\n",
       "0                                                     NaN  ...         NaN   \n",
       "1                                                     NaN  ...         NaN   \n",
       "2                                                     NaN  ...         NaN   \n",
       "3                                                     NaN  ...         NaN   \n",
       "4                                                     NaN  ...         NaN   \n",
       "...                                                   ...  ...         ...   \n",
       "101445           AMERICANA MEZCLA ALGODÓN\\n+1\\n\\n\\n-35% *  ...         NaN   \n",
       "101446  SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...  ...         NaN   \n",
       "101447  SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...  ...         NaN   \n",
       "101448  SOBRECAMISA POPELÍN DETALLE BOLSILLOS\\n+1\\n\\n\\...  ...         NaN   \n",
       "101449        CHAQUETA 100% ALGODÓN BOLSILLOS\\n\\n\\n-50% *  ...         NaN   \n",
       "\n",
       "       price€  color brand section  Product ID Promotion Product Category  \\\n",
       "0         NaN    NaN   NaN     NaN         NaN       NaN              NaN   \n",
       "1         NaN    NaN   NaN     NaN         NaN       NaN              NaN   \n",
       "2         NaN    NaN   NaN     NaN         NaN       NaN              NaN   \n",
       "3         NaN    NaN   NaN     NaN         NaN       NaN              NaN   \n",
       "4         NaN    NaN   NaN     NaN         NaN       NaN              NaN   \n",
       "...       ...    ...   ...     ...         ...       ...              ...   \n",
       "101445    NaN    NaN   NaN     man         NaN       NaN              NaN   \n",
       "101446    NaN    NaN   NaN     man         NaN       NaN              NaN   \n",
       "101447    NaN    NaN   NaN     man         NaN       NaN              NaN   \n",
       "101448    NaN    NaN   NaN     man         NaN       NaN              NaN   \n",
       "101449    NaN    NaN   NaN     man         NaN       NaN              NaN   \n",
       "\n",
       "        Seasonal Sales Volume  \n",
       "0            NaN          NaN  \n",
       "1            NaN          NaN  \n",
       "2            NaN          NaN  \n",
       "3            NaN          NaN  \n",
       "4            NaN          NaN  \n",
       "...          ...          ...  \n",
       "101445       NaN          NaN  \n",
       "101446       NaN          NaN  \n",
       "101447       NaN          NaN  \n",
       "101448       NaN          NaN  \n",
       "101449       NaN          NaN  \n",
       "\n",
       "[101450 rows x 27 columns]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "brands_df = pd.concat([footlocker_df, asos_df, HM_df, mango_df, zara_df, massimo_dutti_df], ignore_index=True, sort=False)\n",
    "brands_df = brands_df.drop(columns=[\"sub_category_name\", \"best_sell_rank\", \"SCAN_DATE\", \"TID\", \"sku\", \"images\", \"currency\", \"scraped_at\", \"terms\", \"image_downloads\", \"Product Position\"])\n",
    "brands_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f39976dd-af26-457b-83ec-e360c6d0a2ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "brands_df['category_combined'] = (\n",
    "    brands_df['category_name']\n",
    "    .fillna(brands_df['category'])\n",
    "    .fillna(brands_df['Product Category'])\n",
    ")\n",
    "\n",
    "brands_df['price_combined'] = (\n",
    "    brands_df['current_price']\n",
    "    .fillna(brands_df['price'])\n",
    "    .fillna(brands_df['price€'])\n",
    ") \n",
    "\n",
    "brands_df['color_combined'] = (\n",
    "    brands_df['color']\n",
    "    .fillna(brands_df['basic_color'])\n",
    ")\n",
    "\n",
    "brands_df['product_id_combined'] = (\n",
    "    brands_df['product_id']\n",
    "    .fillna(brands_df['Product ID'])\n",
    "    .fillna(brands_df['article_id'])\n",
    ")\n",
    "\n",
    "brands_df['department_combined'] = (\n",
    "    brands_df['department_name']\n",
    "    .fillna(brands_df['section_name'])\n",
    "    .fillna(brands_df['section'])\n",
    ") \n",
    "\n",
    "brands_df['name_combined'] = (\n",
    "    brands_df['product_name']\n",
    "    .fillna(brands_df['name'])\n",
    ") \n",
    "\n",
    "brands_df['brand_combined'] = (\n",
    "    brands_df['titled_brands']\n",
    "    .fillna(brands_df['brand'])\n",
    ")\n",
    "\n",
    "brands_df['url_combined'] = (\n",
    "    brands_df['url']\n",
    "    .fillna(brands_df['listing_url'])\n",
    ")\n",
    "\n",
    "brands_df['description_combined'] = (\n",
    "    brands_df['description']\n",
    "    .fillna(brands_df['detail_desc'])\n",
    ")\n",
    "\n",
    "df_cleaned = brands_df.drop(columns=[\n",
    "    'category_name', 'category', 'Product Category',\n",
    "    'department_name', 'section_name', 'section',\n",
    "    'product_id', 'Product ID', 'article_id',\n",
    "    'current_price', 'price', 'price€',\n",
    "    'product_name', 'name',\n",
    "    'titled_brands', 'brand',\n",
    "    'url', 'listing_url',\n",
    "    'description', 'detail_desc',\n",
    "    'color', 'basic_color',\n",
    "])\n",
    "\n",
    "df_cleaned = df_cleaned.rename(columns={'category_combined': 'category', 'department_combined': 'section', 'product_id_combined': 'product_id', 'price_combined': 'price', 'name_combined': 'name', 'brand_combined': 'brand', 'url_combined': 'url', 'description_combined': 'description', 'color_combined': 'basic_color'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0e1999f1-3c6a-47ce-893c-9d0e3e3bf82c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned = df_cleaned.drop(columns=['retail_price', 'Seasonal', 'Sales Volume'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "eea07e0c-ab0e-42c3-b716-1d3bf26b594c",
   "metadata": {},
   "outputs": [],
   "source": [
    "size_mode = df_cleaned['size'].mode()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "4394df43-5ac5-424a-a120-3db52b25f260",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned['size'] = df_cleaned['size'].fillna(size_mode)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "fdffcd1a-8922-48bb-aa0d-cfe02e67ab7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned['description'] = df_cleaned['description'].fillna('NA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "32fb126c-c360-47b8-a9e1-6d7ad7c476ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned['section'] = df_cleaned['section'].fillna('unknown')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "4528ca86-82e0-4e16-9e67-b36480ef3a4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned['product_id'] = df_cleaned['product_id'].fillna('unknown')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "dc22fcb1-00e9-4873-8cde-1b7aa816edf5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned['brand'] = df_cleaned['brand'].fillna('asos')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "67a3a467-b6ba-4124-8ae9-2a56f33adb76",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned['url'] = df_cleaned['url'].fillna('NA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "c6f170ec-6119-4285-a6b2-afd158444618",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned['Promotion'] = df_cleaned['Promotion'].fillna('No')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f82b5285-5ebb-46e0-86f8-1fd1ad9e31f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "size              0\n",
       "Promotion         0\n",
       "category          0\n",
       "price             0\n",
       "basic_color    7443\n",
       "product_id        0\n",
       "section           0\n",
       "name              0\n",
       "brand             0\n",
       "url               0\n",
       "description       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cleaned.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "b75d5c71-8a60-4d4e-a526-6d93dfbed8ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['size', 'Promotion', 'category', 'price', 'basic_color', 'product_id',\n",
       "       'section', 'name', 'brand', 'url', 'description'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cleaned.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "3fdf7272-b520-47a4-b210-b007cc5a08e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(101450, 11)"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cleaned.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "da9c0124-a347-4dd5-a400-3f0c0dc877fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['size', 'promotion', 'category', 'price', 'basic_color', 'product_id',\n",
       "       'section', 'name', 'brand', 'url', 'description'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cleaned.columns = [col.strip().replace(\" \", \"_\").replace(\".\", \"\").lower() for col in df_cleaned.columns]\n",
    "df_cleaned.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "2d925aac-13ed-45de-a325-9eaf73752019",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cleaned['price'].dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "8c26a4d2-2304-483d-80cd-f4f29a530831",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method Series.mean of 0         110.00\n",
       "1         140.00\n",
       "2         200.00\n",
       "3         110.00\n",
       "4         110.00\n",
       "           ...  \n",
       "101445    129.00\n",
       "101446     89.95\n",
       "101447     89.95\n",
       "101448     69.95\n",
       "101449    129.00\n",
       "Name: price, Length: 101450, dtype: float64>"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cleaned['price'].mean"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e31230d5-b2ea-414b-ab60-938476332ed0",
   "metadata": {},
   "source": [
    "## DF_CLEANED"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "31bf9581-ffd8-473a-8dd0-4853c43d7022",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Man', 'unknown', 'Woman', 'Baby', 'Kids'], dtype=object)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Function to categorize the 'section' values\n",
    "def map_section(value):\n",
    "    if pd.isna(value) or value == 'unknown':\n",
    "        return 'unknown'\n",
    "    elif 'Men' in value or 'MAN' in value or 'H' in value:\n",
    "        return 'Man'\n",
    "    elif 'Women' in value or 'Ladies' in value or 'WOMAN' in value or \"M,S,I,T,V\" in value:\n",
    "        return 'Woman'\n",
    "    elif 'Kids' in value or 'Girl' in value or 'Boy' in value:\n",
    "        return 'Kids'\n",
    "    elif 'Baby' in value or 'Mama' in value:\n",
    "        return 'Baby'\n",
    "    else:\n",
    "        return 'unknown'\n",
    "\n",
    "df_cleaned['section'] = df_cleaned['section'].apply(map_section)\n",
    "\n",
    "df_cleaned['section'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "c8dfee75-8e2a-44ad-a0db-c8a244a3dc49",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cleaned.to_csv('brands.csv', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "94fb57cb-4fbb-4eb0-8451-28966f3a4948",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>size</th>\n",
       "      <th>promotion</th>\n",
       "      <th>category</th>\n",
       "      <th>price</th>\n",
       "      <th>basic_color</th>\n",
       "      <th>product_id</th>\n",
       "      <th>section</th>\n",
       "      <th>name</th>\n",
       "      <th>brand</th>\n",
       "      <th>url</th>\n",
       "      <th>description</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>110.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>BB550LSB</td>\n",
       "      <td>Man</td>\n",
       "      <td>New Balance BB550 - Men's</td>\n",
       "      <td>New Balance</td>\n",
       "      <td>https://www.footlocker.com/product/~/BB550LSB....</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>140.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>37758401</td>\n",
       "      <td>Man</td>\n",
       "      <td>PUMA MB2 x Slime - Men's</td>\n",
       "      <td>PUMA</td>\n",
       "      <td>https://www.footlocker.com/product/~/37758401....</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>200.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>M990GL6</td>\n",
       "      <td>Man</td>\n",
       "      <td>New Balance 990V6 D - Men's</td>\n",
       "      <td>New Balance</td>\n",
       "      <td>https://www.footlocker.com/product/~/M990GL6.html</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>110.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>W2288111</td>\n",
       "      <td>Man</td>\n",
       "      <td>Nike Air Force 1 '07 LE - Men's</td>\n",
       "      <td>Nike</td>\n",
       "      <td>https://www.footlocker.com/product/~/W2288111....</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>110.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5950CHE</td>\n",
       "      <td>Man</td>\n",
       "      <td>UGG Tasman - Men's</td>\n",
       "      <td>UGG</td>\n",
       "      <td>https://www.footlocker.com/product/~/5950CHE.html</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101445</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>AMERICANA</td>\n",
       "      <td>129.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>unknown</td>\n",
       "      <td>unknown</td>\n",
       "      <td>AMERICANA MEZCLA ALGODÓN\\n+1\\n\\n\\n-35% *</td>\n",
       "      <td>asos</td>\n",
       "      <td>https://www.massimodutti.com/es/americana-mezc...</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101446</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>SOBRECAMISA</td>\n",
       "      <td>89.95</td>\n",
       "      <td>NaN</td>\n",
       "      <td>unknown</td>\n",
       "      <td>unknown</td>\n",
       "      <td>SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...</td>\n",
       "      <td>asos</td>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-de...</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101447</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>SOBRECAMISA</td>\n",
       "      <td>89.95</td>\n",
       "      <td>NaN</td>\n",
       "      <td>unknown</td>\n",
       "      <td>unknown</td>\n",
       "      <td>SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...</td>\n",
       "      <td>asos</td>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-de...</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101448</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>SOBRECAMISA</td>\n",
       "      <td>69.95</td>\n",
       "      <td>NaN</td>\n",
       "      <td>unknown</td>\n",
       "      <td>unknown</td>\n",
       "      <td>SOBRECAMISA POPELÍN DETALLE BOLSILLOS\\n+1\\n\\n\\...</td>\n",
       "      <td>asos</td>\n",
       "      <td>https://www.massimodutti.com/es/sobrecamisa-po...</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101449</th>\n",
       "      <td>UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18</td>\n",
       "      <td>No</td>\n",
       "      <td>CHAQUETA</td>\n",
       "      <td>129.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>unknown</td>\n",
       "      <td>unknown</td>\n",
       "      <td>CHAQUETA 100% ALGODÓN BOLSILLOS\\n\\n\\n-50% *</td>\n",
       "      <td>asos</td>\n",
       "      <td>https://www.massimodutti.com/es/chaqueta-100-a...</td>\n",
       "      <td>NA</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>101450 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                size promotion     category  \\\n",
       "0       UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No        Shoes   \n",
       "1       UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No        Shoes   \n",
       "2       UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No        Shoes   \n",
       "3       UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No        Shoes   \n",
       "4       UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No        Shoes   \n",
       "...                                              ...       ...          ...   \n",
       "101445  UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No    AMERICANA   \n",
       "101446  UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No  SOBRECAMISA   \n",
       "101447  UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No  SOBRECAMISA   \n",
       "101448  UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No  SOBRECAMISA   \n",
       "101449  UK 4,UK 6,UK 8,UK 10,UK 12,UK 14,UK 16,UK 18        No     CHAQUETA   \n",
       "\n",
       "         price basic_color product_id  section  \\\n",
       "0       110.00         NaN   BB550LSB      Man   \n",
       "1       140.00         NaN   37758401      Man   \n",
       "2       200.00         NaN    M990GL6      Man   \n",
       "3       110.00         NaN   W2288111      Man   \n",
       "4       110.00         NaN    5950CHE      Man   \n",
       "...        ...         ...        ...      ...   \n",
       "101445  129.00         NaN    unknown  unknown   \n",
       "101446   89.95         NaN    unknown  unknown   \n",
       "101447   89.95         NaN    unknown  unknown   \n",
       "101448   69.95         NaN    unknown  unknown   \n",
       "101449  129.00         NaN    unknown  unknown   \n",
       "\n",
       "                                                     name        brand  \\\n",
       "0                               New Balance BB550 - Men's  New Balance   \n",
       "1                                PUMA MB2 x Slime - Men's         PUMA   \n",
       "2                             New Balance 990V6 D - Men's  New Balance   \n",
       "3                         Nike Air Force 1 '07 LE - Men's         Nike   \n",
       "4                                      UGG Tasman - Men's          UGG   \n",
       "...                                                   ...          ...   \n",
       "101445           AMERICANA MEZCLA ALGODÓN\\n+1\\n\\n\\n-35% *         asos   \n",
       "101446  SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...         asos   \n",
       "101447  SOBRECAMISA DETALLE BOLSILLO CON ALGODÓN\\n+1\\n...         asos   \n",
       "101448  SOBRECAMISA POPELÍN DETALLE BOLSILLOS\\n+1\\n\\n\\...         asos   \n",
       "101449        CHAQUETA 100% ALGODÓN BOLSILLOS\\n\\n\\n-50% *         asos   \n",
       "\n",
       "                                                      url description  \n",
       "0       https://www.footlocker.com/product/~/BB550LSB....          NA  \n",
       "1       https://www.footlocker.com/product/~/37758401....          NA  \n",
       "2       https://www.footlocker.com/product/~/M990GL6.html          NA  \n",
       "3       https://www.footlocker.com/product/~/W2288111....          NA  \n",
       "4       https://www.footlocker.com/product/~/5950CHE.html          NA  \n",
       "...                                                   ...         ...  \n",
       "101445  https://www.massimodutti.com/es/americana-mezc...          NA  \n",
       "101446  https://www.massimodutti.com/es/sobrecamisa-de...          NA  \n",
       "101447  https://www.massimodutti.com/es/sobrecamisa-de...          NA  \n",
       "101448  https://www.massimodutti.com/es/sobrecamisa-po...          NA  \n",
       "101449  https://www.massimodutti.com/es/chaqueta-100-a...          NA  \n",
       "\n",
       "[101450 rows x 11 columns]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_cleaned"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f7992e8-40e9-478d-9107-ab0e9474f994",
   "metadata": {},
   "source": [
    "## EDA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "4d3ac5e7-3b3a-4278-b985-25b15e42902b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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hg0bpnfeeUc7d+6U9H8/p88//1yhoaG3XPfGffqvbvYz+icymgkAYC1KNwDcx1JSUjRr1iwVL15c06dPTzd/yZIlGjdunJYuXarGjRsrd+7catasmT755BPVqFFD8fHx6a6O3bhxY40ePVp58+ZVsWLF/lYum80mDw8Pubu7O6ZdvnxZs2fPdlquVq1akq5fffmhhx5yTP/888/TXZG8cePG+u6771S8ePEMHfp9LzRs2FCzZ8/Wnj17VKpUqZsu83c+T7vdrtq1aytXrlxavny5tmzZcsfS/cMPP+jEiROO0dSUlBQtWLBAxYsXdxqN9/b2VufOnTVp0iTFxMSoYsWKtzzs+UadOnXS2LFjNWDAAD322GNOX5Kk+eKLL/Tss89m6D1K1z+b+fPnKyUl5a7d3s5ut0tShke/jx8/ftMjG3bv3i3p/77MadCggTw8PLR//34999xzt9xeqVKlFBQUpM8++8zpjgCHDx9WTExMhr4cyqiMZsqMzH5+AABKNwDc15YuXapjx47prbfeSncrJkkqV66cJk2apBkzZqhx48aSrh9ivmDBAnXv3l2FCxfWE0884bRO7969tWjRItWqVUt9+vRRhQoVlJqaqsOHD2vFihXq16/fHQvSU089pfHjx6tNmzbq3Lmz/vzzT7399tuOP+jTlC1bVq1bt9a4cePk7u6uunXrKjY2VuPGjVNAQIDTea4jRoxQdHS0atasqZ49e6pUqVK6cuWKDh48qO+++06TJ0++46Hed9uIESO0dOlS1apVS//73/9Uvnx5nTt3TsuWLVPfvn0VHh6e4c/z9ddf19GjR/X444+rcOHCOnfunN599115enqqdu3ad8ySL18+1a1bV6+99pr8/Pz0wQcf6LfffnO6bViarl27KioqSps3b77plzU3ExAQoK+++kqNGzdWpUqV1L17d9WoUUNeXl6Ki4vTp59+qm3btmWqdLdq1Upz5sxRo0aN1KtXL1WrVk2enp46evSofvzxRzVt2lTPPPNMhrcnXd/nJWnq1Kny9/eXt7e3ihUrdtND06XrxbVw4cJq0qSJwsPDlZqaqq1bt2rcuHHKkSOHevXqJen6LctGjBihIUOG6Pfff9eTTz6p3Llz68SJE/rll1/k5+enyMhIubm5KTIyUl26dFHz5s3VsWNHnTt3TpGRkSpYsOBNb0P2d2U0U2b4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junGGE2YMEFDhgzRs88+q3LlymnWrFm6dOmS5s6d68LEAAAAAABkjMtLd7du3fTUU0/piSeecJp+4MABxcfHq379+o5pdrtdtWvXVkxMzL2OCQAAAABApnm48sXnz5+vX3/9VRs3bkw3Lz4+XpIUGBjoND0wMFCHDh265TaTkpKUlJTkeJ6YmHiX0gIAAAAAkDkuG+k+cuSIevXqpU8//VTe3t63XM5mszk9N8akm3ajMWPGKCAgwPEICQm5a5kBAAAAAMgMl5XuzZs36+TJk6pcubI8PDzk4eGh1atXa+LEifLw8HCMcKeNeKc5efJkutHvGw0ePFgJCQmOx5EjRyx9HwAAAAAA3IrLDi9//PHHtWPHDqdpHTp0UHh4uAYOHKgHHnhAQUFBio6OVqVKlSRJV69e1erVq/XWW2/dcrt2u112u93S7AAAAAAAZITLSre/v7/KlSvnNM3Pz0958+Z1TO/du7dGjx6tsLAwhYWFafTo0fL19VWbNm1cERkAAAAAgExx6YXU7mTAgAG6fPmyunbtqrNnz6p69epasWKF/P39XR0NAAAAAIA7shljjKtDWCkxMVEBAQFKSEhQzpw5XR0HAJCFvLnltKsjIJsYVCmfqyMAALKYjHbNLD3SDQAAAOD+wBedyIz76ctOl129HAAAAACA+x2lGwAAAAAAi1C6AQAAAACwCKUbAAAAAACLULoBAAAAALAIpRsAAAAAAItQugEAAAAAsAilGwAAAAAAi1C6AQAAAACwCKUbAAAAAACLULoBAAAAALAIpRsAAAAAAItQugEAAAAAsAilGwAAAAAAi1C6AQAAAACwCKUbAAAAAACLULoBAAAAALAIpRsAAAAAAItQugEAAAAAsAilGwAAAAAAi1C6AQAAAACwCKUbAAAAAACLULoBAAAAALAIpRsAAAAAAItQugEAAAAAsAilGwAAAAAAi1C6AQAAAACwCKUbAAAAAACLULoBAAAAALAIpRsAAAAAAItQugEAAAAAsAilGwAAAAAAi1C6AQAAAACwCKUbAAAAAACLePydlY4cOaKDBw/q0qVLyp8/v8qWLSu73X63swEAAAAAkK1luHQfOnRIkydP1rx583TkyBEZYxzzvLy89Nhjj6lz58567rnn5ObGADoAAAAAABlqx7169VL58uUVFxenESNGKDY2VgkJCbp69ari4+P13Xff6dFHH9Vrr72mChUqaOPGjVbnBgAAAAAgy8vQSLeXl5f279+v/Pnzp5tXoEAB1a1bV3Xr1tWwYcP03Xff6dChQ6patepdDwsAAAAAQHaSodI9duzYDG+wUaNGfzsMAAAAAAD3kwyffJ2cnKx169bddN6pU6e0Zs0apaSk3LVgAAAAAABkdxku3ePHj9fnn39+03m5cuXS8OHDNWHChLuVCwAAAACAbC/DpXvmzJlq1aqVJKlChQo6efKkY56np6dGjhypadOm3f2EAAAAAABkUxku3UePHlVQUJAk6cCBA7pw4YIqVaqkU6dOSZLy58+vw4cPW5MSAAAAAIBsKMOlu3jx4lq/fr0kyWazyRijffv26fz585KkRYsWqUyZMtakBAAAAAAgG8rQ1csl6ZVXXlGfPn3k7+8vY4xsNpskKTY2Vh9++KEmTpyohQsXWhYUAAAAAIDsJlOl+8CBA3ruueeUnJysSpUq6dKlS2ratKnCwsL09ddfq0GDBlZmBQAAAAAgW8nw4eWS9NZbb+nYsWPy9vbW0KFD5eXlpR9//FF79uyhcAMAAAAA8BcZHulOkzdvXo0YMULt2rWTm5sb53EDAAAAAHALGSrdFy9elJ+fn+N5v379nP73TssDAAAAAPBvlKHDy0uUKKHRo0fr2LFjt1zGGKPo6Gg1bNhQEydOvGsBAQAAAADIrjI00r1q1SoNHTpUkZGRqlixoqpUqaLg4GB5e3vr7Nmz2rVrl9avXy9PT08NHjxYnTt3tjo3AAAAAABZXoZKd6lSpbRw4UIdPXpUCxcu1Jo1axQTE6PLly8rX758qlSpkqZNm6ZGjRrJzS1T12YDAAAAAOC+lakLqRUuXFh9+vRRnz59rMoDAAAAAMB9g2FpAAAAAAAsQukGAAAAAMAilG4AAAAAACxC6QYAAAAAwCKUbgAAAAAALPK3SvfatWvVtm1b1ahRQ3/88Yckafbs2Vq3bt1dDQcAAAAAQHaW6dK9aNEiNWjQQD4+PtqyZYuSkpIkSefPn9fo0aPvekAAAAAAALKrTJfukSNHavLkyZo2bZo8PT0d02vWrKlff/31roYDAAAAACA7y3Tp3rNnj2rVqpVues6cOXXu3Lm7kQkAAAAAgPtCpkt3wYIFtW/fvnTT161bpwceeOCuhAIAAAAA4H6Q6dLdpUsX9erVSxs2bJDNZtOxY8c0Z84c9e/fX127drUiIwAAAAAA2ZJHZlcYMGCAEhISVKdOHV25ckW1atWS3W5X//791b17dysyAgAAAACQLWW6dEvSqFGjNGTIEO3atUupqakqU6aMcuTIcbezAQAAAACQrWW6dCckJCglJUV58uRRlSpVHNPPnDkjDw8P5cyZ864GBAAAAAAgu8r0Od2tWrXS/Pnz003/7LPP1KpVq7sSCgAAAACA+0GmS/eGDRtUp06ddNMjIiK0YcOGuxIKAAAAAID7QaZLd1JSkpKTk9NNv3btmi5fvnxXQgEAAAAAcD/IdOmuWrWqpk6dmm765MmTVbly5bsSCgAAAACA+0GmS/eoUaM0ffp01apVS5GRkYqMjFStWrX00UcfafTo0Zna1ocffqgKFSooZ86cypkzp2rUqKGlS5c65htjNHz4cAUHB8vHx0cRERGKjY3NbGQAAAAAAFwi06X7kUce0fr16xUSEqLPPvtM33zzjUqUKKHt27frsccey9S2ChcurDfffFObNm3Spk2bVLduXTVt2tRRrKOiojR+/HhNmjRJGzduVFBQkOrVq6fz589nNjYAAAAAAPeczRhjXB3iRnny5NHYsWPVsWNHBQcHq3fv3ho4cKCk6+eTBwYG6q233lKXLl0ytL3ExEQFBAQoISGB25kBAJy8ueW0qyMgmxhUKZ+rIwDZHr9zkRnZ4fduRrtmhka6ExMTnf77do+/KyUlRfPnz9fFixdVo0YNHThwQPHx8apfv75jGbvdrtq1aysmJuZvvw4AAAAAAPeKR0YWyp07t44fP64CBQooV65cstls6ZYxxshmsyklJSVTAXbs2KEaNWroypUrypEjh7788kuVKVPGUawDAwOdlg8MDNShQ4duub2kpCQlJSU5nv+TLwIAAAAAAPgnMlS6V65cqTx58kiSfvzxx7saoFSpUtq6davOnTunRYsWqX379lq9erVj/l8Lflq5v5UxY8YoMjLyrmYEAAAAAODvyFDprl27tiQpOTlZq1atUseOHRUSEnJXAnh5ealEiRKSpCpVqmjjxo169913Hedxx8fHq2DBgo7lT548mW70+0aDBw9W3759Hc8TExPvWlYAAAAAADIjU1cv9/Dw0Ntvv53pQ8gzwxijpKQkFStWTEFBQYqOjnbMu3r1qlavXq2aNWvecn273e64BVnaAwAAAAAAV8jQ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nTp1tH79+rsaDgAAAACA7CzTpXvHjh165pln0k3Pnz8/9+8GAAAAAOAGmS7duXLl0vHjx9NN37JliwoVKnRXQgEAAAAAcD/IdOlu06aNBg4cqPj4eNlsNqWmpuqnn35S//799eKLL1qREQAAAACAbCnTpXvUqFEqUqSIChUqpAsXLqhMmTKqVauWatasqaFDh1qREQAAAACAbCnT9+n29PTUnDlzNGLECG3ZskWpqamqVKmSwsLCrMgHAAAAAEC2lenSvXr1atWuXVvFixdX8eLFrcgEAAAAAMB9IdOHl9erV09FihTRoEGDtHPnTisyAQAAAABwX8h06T527JgGDBigtWvXqkKFCqpQoYKioqJ09OhRK/IBAAAAAJBtZbp058uXT927d9dPP/2k/fv36/nnn9cnn3yiokWLqm7dulZkBAAAAAAgW8p06b5RsWLFNGjQIL355psqX768Vq9efbdyAQAAAACQ7f3t0v3TTz+pa9euKliwoNq0aaOyZctqyZIldzMbAAAAAADZWqavXv6///1P8+bN07Fjx/TEE09owoQJatasmXx9fa3IBwAAAABAtpXp0r1q1Sr1799fzz//vPLly+c0b+vWrapYseLdygYAAAAAQLaW6dIdExPj9DwhIUFz5szR9OnTtW3bNqWkpNy1cAAAAAAAZGd/+5zulStXqm3btipYsKDee+89NWrUSJs2bbqb2QAAAAAAyNYyNdJ99OhRffzxx/roo4908eJFtWzZUteuXdOiRYtUpkwZqzICAAAAAJAtZXiku1GjRipTpox27dql9957T8eOHdN7771nZTYAAAAAALK1DI90r1ixQj179tR///tfhYWFWZkJAAAAAID7QoZHuteuXavz58+rSpUqql69uiZNmqRTp05ZmQ0AAAAAgGwtw6W7Ro0amjZtmo4fP64uXbpo/vz5KlSokFJTUxUdHa3z589bmRMAAAAAgGwn01cv9/X1VceOHbVu3Trt2LFD/fr105tvvqkCBQro6aeftiIjAAAAAADZ0t++ZZgklSpVSlFRUTp69KjmzZt3tzIBAAAAAHBf+EelO427u7uaNWumr7/++m5sDgAAAACA+8JdKd1/15gxY1S1alX5+/urQIECatasmfbs2eO0jDFGw4cPV3BwsHx8fBQREaHY2FgXJQYAAAAAIONcWrpXr16tbt266eef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6cMPP5QkVaxYUd27d5ckDRgwQG5ubmrVqpUrY+L/Y6Qb2cqhQ4fUu3dv1apVS506dVJMTIz8/f01ePBgffvtt/rmm29cHRH/cmXLllVkZKR+++03TZgwwTHi3aNHD+3cuVOFCxfWmTNn9Morr2jbtm2KiorSL7/8oosXL7o4OfB/Dh8+rEKFCmngwIGOLzwlqWnTpvr888/1/vvva8SIETp37pzrQgJ/Q1BQkHr16qX9+/fr1KlTkq4fSefm5qYBAwbozTff1CuvvKKZM2e6OCmQXtqRSGn/W7JkSe3fv18nT550LFOyZEn16NFDLVq0UIcOHfT555+7JCucMdKNLC3tH8I0oaGhio+P19SpU7V27VrVrVtXrVu3VuXKldWuXTtFR0erUaNGstlsTusB90JycrI8PDzUtm1bXbt2TdOnT9ekSZM0aNAgNW7cWFWrVtVvv/2m2rVrO9bZvXu3QkND5eHBr2NkHUWKFNGHH36onj17au/evbp27Zo8PT1ljFHTpk21ePFiNWnSRJ6enhozZgwXoEK2kTt3bv3vf/+TMUa9evVSaGionnrqKcc1DPr37y8vLy89/PDDro4KpGOz2fTLL79o3bp16tu3r2NffvXVV+Xn56f69etLksLCwtSlSxfZ7XY9+OCDLk4NSbIZrjOPLOrGwr127Vq5u7vLGKNHHnnEscySJUu0atUqLVy4UEeOHFHu3Lm1fft2FSpUyPEPKHCvpO1zy5cv108//aR58+bp4MGDatmypQYMGOD0D9/OnTs1e/ZsTZ06VWvWrFH58uVdmBy4uQ8//FDdunXTW2+9pf79+8tmszn282XLlik0NFSlS5d2dUzgptL21X379uny5cu6ePGio0yfO3dOQ4cO1dSpU/Xll186FW8gK+vXr5+++eYbbdy4UQEBAYqJidH777+v7du3a/z48apXr55j2bQvTOF6lG5kOT179lTVqlXVrl07SVKfPn306aefytPTU1euXFHTpk01atQoBQcHS7o+unju3DlNnjxZCxYsUK1atfTee+8x0o175sYviL7//nvVr19f7777rooUKaJdu3Zp6tSpql27tvr166fy5ctr48aNmj59umJiYvTpp5/yLTRcKq1o7Ny5UydPnlRiYqKaNWvmmD9p0iT17NnzpsUbyKrS9tHFixdr4MCBSk1NVUJCgp577jm988478vb2VkJCgoYMGaKZM2fq008/1TPPPOPq2EA6afvyjQW6dOnSKl++vD777DNJUkxMjCZNmqTdu3dr1KhRatSokSsj42YMkIUcPHjQPPvss6ZMmTLmiy++MLt37zYlSpQw69evN9u2bTMrVqwwefPmNY0bNzbnz583xhhz9epVY4wxKSkpJioqyjzyyCPm0qVLrnwb+JdYt25dumn/+c9/TNOmTZ2mzZw50xQuXNi88MILZu/evSY1NdVs2LDB/PHHH/coKXBzqampxhhjvvjiC1O4cGFTvnx5kytXLlO/fn2zfft2k5KSYowx5r333jN2u91ERkY61gGyuqVLlxp/f38zefJkc+LECTNv3jxjs9lM+/btTUJCgjHGmHPnzpn27dub/PnzmwsXLrg4MXBzK1asMEOHDjUbNmwwxhizcuVKU7ZsWTN9+nTHMj///LNp3LixqVmzprl48SK/q7MYSjeynG3btpmXX37ZlC9f3nTo0MG88sorTvP37t1rcuTIYQYNGuSYlvaH4d69e03+/PnN5s2b72lm/PvMmzfPPP744+bEiRNO03v27GkaNGhgkpOTHfulMcYMGzbM5MiRwzz33HNm586d9zoucEvR0dEmd+7cjj/eNm/ebGw2m6lbt67ZvHmz4w+3qKgokydPHvPnn3+6Mi6QIX/++ad58cUXzZgxY4wxxhw+fNgUK1bMNG3a1OTKlcu0atXKnD171hhjTEJCgjl+/LgL0wK3dunSJdOoUSNjs9lMhQoVzPvvv2/OnDljXn75ZdOhQwdz9OhRx7IbN250eo6sg+NvkeVUqFBB3bp1U40aNbRkyRIdP37cMS8pKUlhYWEaNmyYli1bpjNnzsgY4zi094svvpCbm5sKFizoqvi4z6XdLz48PFwfffSRChQooCNHjjjmP/DAA4qJidGuXbvk5ubmWL5o0aIKDg7WpUuXlCdPHpdkByTp4MGD+vrrryVJV69e1bfffquePXuqU6dOOnDggFq0aKH27dvr4MGD6tatm3799Velpqbq1Vdf1b59+9h/kS34+fmpdu3aatGihU6fPq2nn35aTzzxhBYvXqyRI0dqwYIF6tSpk86fP6+cOXMqKCjI1ZEBB3PD2b/e3t5q3769IiIi9OKLL2rMmDEaPXq08uTJoy+++EJr1qxxLFulShUVKlTIFZFxB5RuZAlpv1zSCkrFihX1yiuvqFGjRlq6dKnmzJkjSbLb7ZKu/2OakpIiLy8vp/MKU1NTtXz5cko3LOPm5qZdu3ZpwIAB8vX11Y4dO9S8eXO98847kuS4R3eTJk20bds2JSUlSZL27Nmjjh076tNPP2X/hMscO3ZMVatW1aBBgzR37lx5eXmpUaNGatmypc6dO6fnn39edevW1cyZMzV9+nRt2LBBXbp00Y4dOyRdv/IzkBWZv1yiyG63q02bNipevLiWLFkif39/DRs2TNL1+3LXqFFD27Zt47Z3yJJsNpvWr1+vr776SjabTc8++6x8fX114MAB/fbbb5Kky5cvKzExUS+99JJiY2NdnBh3wj1q4HI3XoQqJSXF8d+VKlVSnz595ObmpqFDhyolJUXNmzfX+fPn9cUXX6hQoULy8/Nz2tbgwYPveX78+/zyyy86f/688uXLpzNnzqh48eL68ssv5enpqe7du2vOnDlq27atHnvsMZUvX14eHh7asGGDNm/ezCghXGrPnj36888/VaxYMS1YsEBubm5q1aqVJOmrr76SJA0cOFCSdOXKFTVp0kRHjhyRv7+/yzIDd2L+/4WmNm3apJ07d6p06dIqUaKE8ubNK+n6rRkTExMdI4C7d+9Ws2bN1KtXL3l5ebkyOnBTiYmJmjNnjj744AP169dPffv21ezZsxUREaGFCxfqrbfe0vbt2/XHH39o+fLl/I7OBrh6OVzqxsL94YcfatWqVXJzc9ODDz6oQYMGSZI2b96siRMnavbs2QoNDVXdunW1b98+ff/99/L09Ex3L2/AamPGjNGiRYu0YcMGubu76/fff9eoUaO0a9cutW/fXq+88ookaerUqTp27JguX76sDh06KDw83MXJAalTp07avHmzSpQooTNnzqhDhw5q166dpk2bpsjISG3YsEGFChXSkCFD5OHhoddff13u7u6ujg3c1uLFi/Xiiy8qX758unbtmp566in169dPYWFh+vnnnxUREaFHH31UdrtdP/30k9atW6dy5cq5OjZwS5cvX9aqVavUo0cPlShRQo899pgKFSqkDRs2qH///ipevLgk6dSpU8qfP7+L0+JOKN3IEgYNGqRZs2apY8eOunr1qhYtWqQ6depoxowZkqRt27bp/fff14IFCzRp0iS1bdtWNptNycnJ8vDggA1YJ+1LnStXrsjb21uS9MYbb2jVqlX64YcfHPP379+v0aNHa9euXXrhhRfUvXt3FycHnCUlJclut+u7777TwoUL1bp1a02ZMkWnT59Wnz59FBERoXLlysnb21tBQUHauXOnVq1apYoVK7o6OnBLxhhdvXpVL730kp588km1atVK06ZN0+eff678+fPrjTfeUHh4uJYvX67JkycrX7586tWrF4UbWYq54Z7yR48eVZ48eVSwYEHlz59fcXFxmjt3rr799lvt2bNHgYGBevXVV/Wf//zHaV1kbQwPwuXmzZunL7/8UosXL9aoUaNUvXp1nThxQgsXLtRzzz0nSXrwwQfVvn17DRkyRG3atHHcJ5bCDau5ubnpjz/+0Isvvqjo6GhJ10+DyJcvn6Tr/9ilpqaqePHiGjhwoMqUKaN58+bp7bffdmVsQJJ05MgRLV68WNL/XROjatWq+vnnnxUXF+coIW+//bbWrVunX3/9Vc8884xq1aql9evXU7iRZaWNGZ09e9ZROipXriy73a7u3burQ4cOOnnypF5//XXt3btXDRo00GeffaYPP/yQwo0sJW3/XbRokR5//HG9+OKLatasmR5//HFt2bJFYWFh6tu3r+bNm6cmTZpo3759GjFihK5cuULhzkYY6cY9d/XqVSUnJ8vX11eSNHnyZB0/flyRkZH65ptv1L59ew0bNkx+fn565ZVX1L59e8eId5qUlBQOd8Q98/vvv6tt27bKlSuXRo4cqUWLFunIkSP65JNP0i178eJFtWnTRsYYzZo1iwtPwWWOHDmiSpUq6cyZM2rYsKHat2+vihUrqmTJkvrmm280duxYLVq0SKdPn9bQoUN15swZdevWTc2bN3d1dCBDFi9erP/973/y9PRUYmKivvnmG6dCPWvWLM2ePVvu7u6aNGmSwsLCXJgWuLWff/5ZTzzxhN5++201aNBAcXFxmjJliqKjo7Vu3TpVqFDBsezcuXNVrVo1lShRwoWJkVmUbtxTixYt0ty5c3XgwAE988wzeu211yRJBw4cUEBAgOrXr68WLVpo4MCB2rdvnyIiInTs2DH1799fUVFRLk6Pf7N9+/ape/fu8vPz06FDh5Samqpy5crJZrPJ3d1dV65ckc1mk6+vr/744w9NmTJFISEhro6Nf7FDhw6pefPm8vT01NWrV1WpUiVFR0dr8ODByp07t2bPnq2uXbuqYcOG2rVrl3r16iVvb2/N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mmez2f72xc8KFSqkdu3aqV27dho5cqRKliypyZMnKzIyUqmpqerSpYt69uyZbr0iRYpoz549N91m2pcQN7oxc1q5vdm0tPeRmpqqyMhIPfvss+m25e3tfdPtpm0ns59Fvnz5dOnSJV29elVeXl5O8/z9/fX000/r6aef1siRI9WgQQONHDlS9erVU2pqqipXrqw5c+ak22ba4el3y1+/EDDGpJt2u88zzZkzZ5Q/f/67lgsAkL1QugEA2VKePHnUoEEDvf/+++rZs2e687rPnTuXofO6H3roIS1atEhFixb9R1c09/T0vOV5yLeTO3duFSxYUBcvXnTkiY2NdZyD/Ffh4eFKTk7Wli1bVLlyZUnSvn37MnSLrjt56KGHtGfPnlu+dkakFeg7fRZp98TetWvXbe+PbbPZFB4erpiYGEfGBQsWqECBAsqZM+dN1ylatKh++OEH1alT56bz7/Szypkzp4KDg7Vu3TrVqlXLMT0mJkbVqlW77fv6q7QR+EqVKmVqPQDA/YPDywEA2dYHH3yglJQUVatWTYsWLVJcXJx2796tiRMnqkaNGhnaRrdu3XTmzBm1bt1av/zyi37//XetWLFCHTt2zFSJTit68fHxOnv27E2XmTJliv773/9qxYoV2r9/v2JjYzVw4EDFxsaqSZMmkqSBAwdq/fr16tatm7Zu3aq4uDh9/fXXjntZh4eH64knnlDnzp31yy+/aMuWLercubN8fHz+8aH2r7/+uj755BMNHz5csbGx2r17txYsWKChQ4dmeBuhoaGy2WxasmSJTp06pQsXLtx0ufz58+uhhx7SunXrHNO2bt2qpk2b6vPPP9euXbu0b98+zZgxQx999JGaNm0qSXrhhReUL18+NW3aVGvXrtWBAwe0evVq9erVS0ePHpUkDR8+XOPGjdPEiRMVFxenX3/91em2XRn5Wb366qt66623tGDBAu3Zs0eDBg3S1q1b1atXrwx/FpL0888/y263Z3h/BADcfyjdAIBsq1ixYvr1119Vp04d9evXT+XKlVO9evX0ww8/6MMPP8zQNoKDg/XTTz8pJSVFDRo0ULly5dSrVy8FBARk6lDlcePGKTo6WiEhIbcc1axWrZouXLigV155RWXLllXt2rX1888/a/Hixapdu7ak6+cIr169WnFxcXrsscdUqVIlvfbaa06Hun/yyScKDAxUrVq19Mwzz+g///mP/P39nQ4B/zsaNGigJUuWKDo6WlWrVtXDDz+s8ePHKzQ0NMPbKFSokCIjIzVo0CAFBgY6XR39rzp37ux0mHjhwoVVtGhRRUZGqnr16nrooYf07rvvKjIyUkOGDJEk+fr6as2aNSpSpIieffZZlS5dWh07dtTly5cdI9/t27fXhAkT9MEHH6hs2bJq3Lix01XHM/Kz6tmzp/r166d+/fqpfPnyWrZsmb7++muFhYVl+LOQpHnz5umFF16Qr69vptYDANw/bOZmJ4EBAIBs4+jRowoJCdH333//jy4gdq9duXJFpUqV0vz58+/LkeBTp04pPDxcmzZtUrFixVwdBwDgIpzTDQBANrNy5UpduHBB5cuX1/HjxzVgwAAVLVrU6fzj7MDb21uffPKJTp8+7eooljhw4IA++OADCjcA/Msx0g0AQDazfPly9evXT7///rv8/f1Vs2ZNTZgwIVOHgQMAgHuD0g0AAAAAgEW4kBoAAAAAABahdAMAAAAAYBFKNwAAAAAAFqF0AwAAAABgEUo3AAAAAAAWoXQDAAAAAGARSjcAAAAAABahdAMAAAAAYBFKNwAAAAAAFvl/GBsKnaWkKOwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "section\n",
       "Baby       29.56\n",
       "Kids       20.13\n",
       "Man        53.37\n",
       "Woman      28.88\n",
       "unknown    39.20\n",
       "Name: price, dtype: float64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Mean price for each group per section\n",
    "average_prices_by_section = df_cleaned.groupby('section')['price'].mean().round(2)\n",
    "sections = ['Baby', 'Kids', 'Man', 'Woman', 'unknown']\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(sections, average_prices_by_section, color='skyblue')\n",
    "plt.xlabel('Client Segment (Section)')\n",
    "plt.ylabel('Average Price (€)')\n",
    "plt.title('Average Prices by Client Segment')\n",
    "plt.xticks(rotation=45)  \n",
    "plt.tight_layout()  \n",
    "plt.show()\n",
    "\n",
    "average_prices_by_section"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "78da483d-c70e-47f5-a4af-73764fda9490",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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z5/o/vz588vPz09hYWG2Zffu3dPWrVtVpUqVpx0XAAAAAIBE0vRI9zvvvKMFCxbo+++/l6enp+08bS8vL7m7u8tisah3794aO3asgoKCFBQUpLFjx8rDw0Pt27e3c3oAAAAAwLMuTZfu6dOnS5Jq1qyZaPns2bP12muvSZIGDhyomJgY9ejRQzdu3FDlypW1fv16eXp6PuW0AAAAAAAklqZLt2EYT1zHYrEoJCREISEh5gcCAAAAACAF0vQ53QAAAAAApGeUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJJRuAAAAAABMQukGAAAAAMAklG4AAAAAAExC6QYAAAAAwCSUbgAAAAAATELpBgAAAADAJBmmdH/++efKnz+/3NzcVKFCBW3fvt3ekQAAAAAAz7gMUboXL16s3r17a8iQITp48KCqV6+uhg0b6q+//rJ3NAAAAADAMyxDlO5Jkyapa9eueuONN1SsWDFNnjxZgYGBmj59ur2jAQAAAACeYU72DvBf3bt3T/v379egQYMSLa9Xr5527dr1yG1iY2MVGxtru33r1i1JUmRkpHlBU8Hd6Ch7R0A6ERnpYu8INuy3SA72WaQ37LNIb9hnkd6kpX32cRL6o2EY/7heui/dV69eVXx8vHx9fRMt9/X1VXh4+CO3CQ0N1ciRI5MsDwwMNCUj8LQl3buBtI19FukN+yzSG/ZZpDfpaZ+NioqSl5fXY+9P96U7gcViSXTbMIwkyxIMHjxYffv2td22Wq26fv26cuTI8dhtkDZFRkYqMDBQ586dU5YsWewdB3gi9lmkN+yzSG/YZ5HesM+mX4ZhKCoqSgEBAf+4Xrov3d7e3nJ0dEwyqh0REZFk9DuBq6urXF1dEy3LmjWrWRHxFGTJkoU3KaQr7LNIb9hnkd6wzyK9YZ9Nn/5phDtBup9IzcXFRRUqVFBYWFii5WFhYapSpYqdUgEAAAAAkAFGuiWpb9++6tSpkypWrKgXXnhBX375pf766y+99dZb9o4GAAAAAHiGZYjS3aZNG127dk2jRo3SpUuXVLJkSa1du1Z58+a1dzSYzNXVVSNGjEhyugCQVrHPIr1hn0V6wz6L9IZ9NuOzGE+a3xwAAAAAAPwr6f6cbgAAAAAA0ipKNwAAAAAAJqF0AwAAAABgEko3AAAAAAAmoXQDj8EcgwAAAMiI+vbtq/nz59s7xjOD0g08hsVi0cKFCzVkyBB7R8Ezgi96AADA05AjRw6VKFHC3jGeGZRu4DFOnjypAQMGyNfXV1ar1d5xkMGdP39eK1as0KlTp+wdBQAAZHBDhgxR2bJltW7dOs2ePdvecTI8SjfwCL/++qvmzJmjl19+Wb169ZLFYrF3JGRgR48eVYMGDbRixQqdPHnS3nGAf+VxR2pwBAfSKr5Qx7Pk4ffiuLg423/v2bNHXbt21dy5c+0R65nhZO8AQFpz/fp1DRs2TDt37lTNmjUlPTjU3Gq1ysGB76mQuo4dO6bq1aurW7du6tatm4KCgpKsYxgGX/wgTXv4/fHs2bOKiYlRrly55Onpyfsn7C7hPXT//v06fvy4oqOj1aZNG2XLls3e0YCnIuH/A+Hh4XJ0dJSPj49++OEHubi4KCQkRBaLRV27dpXVatVrr71m77gZEqUb+Jvs2bOrR48eunfvnjZv3qy1a9eqUaNGcnBwoPwgVUVFRalfv37q0qWLJkyYYFtuGIZu3bql6Oho5c6dWxaLhX0PaZZhGLZCPWTIEP3www/63//+p0qVKqlSpUr6+OOP5eDgQPGGXSS8dy5fvlzvvvuufH19JUkhISFavXq1KlWqZOeEgPksFotu3Lih119/XQEBAapatareeOMNLVmyRJI0YsQIGYahN954Q4Zh6PXXX7dz4oyH0o1nXsI/yLdv35YkZcqUSfXr11fWrFkVEhKiiRMnytnZWXXr1qX8IFXdv39f4eHhib5V3rJlizZu3KjZs2fLzc1NHTp00MiRI9nnkGYl7Jvjxo3TjBkz9M0338jFxUW7du3Sd999p4iICM2dO5fCDbuwWCzaunWrunXrpgkTJqhr1676/fffVbx4cbVo0UJz5sxR7dq17R0TMF3WrFnVsGFDTZs2TXPnztXUqVP1yiuvKC4uTk5OTgoJCZEkdevWTQ4ODurcubN9A2cw/AuIZ1pCgV67dq2aN2+u4OBgVatWTevXr1flypX1wQcfKFOmTBo/frw2bNggSZQfpArDMHTjxg3dvn1bly9fVkREhKZOnarevXvr4MGD6tSpkzp37qzRo0fr66+/tndc4B9FRkZq69atCgkJUdOmTVW/fn0NGDBAQ4YM0b59+/T555/bOyKeUYZhaPPmzerVq5e6du2qc+fOqX79+urWrZsqV66stm3bavv27faOCaS6h+csiI+Pl8ViUZ06dWQYhnLlyqXffvtNERERcnJyUnx8vKQHR4AMHz5cr7/+OpcTS2UWgxlO8Iz74Ycf1KZNGw0cOFCNGjXSoEGDdPToUa1Zs0YVK1bUpk2bNHXqVJ07d04ff/yx7TxvIDV88MEH+uSTT+Tr66uIiAiFhoaqXr16KlasmG7fvq06deqoatWqmjhxor2jAjZ/P1T83r17qlixourUqaNPPvnEtjwmJkbt2rVTtmzZmB0XT03CF+phYWEqW7aszp8/L8MwFBQUpAYNGqhkyZL64osv9Msvv+i5556Tm5ubfvzxR9WoUcPe0YFUdf78ebm5ucnb21urVq3SypUr1atXL+3cuVPz589X8eLFNXbsWOXMmVPx8fFydHSUJH300Udq0qSJihUrZudnkHFweDmeWVarVXfv3tXnn3+uAQMGaPjw4bp+/brOnDmjFi1aqGLFipKk2rVr6/79+/rmm29UoEABO6dGenbz5k3dunVLZ86cUdasWVW2bFmNHTtWDRo0UHR0tEqXLq3cuXMn2iZz5szKmzevnRIDj5ZQuKOiouTp6Smr1aqqVavq1KlTOnnypG1CQHd3dxUrVkwHDx7U/fv35ezsbM/YeEZYLBZt375d9evX17x589S+fXtJ0r59+3Tv3j298847kiRnZ2e1bdtWHh4eypkzpz0jA6kuNjZW9evXl5+fn9q1a6c333xTixYtUtmyZVW2bFnFxsZq6dKlGjZsmEaPHi0fHx9NnTpVxYoV04ABA+wdP8OhdOOZ5eDgIDc3N12+fFmvvPKKrl69qtKlS6tp06a2QyGXLl2qmjVrqn79+qpevbo8PDzsnBrp1dGjR9W9e3dFRkbq2LFjcnNz03PPPaeJEyeqSpUqcnJK/HYcHx+v0NBQnT59Wk2bNrVTaiCxh0e4v//+e3Xt2lW//vqrAgIC1KFDB7388sv66KOP1LNnT5UuXVq3b9/W7t27Vbx4cQo3nprTp09r+/bt+uijj2yFW3ow6nfw4EF5eHgoPj5ey5YtU0xMjG0eAiAjcXV11datW1WkSBHt2rVLU6ZMUevWrW0j2n379pXFYtGKFSvUqlUrFStWTF988YWOHDli7+gZEqUbz4yHPyzu2LFDrq6uqlSpktzc3DRlyhRt3LhRzZo106effipJunHjhmbPnq2oqCi9/vrrFG78a8eOHVPVqlXVrVs3vfzyy8qRI4c2bNigKVOmqGXLlpo+fboaNGhgW3/jxo1atWqVFixYoPXr1yt//vx2TA888PB76JIlS3To0CFdv35djRs31vfff69q1appwYIF6tq1qw4ePCir1SpXV1dFRUXZ3leZiBJm+/3339W9e3f98ccf+vDDDyXJVjJefvllBQcHq3jx4ipTpoxOnDihbdu2UbiRIVmtVtus5R4eHlq/fr3atm0rb29v2/t5nz59bJ9J/vjjDx0+fFglSpSwd/QMiXO6keEdPXpUJUuWlCTFxcXp9u3bKlKkiObMmaP69evriy++UEhIiPLkyaM9e/bYthsyZIiWL1+udevWKV++fHZKj/QuMjJSrVq1UokSJTRp0iTbP3Tx8fE6deqUWrdurbi4OG3dulXe3t5avXq1hg8fLn9/f3300Uf844c0p3///lqxYoW6du2qkydPaseOHZKkDRs2KG/evPr111916NAhHTlyRLlz59Y777wjJycn2wy5gJmuXLmikJAQLV68WPXr17dNBpWw/8XExGjmzJmyWCxq0KCB7VQIIKP566+/lCdPHt24cUORkZF6/vnnVa5cOc2ZM0c+Pj5JvgSNiYmRu7u7HRNnbJRuZGhLlizR2LFj1adPH7366quSHpxXW6ZMGf3www8qWbKkLly4oNGjR2vLli0qX768ihcvrhMnTmjVqlXasmWLypYta98ngXTt8uXLql69uj7++GO99NJLSe7fu3ev6tatq7feekvjx4+XJB05ckQBAQHKkSPH044L/KPDhw+rSZMmmjVrlurVqydJ2rRpk0aMGKGIiAht3LgxybwEkhJN0AOY7dq1axo3bpzWrl2r1q1ba8SIEZLYD/FsMAxDJ0+eVMWKFTVy5Eh17txZ2bNn15EjR1S/fn2VL19es2fPlo+PjyZOnKjIyEiNHDmSI5FMxlfOyNAqVqyogIAAzZ07VxaLRZ06dZK7u7syZcokb29vSVKuXLn0wQcfqFKlSpo1a5YuXryoAgUKaNeuXSpevLidnwHSM8MwdPr0af3555+20ZS/f+grW7asypcvrzNnztiWlSpV6qlnBZIjOjpa165dk7+/v21ZcHCwBg4cqPbt26tJkyZau3atAgICEh2OTtGBGRJKwsmTJ3Xu3Dllz55duXLlko+PjwYMGKC4uDitW7dODg4OGjZsmBwdHSneyPAsFosKFy6szp07a/z48XJ1dVW7du1UqlQprV+/XvXr11etWrVUtGhR/fDDD/r5559t28E8XKcbGVZ8fLzy58+vGTNmyMPDQ7NmzdKCBQsUHh6uuLi4RNcvDAwMVJcuXbRz505t3rxZX375JYUb/1rCvmWxWFS0aFFlz57dNjmfo6OjHj7AyMXFRf7+/rp9+7ZdsgKP86gD4YKCglSsWDGtXbtW9+/fl/Rgn65Tp45KlCihW7duqUmTJrp69WqiS4oBqS3hfNXly5erQYMGeuONN/Taa6+pR48eOnHihHLmzKlBgwbphRde0E8//aRBgwZJ4gsgZEwJ79cPv29PnTpVnTp10rBhw7Rw4ULdvHlTJUuW1IEDB1ShQgX5+Pho3759KlOmjL1iP1MY6UaGlfCBLzAwUFOnTtW7776rOXPm6H//+5+ioqL02Wefyc3NTW5ubnJ0dNSVK1dUrFgxvfrqq3xYxL/2559/atGiRWrTpo3y588vNzc3BQcHa82aNapevbpat24ti8ViG6GxWq2Kjo7W888/b+/ogM3Do9RRUVGyWq3y8vJStmzZVLFiRa1cuVL58uVTmzZtJEl3795VYGCg3n77bU2bNk2LFi1Sz549OVwRqS42Nlaurq5ycHBQWFiYunbtqg8//FA9e/bUjBkzNGDAAF28eFEzZsxQqVKlNGjQIA0dOlT79+/X1atXbUe5ARmJxWLRxo0bFRkZqcaNG9smB/zoo48kSQMHDpRhGGrdurV8fX01e/ZsxcfHc1WJp4hzupEhJXzQ++WXX+Tg4KDy5cvrr7/+Us+ePXX8+HHdvHlTlSpVUlxcnBwdHXXv3j1FR0drzpw5Klq0qL3jI506cuSIWrZsqRIlSqhx48bq2rWrJOnMmTOqUqWKPD091a9fP3Xv3l3Sgw+PY8aM0YwZM7Rz504m9EGaM3LkSIWFhen69et666231KtXL92+fVvt27fXhQsXVKxYMVWpUkULFy6Us7Oz1q9fr+eee07PPfecpk+fbu/4yGBOnjyp9957T9OnT1f27NnVpUsXlShRQiEhIQoPD1flypVVokQJRUZGymq1avbs2SpSpIgiIiJkGIZ8fX3t/RSAVJHwxahhGDIMQw4ODmrdurWWLl2qlStXqkGDBolm5W/Xrp127typPn366LXXXlO2bNnsmP4ZZQAZjNVqNQzDMJYtW2b4+fkZvXv3Ni5dumQYhmGcO3fOaNasmVGnTh1j3rx5ibaLj49/6lmRcfz222+Gt7e3MXDgQOPq1atJ7j9+/LhRokQJI2vWrEaZMmWMRo0aGY0aNTL8/f2N/fv32yExkNTD74OTJ082/P39jdDQUOO9994zHB0djZ49exqGYRi3b982xo8fb9StW9eoUKGC0aJFCyMmJsYwDMNo3LixMXbsWMMw/u/9GPivDh8+bGTNmtWwWCzG4cOHDcMwjLCwMGPnzp3G9evXjVKlShndu3c3DMMwJk6caFgsFqNYsWLGkSNH7BkbSFUJ79EJ/3vt2rVE79tt27Y1vLy8jBUrVhixsbG25SEhIUaOHDmMoKAg4/r16083NAzDMAxGupEhbdmyRU2aNNHUqVPVtGlTeXt720a/E0a8b9++rdatW9tGHQ0Og8S/FBsbq1dffVXZs2dPNLp39+5d3bp1S7du3VLhwoV1/fp1LVu2TJs3b5YklS9fXi1atFCBAgXsFR14pMOHD+unn35S8eLF1aRJE0nS999/r5YtW6p79+769NNPbefGRkVFydPTU9KDSy3OnDmTIzeQqg4dOqQqVarotdde086dOxUSEqKXX37Zdv+iRYv05ZdfauHChfL19dXq1as1fvx4FS5cWMOGDVP+/PntmB5IHQmj22fOnNGsWbO0YcMGnTp1SpUrV1bDhg3Vs2dPSVLr1q21fv16zZ49W7Vq1VLWrFn1wQcfqG7duipZsqR8fHzs/EyeTZy4igwpLCxMzZo102uvvabs2bNL+r/JrfLkyaPPP/9c8fHxWrNmjSIjIyUxayP+vXv37unEiROJZh3/6aef1K9fPxUrVkxlypRRp06ddPv2bXXr1k0LFizQggUL1L9/fwo30pxffvlF5cqV0/Dhw20T/BmGoWbNmmn58uX68ssv1bdvX12/fl2S5OnpqRMnTuiVV17RggUL9NNPP1G4kWoOHz6sKlWqqG/fvvr888917do1XbhwIdE6V69e1bFjx2yT++3cuVOVKlXS5MmTKdzIEBIK95EjR1S3bl2dPXtW1apV07BhwxQREaFBgwbZSvd3331nK+Ht2rVTixYt9Omnnyp37twUbjtiIjVkOFarVfv375ebm5ssFott0qqEUZlz584pMDBQ3377rSQpS5Ys9oyLDMDV1VV58+bVhg0b9OKLL2rZsmWaM2eOypYtqwkTJsjLy0tdunRRuXLl1LdvX9t2HF2BtKhixYqaNWuWunfvrv379+uVV16Rk5OTDMNQ06ZNtXz5cr300kvKnz+/evfuLUkqUqSI3nzzTRUuXJiSg1Rz4MAB1axZU3369NHo0aMlPfjiPOELn4QiUqZMGRUtWlQNGzZUvnz5tGnTJu3bt49/35EhJOznhw8fVtWqVfXOO+9o6NChtiOMGjdurOnTp+vTTz9V5syZNW7cOC1cuFATJ07U8ePHFR0drT179vBlqJ1xeDkypNDQUC1fvlxfffWV7VIIVqtV4eHhGjlypHr27Mm1kJEqEv4xnD17tqZPn64zZ87IarVq3Lhxql27tgoWLChJatq0qZycnLR8+XKKNtKMh2cp/7vPP/9cPXv21Pjx49W/f/9Es+7v3LlTlStXtpVx9mmktuvXr9uuNTxx4kTb8pdfflmZMmXSvHnzEl1ze+XKldq/f7/OnTunAQMGqESJEvaKDqS6P/74Q0WLFtXQoUM1fPhw276f8B5+7tw5DR8+XJs2bdL8+fNVrVo127ZxcXFycmKc1d74CyBdS/iwl3CIeMK32jVq1NBXX32lr776yjbCeP/+fc2cOVMbNmzQkCFD7Bkb6dzvv/+uOXPmqFu3bsqdO7dcXFz0+uuvq2bNmoqIiFC+fPlss+QahqHY2Fg5ODiobNmylBOkGQ8X7tWrV+vGjRuKjY1Vt27dJEk9evSQ1WpVr169ZLFY1K9fP9v+W7VqVUl8mIN5MmfOrHXr1qlSpUqSZCsZ2bJl0+XLlyUpUen4448/1Lp1a75QR4ZjtVr1/fffy9PT03YdbkdHx0RfOgUGBqp79+6aP3++zp07l2h73qPTBv4KSLcSCveqVas0btw43bx5U87Ozurfv786deqkTz75RMOGDdO2bduUNWtWubu7a8+ePdq0aZPy5Mlj7/hIp+7du6dXX31Vv/zyi5YuXaomTZroueeeU7t27ZQ/f37lz59fDx9AZBiGxowZo4MHD+rjjz+2Y3Lg/zxcuAcPHqy5c+cqX758OnnypJYuXarx48erdOnStnME+/btq6ioKI0cOTLR4/BhDmZxcXGxFe6HFS9eXKdPn5Yk26WShg8frtGjR+vw4cNPOyZgOgcHB7Vv316xsbH69ttvdefOHY0fP95WvB0cHGSxWPT888/Lx8dH58+ft3dkPAL/WiLdslgs+umnn9SqVSsNGTJEhQoV0vr16zVq1CidOnVKI0eOVK5cuXT48GFt2rRJJUuW1JQpU1S4cGF7R0c65uLiolatWqldu3YqVaqUduzYobffflurV69WlSpV1KNHD1uZWbJkicLCwrRixQqtX7+e86mQZiTso5MmTdLcuXO1atUqVahQQQsXLlSHDh0UExOjTz/9VGXLllXPnj0VHR2tH374QSEhIRytAbtIGNHz9vbWiRMndOPGDWXLlk0jRozQRx99pH379jHKjQzL19dXXbt2ldVq1fz582WxWDRu3LhEI9579+6Vj4+Pqlevbu+4eATO6Ua6ZBiG4uLi1KFDB/n4+Oizzz6z3Td69Gh9/fXXGj9+vFq1amXHlMiotmzZoubNm2vDhg2qWLGiLl26pC+//FLjxo1T6dKl9dprryk+Pl4nT57U5cuXNWLECBUrVszesQGtX79e169fV9u2bXXr1i0NGjRI1apVU4cOHbR8+XJ17dpVw4cP12effaaAgABNmjRJ5cuXl4ODg+3oIs7hhj39+OOP6ty5sy5cuKBx48ZpzJgx2rFjhypUqGDvaIDprly5opkzZ2r+/Plq2rSpxo0bZ7uvf//+OnjwoBYvXixvb287psSjMNKNdMliscjZ2Vm3b9+Wn5+fpAfXSnZ1ddXQoUN19OhRTZw4kdINU9SsWVPdunXT5MmT9dVXX8nf31/Hjx9Xvnz5VKJECa1cuVIbN25U9+7dNWPGDGXNmtXekQHt3LlTDRo0UIUKFWS1WtW+fXu1atVKJUqU0KFDhzRw4ECNHDlSvXr1kre3tzp37qzOnTtrxYoVKly4MIUbaULx4sWVLVs2tWzZUuvWrdOuXbso3Hhm+Pj42ObdmDdvniRp3LhxGj16tGbNmqXt27dTuNMoSjfSNV9fX23atEnSg8s23bt3Ty4uLqpSpYrOnj2r+/fvy9nZ2c4pkRFVrlxZkyZNkrOzs9544w1t2bJFGzduVIkSJfS///1PmzZtUo0aNSjcSDOuXLkiSfLw8NDixYvl6OioNm3aSJKWLl2qvHnzql27dpIefLHZo0cPXbt2zTYDf8JywJ4sFov+97//6cyZM9q7d6/tCiXAs+Lh4v3dd99p9erV+uOPP7Rjxw6VLFnSzunwOI++TgiQBlit1kf+ryTbRFUhISG6c+eOGjduLOnB+baSdPToUWXNmlXx8fFPMzKeIS1btpSzs7NcXFy0bt06/fTTT7ZL1BQuXFhvvfWWihcvbueUwP9p3ry5OnToIIvFIicnJ82YMUPffvutJOnSpUu6cOGC4uPjFRkZqcWLF6tYsWJauHCh7ZxBIC0ICAjQqFGjdPjwYQo3nhl/Pxs4oXg3adJEDg4O2r17N0d8pHGc04007ezZs2rXrp1WrVolb2/vJNeUtVqtCgsL09tvvy0XFxdVrFhRsbGx+vHHH7Vz506VLl3ajumRUSUcYrt27Vr16dNH48ePV/PmzTn0FmlWwuk38+fP19atW9W1a1dNmDBBV65c0YABA/T888/bCoy7u7syZcqk/fv3c6QQ0qSHL5UEZBQJnyF+//13/fXXX8qaNav8/f0VGBiY6P6HXb16VRaLRTly5LBHZKQAI91I0+7fv6+IiAjVrl1b169fl4ODQ6IRbwcHB9WrV087d+5U/fr1ZbValT17du3Zs4fCDdMk/KOXcG7s/v37Ey0H0oLNmzdr1qxZkh6cfiNJtWvX1tq1a3Xs2DF99tln8vHx0YQJE7R3714dO3ZMgwcPVv/+/XXgwAE5OzsrLi7Onk8BeCQKNzIii8WiZcuWKTg4WL169VKjRo3UsmVLLVq0yHb/38dKvb29KdzpBCPdSPNOnDihjh07Kjo6Wjt37lT27NmTjHg/jG/A8TTNmzdPb731ljZt2qTnnnvO3nEASQ8Kd506dSRJ9erVU/PmzVWtWjWVLFlSixYt0oIFC7RgwQKdPXtWI0aM0NWrV/Xmm2+qffv2tsfgvRQAnp79+/erdu3aCg0NVZs2bXTs2DEtXrxY33//vSZNmqTWrVvbOyL+A0a6keYVKVJE8+bNU+bMmVW1atUkI9737t1Thw4dVLlyZVmtVkYb8VTVqlVLlSpVUkBAgL2jADaBgYGqXr26atWqpXv37um3335TzZo1NXnyZF26dEm3b9/WoUOHVKJECY0aNUoWi0W7du1K9BgUbgB4eg4ePKiSJUuqe/fuypEjh2rUqKG+ffuqcePG+uyzzxQREWHviPgPKN1IFx5XvGNiYtSvXz+tXr1aU6ZMkYODw2NHwAEz5MqVS+vWrVPu3LntHQWwKVSokGbOnKmsWbMqc+bMatasmRYsWKDt27crLCxMmzdv1sSJExUfH6/ixYtr9uzZmjJlir1jA8Azy8XFRX/++acuXLhgW1awYEE1b95chw8ftl2BAukT7QRpxt/PdHj43G0pcfGuVq2awsPDNXz4cM2aNUtbt25V5cqVn2ZcwMbNzc3eEYAkChcurLFjx+r+/fuaMGGC8uTJo++++04ff/yxunTpopCQEDk6OsowDOXLly/JnBkAAHM86uzevHnzysPDQ6tWrVJkZKRtefHixeXv76/bt28/zYhIZZzTDbtKODf74RkZjx8/rgIFCtgm/vm7EydO6PXXX9fPP/8sNzc37dixQ+XLl3+asQEg3Th58qR69uwpSRo6dKiqV69uu++f5scAAKS+hM+8+/bt08WLF+Xk5GS79G2/fv00d+5cDRs2TPXr11fu3Lk1atQoLVmyRLt375avr6+d0+PfonTD7v744w/169dPK1as0PLly9W/f3+tXLnyH2cfP3LkiEJDQzVo0CBmKQeAJzh58qR69eolSRoyZIiqVatm50QA8OxauXKlOnbsKD8/P928eVO1a9fWd999J0kaMGCA1qxZo/DwcBUqVEjnzp3TunXrVK5cOTunxn9B6Ybd7du3T/Xr11f+/Pl18OBBffvtt+rQocMTt7t3755cXFyeQkIASP9OnjypPn366PLly5o1axZfWALAU2YYhuLi4tSmTRs1b95ctWrV0qFDh9StWzeVL19ea9eulfRgJvNz587JarWqYsWKypMnj52T47+idCNNGDdunD744AOVKFFCR44ckcRhjwCQ2o4fP66vvvpKH330Ee+vAPCUJBxSfvPmTcXFxWnw4MEaOHCggoKCZLVatX37drVt21blypWzFW9kLJRupAlLly7VkSNHNHfuXBUoUEBhYWFycHBIcp1YijgApA7eTwHg6VmxYoVGjBihbNmy6ciRI1q3bp1tEmDDMLRt2zZ17NhRBQoU0NatW+2cFqmN0g27eHjitIc/+P38889q1aqVgoKCtGnTJtv627ZtU+XKlR87uRoAAACQViRULIvFov3796tJkybq1KmTMmfOrJkzZ6pw4cJatGiRfHx8bOtv3LhRPXv2VFhYmAIDA+0ZH6mM0o2nLqFwb9q0ST/++KNOnjypV155RRUrVlTRokW1Z88etWrVSoUKFdIXX3yhb775RkuXLtXWrVvl5+dn7/gAAADAI92+fVuZMmWy3T58+LAOHDigM2fOaNSoUZIenOpTr149FS9eXPPmzUtUvO/evSt3d3e7ZId5KN2wixUrVqh9+/Zq1qyZoqKidPjwYVWsWFHvvfeeatWqpYMHD6pNmza6f/++4uPjtXz5clWsWNHesQEAAIBHGjlypHLkyKG3335b0oOjOfPkyaPLly+rffv2mjdvnm3dhOJdunRpff3111wOLIOjdOOpu3Dhgho1aqQ333xT77zzjiQpLCxMU6dOlZOTkyZMmKBChQopNjZWu3fvVpEiReTv72/n1AAAAMDjDRs2TG3btlWJEiVsV9m5cuWKateurbt37+q7775T2bJlbadY/v777ypfvrwaNmyoJUuWMM9GBuZk7wB49jg4OOjmzZsKCAiwLatbt64Mw1Dnzp119OhRFSpUSK6urqpZs6b9ggIAAABPkHDq5IcffihJ2rJli/bv36+2bdsqV65c2rRpk8qXL69evXpp+vTpKlmypCSpaNGiOnTokCwWC4U7g+Ovi6ci4YAKwzAUExMjZ2dn3bx5U5J0//59SVK9evVUsGBBLpUAAACAdCNh5Drh8+6qVas0ZswYLVmyRJcuXZKPj4/279+vM2fO6O2339axY8ds2xYuXFhBQUF2yY2nh9INU/397AWLxaICBQqoQYMG6t27tw4dOiRnZ2dJD857cXd3V/78+e0RFQAAAEixhM+7V69elSRNmjRJ3bt31+TJk7Vw4UJdunRJOXPm1IEDB3T+/Hm1bdtWv//+uz0j4ynj8HKYJuFQm82bN2vFihWKj49XQECAhgwZomnTpik8PFzVq1fX2LFj5enpqd9++0379u3TtGnT7B0dAAAAeKKEz7tr167VjBkz9MYbb+ill15SaGiorFarpkyZIklq166d/P39tXv3btWpU0dubm52To6niYnUYKqEWcpbtGiha9eu6ciRI8qVK5dWr14tX19f9e3bVxs3blRsbKy8vb01bdo0lS1b1t6xAQAAgGRZvny5OnbsqJEjR6pu3bqJPsv2799fS5YsUZ8+fdSqVSvlypVLVquVc7ifMZRupIpHvXlcvnxZtWvX1uuvv67+/fsrPj5ep0+fVuvWreXq6qo9e/ZIki5duiR3d3dZLBZ5eXnZIz4AAACQYidPnlTDhg01cOBAvfnmm7ble/fu1XPPPSdJGjRokD777DONHz9e3bt3l4ODg+08cDwb+IoF/1lC4T5w4IA+/PBD23ktd+7cUVRUlKpWrSpJcnR0VOHChbVgwQKdP3/edriNr6+vsmbNSuEGAABAunL16lVZrVa1bNlS9+/f19SpUxUcHKzatWsrODhYhmFo3Lhx6tu3r+rVqydHR0cK9zOI0o3/JKFw//rrr6pUqZJu3bpleyNJuLb2xo0bE21ToEABBQYGKiIiQpI4vAYAAADpQsLg0vXr1yVJefPmVdasWfXSSy+pdOnS2rBhg6pWraqdO3dq9+7dmjp1qiRp5MiRKlSokN1yw76YSA3/WkLhPnz4sF544QUNGjRIY8aMsd3v5uam1q1ba/369SpSpIhatWplW54jRw45OT3Y/RImoAAAAADSqoTPrOvWrdOCBQvUuXNnvfjiixozZozWr1+vbNmyqVOnTsqXL58sFouCg4Pl5+dn79hIAzinG//JqVOnVKpUKfXv3992aLnFYtHcuXNVpkwZZc6cWf369dOVK1cUHBysatWq6ccff9TcuXO1d+9eFS5c2N5PAQAAAEiWhydNa9CggUqVKpVknfv372v06NGaOXOmdu7c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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean price foot locker: 104.67€\n",
      "mean price asos: 41.02€\n",
      "mean price mango: 43.13€\n",
      "mean price zara: 72.45€\n",
      "mean price massimo dutti: 96.88€\n"
     ]
    }
   ],
   "source": [
    "# Average prices for each brand\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "brands = ['Foot Locker', 'ASOS', 'Mango', 'Zara', 'Massimo Dutti']\n",
    "average_prices = [mean_footlocker_df, mean_asos_df, mean_mango_df, mean_zara_df, mean_massimo_dutti_df]\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(brands, average_prices, color='skyblue')\n",
    "plt.xlabel('Brand')\n",
    "plt.ylabel('Average Price (€)')\n",
    "plt.title('Average Prices of Each Brand')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "print(f\"mean price foot locker: {mean_footlocker_df}€\")\n",
    "print(f\"mean price asos: {mean_asos_df}€\")\n",
    "print(f\"mean price mango: {mean_mango_df}€\")\n",
    "print(f\"mean price zara: {mean_zara_df}€\")\n",
    "print(f\"mean price massimo dutti: {mean_massimo_dutti_df}€\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "0b125203-2e2b-4e57-a162-66e4fcaaa6ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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XbNZrlatWvree++97vJeu9jb7t27d1X16fabNm1adXd316CgIJuDvW7duuk777yTZAOm9Uyj6v999p9++klLliypN2/eVFXVrl27arZs2fTIkSPat29fLVmypObMmVNDQ0MTzRnJxObAgQOaK1cuLVeunJYsWVJz5MihVatW1aJFi2q5cuW0cuXKWq9ePaPVKrl70cHovXv3dPjw4S8MTGvWrDF+S2FOVFSUNm/eXF1cXHTSpElxTlYGBgaqt7e3Llu2zE4Vvl6xTxZFRUXpTz/9pJ07d1ZV1fPnz2vu3Lm1c+fOOmrUKM2UKZMGBgZqcHCwPUt+razrZt26dRoYGKg7d+5UVdVPPvlEmzZtqkFBQfrHH3+o6tPvbYkSJXT79u12qzc2glQSEvtAo1atWporVy595513npvK7969q0OGDNFMmTLp6dOnX3epdhMVFaWqqrt27dJixYppWFiYPnz4UH19fdVisWhQUJDN8n379tVq1arpnTt37FFuihX7AHjXrl1GmFq3bp0xPTQ0VNeuXat169bVIkWKGK0uyfXg2fq5Vq9ercWKFdOhQ4fqw4cP9e7du9q9e3fNkiWLrly5UlVVb968qQMHDlRPT089efKkPct+aSdPntTq1avrkiVL9NGjRzbz6tSpo127dtVOnTqpt7e3HjhwwOZ5169ff93lJlqxvw/W/Z/q026SZcuWVYvFol9++aUuXrxYJ02apNOmTdOpU6fqqVOn7FHuaxc7RG3YsEFXr15tc/AeFhamQ4cOVYvFogsWLHjuaxCm/tmLgmp0dLQ2btxYAwICdOnSpXG65o4fP95mm00JfvnlF126dKneu3dPz5w5oxEREVqvXj2bE4X58uVTLy8vDQwMTFHrZ9WqVZoqVSodOXKkHj9+3Jhu7Z1gNWTIEM2bN69euXLldZf4XASpROx5B4xr1qzRtGnT6uDBg3XdunVaoUIFLVeunNE8rKq6fv16bd26tebIkUMPHTr0Oku2i9mzZxtndqw2b96sVatWNR7/8MMP6ufnp2+//baeP39ef/vtN/3oo480Xbp0evTo0ddcccoU+8f22W17x44dWrlyZW3UqJFu2LBBVZ928+vRo4c2a9bMOJBJ7gc069atU1dXV501a5aeP3/emL5//37t0qWLOjk5aaFChfSNN97QnDlzJtnvd1RUlNauXVstFotW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jm7evFlVn25zZcuW1YCAAD1z5ozev39fo6KitFmzZrpkyRKboeMRP9Ztb9OmTca0NWvWaN26dbVNmzYaHBys0dHRunHjRm3UqFGKWLfR0dHG5/z999+NAB/7d61q1aqaLVs2nTJlin733XfGADDW27YkV7du3dL9+/fr3r17NSwsTC0Wi2bIkEHHjh1rs9yKFSu0VKlS6unpqfnz59ecOXPG6Z2VVBCk7ODmzZtavHhxLVasmM1NA2fNmqWOjo7GMJCqqp999pk2aNBAc+fOrRUqVEiyG9p/cfbsWW3atKk2adJE9+zZo5cuXdLvvvtOK1asqGXKlNFUqVJpQECAWiwWbdGihb3LTRGebUFauHChzXUun332mTo4OOhXX30V57m//PJLsu/GZz1gW7lypfr6+mrhwoW1dOnSmjNnTuOH1BqmcubMqY0bN7Znuf/Z7du31dPTM87fO/Z20rNnT82VK5du2bLFmHbhwgWuYYzFut3s3LlTJ06cqD169DC6P968eVO7du2qefLk0ffee0+nTZumH330kbq4uBjdrFKS6dOnq5eXl1aoUMGmu9758+e1cuXK6unpqUWKFNFChQqpv7+/sc9JCQf6CWXlypVqsVjU29vb5nur+nRkuowZMxrd7mOH+OS+jmPv32vXrq1169ZVNzc3zZo1q37xxRfGch07dtQyZcpo7ty5tWLFisn+2vYTJ05oxYoV9c0339SmTZuqquq0adPUYrFoq1at9NatWzbLX7t2TY8cOaI7d+40BiVKighSr5l1B3P//n0tV66cBgQEGC1TEREROmPGjDhhSvVpyg8LC3vt9SYWp0+f1rp162rt2rV13759xvT79+/rokWLdPDgwVqyZMkUGTTtKTo6WsPCwtTFxUUrVKhgc0A3atQodXBwMO4X9KzkGqZiD/OeIUMGI1xYuz16eXkZAy2EhobqvHnztFChQkn6HmdRUVE6YMAAdXV11fnz58eZZ1W1alXj+q+U1J3TjJUrV2qmTJn0rbfe0jZt2qiTk5P27dtXo6OjjdYBDw8PzZs3r44ZMybFDHH+rN27d2vp0qXV3d3d+A2NfTA/f/58nTRpko4fP57R+V5SeHi4vv/++2qxWHTWrFkaExNjs47z5cunn376qR0rtJ8DBw6om5ubzpw5U69evap79+7V9u3bq7+/v06dOtVYLjg4WIODg5P9PaOOHz+u6dOnN+4lFrunyowZM9Risehnn32WLNcDQeo1swap48eP6+rVq9VisWjlypVtWqasYSp2Nz88HfGrbt26WrduXd22bVuc+cn1wDyxif1Dag33169fV19fX61SpUqcMOXi4mIM4ZxcrVixQnfu3Gk8fvDggX700UfGDVGvXr2qOXLk0Pbt22u9evXU09PTGBDlwYMHSXaUtcuXL+ucOXN06tSpumrVKp0+fbo6ODjECVPW7+agQYNsRviCrdOnT2uuXLl07ty5qvr0u+bg4KBDhgwxvnfXrl3Ttm3batOmTZPEPVYSwvNaOCIjI/XAgQPq7++vZcuWNW4T8GxXYytC1D+LvY5j7+MjIiK0TZs26uHhoRs2bDCWu3fvnubNm1dnzZr12mtNDObOnatFihQxrmFXVT116pS2bdtWvb29je9wSnD37l2tVKmSMdCLVexjsi+++EItFouOHj06yf7evQhByg5WrVql6dKl048++kgbNWqkvr6+GhAQEKebn8ViidMfPqX7888/9c0339S6devGGT4Tr17sH9uZM2fq6NGj9fr166r6NExlzZo1Tpjq37+/VqpUKVlevxETE6PBwcHq6empjRo10j179hjztmzZonv27NGQkBAtXbq0duvWTVWf3lTVYrGoo6Njku7q8ccff2jOnDm1WLFimi5dOvXw8NBx48bpl19+qRaLRRcuXBjnOe+9916KvZ4nPg4dOqSVKlVS1aehKnv27Pr+++8b862/ERcvXjS+d8ld7H3Onj17dP369Xr06FHjRt8HDx7UXLlyaaVKlYwQRWgyJ/Z3ccGCBfrJJ5/oN998Y9N60KJFC02bNq0GBgbqxIkTtVGjRin6hsZr1qxRHx8fPXr0qM307du3q5ubm6ZJk0Znzpxpp+perxMnTmiePHl027ZtcU56xN7XT5061RhwKjmFKYLUa3br1i3NmzevcbPdqKgoPXPmjJYoUcImTIWHh+vcuXONeyLh/1hv4lquXLk4w6Lj1Ym9g7xw4YJWqlRJc+bMqV988YUxGps1TFWtWtUmTFl3pMn14PnAgQNasGBBbdq0aZyAv3PnTi1Xrpzx3d63b582a9ZMO3funGS7Zf3xxx+aOnVq/fjjj/XevXv6+++/a/v27dXLy0u3b9+uQ4YMUUdHR500aZLeuHFDb9y4oYMHD1YvL69k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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product Count</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>adidas</td>\n",
       "      <td>526</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Nike</td>\n",
       "      <td>499</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>adidas Originals</td>\n",
       "      <td>276</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>New Balance</td>\n",
       "      <td>230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>PUMA</td>\n",
       "      <td>194</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Reebok</td>\n",
       "      <td>166</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Jordan</td>\n",
       "      <td>137</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Champion</td>\n",
       "      <td>119</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Diadora</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Crocs</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Product Count  count\n",
       "0            adidas    526\n",
       "1              Nike    499\n",
       "2  adidas Originals    276\n",
       "3       New Balance    230\n",
       "4              PUMA    194\n",
       "5            Reebok    166\n",
       "6            Jordan    137\n",
       "7          Champion    119\n",
       "8           Diadora    100\n",
       "9             Crocs     90"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Top 10 brands (Footlocker) \n",
    "top_10_footlocker_brands = footlocker_df[\"titled_brands\"].value_counts().nlargest(10)\n",
    "top_10_footlocker_brands_df = top_10_footlocker_brands.reset_index().rename(columns={'index': 'Brand', 'titled_brands': 'Product Count'})\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "top_10_footlocker_brands.plot(kind='bar', color=\"skyblue\")\n",
    "plt.title('Top 10 Brands by Product Count in Footlocker Data')\n",
    "plt.xlabel('Brand')\n",
    "plt.ylabel('Product Count')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()\n",
    "\n",
    "top_10_footlocker_brands_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b50d7fb5-b252-403e-9418-d11e855c8f81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Sales Volume by Promotion Status: Promotion\n",
      "No     240312\n",
      "Yes    215244\n",
      "Name: Sales Volume, dtype: int64\n"
     ]
    },
    {
     "data": {
      "image/png": "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7N69W6xbt048+eSTws3NTVy8eLFkuuvXrwsAYunSpSWXRUVFCW9vbxERESG++eYbsX37djF58mShVqvFjBkzSqb74IMPhEajEdOnTxc7duwQW7duFXPnzi01TXmMRqMIDQ0V7dq1K3W5wWAQwcHBomvXrkKIqj8HQggRGhoqRo0aVfL70qVLBQBx/fr1UtPt3LlTACj1+Pfs2VP4+/uLFi1aiK+++kps27ZNDBo0SAAQM2fOFBEREWLlypViy5YtomvXrsLFxUXcvHmz2o9XRQCIBg0aiFatWomVK1eKjRs3iv79+wsA4scffyyZbsiQIaJhw4bCYDCU+vthw4aJevXqiaKiogpv487z/NFHH5W6/PTp0wKAGDFiRKnHLSQkRIwbN0788ssv4qeffhIGg0GMGzdOABCTJk0SW7duFQsXLhQBAQGiQYMGIiUlxWyP565du4STk5Po2LGjWL16tVi/fr3o27evUKlUYtWqVUIIIZKTk8WsWbMEAPH555+XvPeSk5OFEMXv59DQ0JJ5mkwm0a9fP6HVasXUqVPF9u3bxccffyx0Op1o3769KCgoKJk2NDRU1K9fX7Rq1Up88803Ytu2bWLYsGECgNi9e3elz2VV36M3btwQr732mgAg1q5dW5I/KytLCCHEe++9J/773/+KzZs3i127domFCxeKRo0aid69e5fMIzo6WgwdOlQAKPn7gwcPioKCgnLf13fc+1nTr18/ERAQIL788kuxa9cusX79ejFt2rSSx7oie/bsEQDEli1bKp2usLBQPPzww8LZ2VkcPHiwzPVffPGF+OCDD8TGjRvF7t27xfLly0Xbtm1FixYtRGFhYcl006dPFwBEaGiomDJlivj111/F+vXrhRBC/Pjjj2LatGli3bp1Yvfu3WLVqlWiZ8+eIiAgoNRr844BAwaIDh06VJrbXjh0ES9cuFAAED/88EOp6WbPni0AiO3bt5dcptPpSpVARQwGgygqKhKRkZFiyJAhpa6rShELIcS7774rnJ2dBQABQDRq1EiMHz9enD59+r63XVhYKJo1ayb++c9/llxe3hu2X79+on79+iUfCndMmjRJuLq6ivT0dCGEEIMGDSpTplV150114sSJkss2bdokAIjFixcLIar3HNS2iAGIY8eOlVyWlpYmNBqNcHNzK1USp06dEgDE//73v5LLqvp4VQSA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",
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Relationship between sales volume and promotion (Zara)\n",
    "total_sales_volume_by_promotion = zara_df.groupby('Promotion')['Sales Volume'].sum()\n",
    "print(f\"Total Sales Volume by Promotion Status: {total_sales_volume_by_promotion}\")\n",
    "\n",
    "plt.figure(figsize=(8, 6))\n",
    "total_sales_volume_by_promotion.plot(kind='pie', autopct='%1.1f%%', startangle=90)\n",
    "plt.title('Total Sales Volume by Promotion Status (Zara)')\n",
    "plt.ylabel('')  \n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "8efc3729-710e-4449-8ed1-db2b016344d1",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "image/png": "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V9OmTfX9999r4MCBqlevns6fP68NGzZo//79qlGjhtavX6969eqpbt26evrppyVJgYGBkqRBgwZp7ty5GjdunMqXL6/Tp09r69atOnbsWIprApCOGQDghujatatlzZrV+f311183SbZo0SKvdi+88IJJsq+//trZJskyZ85s4eHhzrbz58/b7bffbkWLFr2qOpo3b26FChW65G3FihWzxo0bJ9t+6NAhk2Tjx4+/7ONu2LDBJNkTTzxxRXUsW7bMJNnEiRO9tr///vsmyd544w1nW506daxOnTrO71fbd0FBQXb8+HGvto899phlz579imq9mCQbNWqU8/usWbNMkvXp08er3cSJE02ShYWF/ePjjRo1yiT940/S529mtnPnTrv99tutePHi5ufnZ59//vk//o09e/aYJJs0aZKdPHnSsmXLZtOmTTMzs6FDh1rhwoUtISHB+vbta1eye5BYc3h4uMXFxVlkZKTNmzfPMmfObAUKFLCzZ8+a2YV/O0m2YsUKr/s/8cQTJsl++OEHr+2PPvqoeTwe27lzp5mZzZgxwyTZp59+6tWuV69eJslmzZrlbLv4dZKoa9euXq/5OXPmmCR78803//E5Zs2a1bp27Zpse5kyZaxNmzb/eF8AuFJMWQQAl6xcuVJZs2ZNNrr10EMPSZJWrFjhtb1+/frKmzev83vGjBnVoUMH/fnnnzp48OA1q+ufFmK4los0JI4aJT7fRO3atVPWrFmTPf+L73s1fVevXj3lyJHDa1uVKlV04sQJPfDAA/r0008vu8Lh1WjVqpXX74kji4nT9/7NN998o02bNiX7KVKkiFe748ePq0GDBmrYsKF+++03NWrUSPfee6++/PJLp828efPk8Xi0Z8+eZH8ncVrqO++8o/Pnz2vOnDnq1q1biv59Q0JC5Ovrqxw5cqhTp06qUKGCli1bpkyZMjltcuTIoXr16nndb+XKlSpVqpSqVKnitf2hhx6SmTmvj1WrVikgICBZ317JAjOX8+WXXypTpkzO1MmrVaVKFX355Zd64okntHr1ap09ezbFtQAAUxYBwCXHjh1TSEhIsp3g4OBg+fj4JJv+FBISkuwxErcdO3bsmqz6lytXrktOuzp+/LgkKWfOnJe9b8GCBSXpkgHgUo4dOyYfHx+vqW3ShdAXEhLyj9O/rrbv8uXLl+wxOnfurPPnz+vN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FezAgQO65ZZblCtXLhcru3ls2rRJjzzyiMaMGaPVq1dr3rx5+uabbxQdHe12aTc1M1NkZKRefvlljR07Vs8++6xat26t33//XS1btlSlSpXcLjHVMzNFRUXpu+++07Rp01S/fn1t3rxZn3/+uSZPnqzKlSs7OzVpSeKR4WXLlql79+6qV6+eevTooc2bNytjxoxul5eqJR29GTVqlFq3bq077rhD7dq105QpUySxA3wtREZG6rvvvtPbb7+tFi1aaOfOndqyZYvGjRunAgUKOOe7pPfwW6xYMc2aNUsnT57UtGnTtGzZMkkXDiT7+vpKurnODbqRTp8+rbfffltjx47VsGHDVK9ePX355Zfq27dvuvj+vNx7p1q1ajp79qwzbTE1HqQjkKVDe/bs0WOPPaZFixbp5MmTkqTjx4+z03IFEr8Efv75Z1WqVEkPP/ywdu/erZ49e6pXr14aNGiQJHG0M4U8Ho8yZ86s6OhoNWvWTHv37lXRokXVunVrZ8fwm2++0Z9//ulypalL0i8hj8cjX19fRUREqGTJklqyZInatm2ryZMnq0ePHoqNjdX8+fO1bt06Fyu+9jwejz799FPdc889Kl26tDp06KCoqChVqFBBBw8edLu8VC0xbI0dO1YzZszQ8OHD9euvv+rw4cN6/fXXtXXrVpcrvDldvHN44sQJbd68WRUrVtTy5cvVqVMnjR8/Xo8++qjOnj2r559/XuHh4YRfSVWrVtXzzz+v6OhoTZ06VV999ZXy58+vW265RcePH1dkZKROnjypU6dOpfpzg663pK+z+Ph47dq1SxUrVlRYWJjuvPNONWvWTK+++qok6YMPPtCvv/7qVqnXXeJ7Z/HixVq9erXze/Xq1VW1alU99dRTio2NTZ37u4Z0aejQoebn52dvv/22mZm9/PLLVrduXZerSl3i4+Od/4+NjTUzs+joaDMze+655+yRRx6xM2fO2C233GIPP/yw037p0qU2depUO3ny5I0v+iaUkJDg9d+DBw9a0aJF7bXXXrOiRYtaz5497fz582Zmtm/fPnvggQfs888/d63e1Cax38z+9/o8fvy4VahQwVq1amU5cuSw6dOnO212795tTZo0sQ8++OCG13o9RUVFWf369e3FF180swuvo4IFC1qvXr282iXtL1yQkJBg4eHhVrNmTVu8eLGZma1atcqyZMlib731lpn97zMQKRcbG2tt2rSxbt26WbZs2ezNN990bvvrr7+sUaNG9umnn7pYobsS35tJv3vXrVtnd911lzVo0MAyZMhg/v7+VqJECStYsKDlzZvXQkJC7MEHH0xX7+vE/jlz5oyz7fvvv7e//vrLzp07Z82bN7dJkyZZ4cKFrVevXk77sLAw69atmy1YsCBN99evv/5qtWvXNh8fH+vbt6/NmzfP2V6rVi1n/yHp6yw1IJClM3Fxcc7/Dxw40Hx8fOyDDz6w0aNHW8eOHe3EiRO2a9cuCwsLsxMnTthPP/1kJ06ccLFid/3555+2ZcsWMzP78MMPbdCgQWZmtnjxYvN4PBYYGGhDhgzxemM/8sgj1rFjRzt16pQrNd+M1q9fb08//bTTZ2PGjDGPx2PNmjXzavfkk09a6dKlbd++fW6Umeokfd19+OGH1rp1azt48KCZmS1ZssSyZs1qzZs3d9pGRUVZs2bN7O6773ZCblpx+PBhK1SokG3fvt3Cw8OdAyWJFixYYOHh4S5WmLpcvEN29OhRK1eunB0/ftwWL15s2bJlsxkzZpiZ2dmzZ23evHm2fft2N0q9qU2YMMEGDBjg/D5o0CDz9fW1hx56yNl28uRJa9q0qTVo0CDNvS+vVNLPsgMHDtjJkyctJibGzMzWrFljd911l1WvXt2eeOIJ2717t+3YscNWr15tP/zwg9d+TXpx4MABK1GihO3cudMWLVpkmTJlsm+++cbM/vf92bhxY68DKSNGjLASJUrY3r173Sr7urhUsDp37pwtXbrUWrRoYSVLlrTatWvbggULrGjRotavXz8Xqvx3BLJ0JOkIRKIBAwZY5syZrVixYpYxY0YrVaqUZc6c2UJDQ61w4cIWEhJiERERbpXsqjNnzljnzp0tc+bMNnnyZPN4PDZnzhzn9kGDBpmfn599/vnnFhcXZ4cPH7YnnnjCcufObdu2bXOx8ptLQkKCPf7441a6dGkbNWqUnT592iIjI61Hjx6WIUMGmzBhgk2YMMF69+5tAQEB9ssvv7hdcqqQ9Evou+++sw4dOliuXLmsZ8+e9vfff5uZ2auvvmoej8caNGhgDRo0sLvuusvKlSvnfEnfzDt/FweKqKgoa9GihU2dOtUKFixojzzyiLOjdujQIevcubN9/PHHbpSa6iTtu8Sj7BEREVagQAHr3LlzslHV7du3W6NGjezLL7+84bXe7N58803zeDz25JNPmtmF92379u2tdOnS1rhxY3vkkUesZs2aXu/L1Hbk/kYaNWqUlShRwipUqGC9e/e2Y8eOmZnZ2rVrrU6dOtaiRQtbvnx5svvdzJ9lVyNx5s25c+esdevWlidPHsuQIYO9++67Xu369+9vmTJlsqFDh9rw4cOte/fuFhgYmOa+P5O+V7766it7++23bf78+c534NGjR23fvn123333Wfv27c3Hx8cyZsxoK1eudKvkyyKQpROJX8BLliyxBg0a2KxZs5zbnnnmGfN4PDZs2DD77bff7Pfff7ddu3bZ7t27nRd1epJ0ysj+/futQoUK5uPjY+PGjTOz/40ybt++3R5++GHzeDxWsmRJq1SpkhUuXNh+/vlnV+q+mZ09e9aGDRtmVapUsdGjR1tMTIydPn3ann/+eStXrpzVqFHDHnzwQfvtt9/cLjXVefzxx61ChQrWo0cPq127tgUHB1uXLl3s0KFDZnZhys+gQYNs0KBBNm3aNOf1mxaOKi9btsymTJni/N65c2fzeDx2zz33eO2gDR8+3MqUKWMHDhxwo8xUJekOzLx58+zxxx+3w4cPm9mF8JAlSxZ74IEHnLanT5+25s2bW/369dPNTm9KXa5/5s+fb76+vjZkyBAzu/B9PGPGDOvWrZt16dLFxo4dm6bel1cj6etx4cKFlidPHps3b54NGjTIatWqZbVq1bKjR4+a2YWRsrp161q1atVs/fr1bpXsmoEDB9qgQYOc18inn35qHo/HsmfP7szkSXqw5YUXXrDWrVtb9erVrXfv3rZ161ZX6r4Rhg4dakWLFrVKlSpZo0aNLDAwMNnz3b59u7311lsWGhpqzzzzjJmlroMfBLJ0ZPHixebv728vv/xystAwZMgQy5Qpk82dO9fOnTvnUoXu27Rpk+XMmdPZcTt+/LhVrlzZSpcubbfccott3rzZzLw/9FasWGFvvvmmLV68mB2+f5GQkOB8AO7fv99rB+bcuXM2ePBgq1Klij377LPOkfvEI6Tp+XV5OV999ZXlyZPHfvjhB2fbxIkTrXLlyta1a1dnNPziHcW0sGN9/vx5Gz9+vHk8HnvppZec7bVq1bKiRYvayJEjberUqdazZ08LCgpy3rvpWdKdjy1btliDBg2scOHC9uyzz9rx48ft1KlT9sQTT5jH47H27dvbAw88YHfffbeVLVuW0Zt/cPFo7U8//ZSszbx588zX19eGDRt22cdJC+/Lq5G03z755BObMGGC1yyUJUuWWI0aNaxmzZpOKFu5cqX17ds3Xb4Ov/zyS699t6NHj9qiRYusXbt2FhwcbGvXrjWz5O/RmJiYNB3033nnHQsODraNGzea2f9GpRctWnTJ9m+//bblyJHDwsLCbmSZ/4pAlk5ERERYtWrV7Pnnn/fanjhH28xs8ODB5vF4bO7cuWn6hM9/EhcXZ8ePHzczc86XOHbsmO3cudNat25t+fLlc4b8E788CQr/7q233rLvvvvO+X3z5s1WtWpVe/nll712Qk6fPm29e/e2fPny2bhx47zOw0uvr8lEHTt2TDbN4uOPP7aQkJBk5wQ8/fTTljlzZuvWrZszyp2QkHBT9+HFi7+YmZ04ccImTpxoHo/HJk2a5Gx/+OGHrW7dulauXDl74IEHGFm9yMCBA61WrVrWtm1bK1u2rOXIkcOeeeYZi4qKMjOzzz77zO677z7r2bOnjRs3Lt2O3lyJvn372qpVq5yd4DVr1pjH47Fp06YlaztjxgzzeDz2wgsv3OgyU5VGjRp5jXD9/PPPVqpUKcuWLZstXLjQ2X7+/HlbsmSJ1axZ0+66665kp0+kp1CW9HNv6dKl1rNnT2dfJTY21lq3bm3BwcG2YcMGp92CBQtsz549N7rU6+7if/dhw4bZyJEjzezCd2K2bNnsjTfeMLMLC10lroOQuK+xa9cuK1u2bKr7XiCQpRN79uyx0NBQ++KLL5LdlvSNPmLECM5/MrO///7bMmTIYI899piz7ZdffrE2bdpYaGio/frrr2Z2YUrA0KFD7dy5czf1zu71tH//fqtfv76VKVPG+bI4evSotWrVyu666y6bPn16slBWoEABK1iwoDNNNL3buXOnPf3008lWulu+fLnddtttTthN/KKKjo62W2+91SpWrGh9+vRJEwvzJL6/Lj6qGRUVZRMmTDCPx2OTJ092tp85c8ZOnz7N6oAX+fjjjy1Hjhz2888/O33Tv39/K1WqlI0aNcoZibg4fKW30ZsrVahQIStRooStW7fOEhISLDY21saOHWu+vr5e5+GZmW3dutVy5sxpHo/HWTAlvTl48KCNGjXK62DwyZMn7fXXX7fixYvb3Xff7XWQMz4+3r744gsrVqyY9e7d28w4OLdkyRLzeDzWr18/5/MwcQXPPHny2KxZs2zgwIEWFBRku3btcrnaayvpv/0333xjJ06csF69etnw4cPts88+81qMKCEhwd544w2bMGGC1/fAs88+ax6Px5nWn1oQyNKJv/76y4oXL+4s/2n2vxf2mjVrnOXvcUFMTIy9/fbbljVrVmdlRbMLIzv33nuvZcyY0Vq3bm0ZMmRIcyfJXg+rVq2ydu3aWfny5e377783swuh7P7777caNWp47ZwcOHDA2rVrZwMHDrT9+/e7VXKqNWPGDHvvvffM7MJ7uEKFClalShWvI6G7d++29u3b2/Dhw61EiRK2adMml6r9b2bNmuU1+rd9+3bLkiWL17QmswsjZYnnwvJZ9j8DBgxwpvEkmjVrlhUtWtSOHDnitXPTs2dPy5Ytm40aNcprJCK97/xeTtKj9FWqVLFixYrZunXrzOxCmH3uuefM4/HYa6+95rQ7ePCg9evXz7766itGG81s0qRJzjnbZ86csbffftvKly9vHTp0SBbK1q5dy0GBJJYsWWIZMmSwPn36eB2k6tSpkxUvXtzKlSt3yamzN7Okn0UjR460MmXK2I4dO+zFF1+022+/3QIDA71Gpo8fP27NmjWzUaNGeT3OJ598kir7hkCWjtStW9fuuOMO2717t9f24cOHW5s2bZxrGKU38fHxl7z+SVxcnM2dO9f8/Pzs8ccfd7YfPHjQXnnlFevfvz/LQF/GpXbiVq5caW3btr1kKKtZs6aNGjXKduzYYSNHjrQWLVqkiVGday08PNzuvfdeK1asmH344YdmdqEPixYtauXLl7dXX33VFi9ebA0bNrT27dubmVmuXLluypHG6Ohoy5s3r1WoUME5N3Pfvn32yCOPWM6cOZ1Qmuj333+3oKCgZDvB6dXGjRvtscceS7bjP2fOHCtQoIATdBNHKg4dOmS5c+e2SpUq2cSJE+3s2bM3vOabWaVKlaxo0aJOKIuNjXXOcRw8eLAtXLjQmjVrZs2aNXM+H9NbKDt27JhFRUU55wffc889li1bNlu2bJmZXZgd8cYbb1ilSpWsQ4cOXqNoidJLKLv4NbJz5077/vvvLSwszAmrn3766SVD2e7duy0yMvKG13yj7Nmzx9q0aeMs83/u3DmrVauW5c6d25YuXWphYWH2xx9/WJMmTaxSpUpOH6b2g0sEsjQm8QX366+/2oIFC2zJkiXOSjNHjhyx4sWLW5kyZWz69Om2YMEC69u3rwUEBDgr9KQne/bs8RrG/vrrr23IkCH28MMP286dO51wNmfOnGShzCx9zV+/Gon9cuLECYuIiPBa6ORyoWzAgAFWokQJCwkJsUKFCqXKo1duuNQXyKZNm6xHjx5WsmRJ56TlU6dOWZs2bezOO++0woULW/369e306dNmduHo/fz5829o3dfK/v37rVSpUlalShVngZIDBw7YgAEDLCAgwCuURUREWNeuXe3ll19m2vX/S3z9zJs3z1myPi4uzooUKWKNGjXyCgS//fabPfjgg9atWze77bbbGJ3+B7t27bKNGzcmW4X44lBmZjZ79mwLDg62cuXKWe3atZ3vnNS+c3itLVq0yOrWrWvFihWz6tWr2969e+3o0aPWrVs3y5Ejh/P6TAxlVatWtYYNG6bLKcezZ8+2iRMnOoH0/ffft9DQUMuVK5fdcccdNmnSJOeAZWIo69+/f5pdVCzpe2Xq1Kl26623WtWqVe2vv/5ytp8+fdpq1qxppUuXtixZsli1atWsZs2aN9UlXghkaUjii/ajjz6ykJAQq1ChgpUuXdrq1atnS5YsMbML0wJatWplFStWtCJFili9evXS5epjCxYsMH9/f/vqq6/M7MK5OL6+vta6dWsrUqSI5cmTx+bPn+8cyZszZ45lzZrVHnnkETfLTvUSw9hvv/1mderUseLFi1vt2rW9ppGtXr06WSg7ffq07dixw7799tt0eamFS7n4Qqm///678/vOnTuta9euVrJkSXv//fed7REREV7z4keOHGmhoaFeX1ypWeJzjo+Pd75AEy+AWqlSJSeU7d+/3wYMGGBZs2a1N954w/744w976qmnrHbt2oysmvcOzF9//WW1atWyunXr2tdff21mF86HveWWW6x27dq2ePFiW7lypTVp0sR69Ohh8fHxljlz5ksuSgGzd99914oWLWoFCxa0LFmy2GeffeZ1e8WKFZ1Qlvh6Dg8Pt7CwsHQ7Mvb6669b5syZ7dlnn7X+/ftbmTJlLF++fHb48GELCwu7ZCh76aWXnNdjepGQkGAxMTHWpk0bq1ixok2fPt127NhhlStXthkzZthvv/1mDz/8sFWtWtVGjBjhfNZ99tln5vF4bOjQoTdF8Lga3333nb344ov24osv2unTp+3QoUN22223mcfjsaVLl5rZ/z7vYmJibNOmTbZo0SLbuHGj89q5Wd5vBLI0ZuXKlZYnTx5nys7ixYstW7ZsVqxYMa/Vi44cOWLh4eHORQbTi6Q7Ko0bN7Z8+fLZihUrbODAgc6qPGZmDz30kOXLl8/mzJnjhLI333zTgoODnWv2wFvih9/mzZsta9as9vjjj9usWbOsc+fOVrduXa8d5ZUrV9o999xj5cuXd5bqxf8kfZ0+88wzdscdd1i+fPmsUqVKNmXKFDtz5oz99ttv1q1bNytVqpQzfTHR9u3brV27dhYSEnLTXBcv8fWzc+dO69u3r7Vp08YmTpxoZv8LZZUrV3ZC2d9//22jR482j8djxYoVszx58nA+p1165OWLL76wli1bWoMGDZyVOnfv3m01atSw2267zQoUKGC1atVyFkIpXbr0JReASu9ef/118/Pzs1mzZtnvv/9uPXv2tPz58ycbxalQoYIVL17c1q5dm2xnMD0FDLMLAdbj8TjTy8wunFOcOXNmZ7XJP/74w7p37245c+Z0pi+ePXv2kqcSpFVJn+Pp06etW7duVqdOHXvqqaesV69ezmjZ+fPnbfjw4clC2dKlS9PczIA5c+ZY8eLFrX///vb666872yMjI61IkSJWqVKlf7222s302iGQ3cQuPuH93Llz1qdPH2dq3YEDB+zWW2+1tm3bWtu2be22226zzz//3K1yU42//vrLqlWrZkePHrX27dtbaGioVatWzfkiSNStWzcLCQmxefPmOaEscVloXNqWLVssKCjIWYLW7MJU0MqVK9uWLVts1apVzvZvv/3W2rVrZ7feemuyhQdwwfjx4y1v3rz2+eefW2xsrNWtW9duvfVWZ4rxL7/8Yj169LBcuXLZt99+69wvOjra5s6dazt37nSr9KuSNMznyZPH2rRpY/fff7/5+PgkC2UVK1Z0QpmZ2bZt22zt2rWMrJr3zkdERITXtMPVq1db06ZNrX79+l47x7t27bLdu3c7O78jR460W2+91fbt23fjCr8JzJ49O1mwWLlypTVt2tQ+/vhjW7JkiddskypVqlhQUFCqW1r7RtqzZ4+VLl3aypUr57X9/PnzVqJECa+Luu/atct69uxpHo/Ha+n29DS1c9euXdalSxeLj4+3EydO2AMPPGAhISF25513erWLjY214cOHW82aNa1///5pcr9kzpw5ljlzZpszZ47XwMELL7xg69atsxMnTtitt95qNWvW9Jo9cjO/XghkN6lLnfBuduFI0/fff2/R0dFWsWJF69mzp5ldGNL28/OznDlz2scff+xW2anC33//bQULFnSmHz7wwAPm8XiSLb9udmHlMV9fX6/RRSSXkJBg0dHRlilTJrvzzju9VsgaOXKkBQYGWpEiRSwgIMAaN27sHNVbtmyZde7c+aaZUnejJCQkWFRUlNWtW9fmzp1rZheCbUBAgM2cOdPM/jcn/scff7Tnnnvupp2qkhgifv31V8ucObM9+eSTZnbh+T322GM2YMAA53y4/fv3W/ny5ZN97sF7R2Ts2LFWuXJlK1y4sFWuXNlZyW7FihXWvHlza9iwoS1fvtzr/r///rt16tTJcufOzUjjRfbs2WOlSpVKFiwaN25sOXLksDvuuMMCAwOtatWqXgdGevTocdO+L6+FmJgYe+ONN6xGjRp2zz33ODvW7733nvn4+CRb/XX79u02fvz4m2aK2bX27bffmsfjsXfeecfMLhwA7tmzpxUsWNAmT57s9b0aFxdnffv2tQYNGiS7PtvNbtu2bVa2bFnnuy5Ru3btzOPxWP369W3jxo124sQJK1y4sNWuXTtNnHpDILuJJT3h/eITsJcvX25VqlRxRtA2bNhgDRo0sGHDhiVbZTGtS7qjkpCQYPHx8fbiiy9ayZIlnek7TZs2tbx589ry5cuTfYH27dv3phlpcNsrr7xivr6+9txzz5mZ2cSJEy0oKMg+/PBD+/nnn23JkiUWGBjodX23xNFHXJD4ej1+/LiVLl3ajh49al999ZXX9VXOnDnjnDuV1M2687d//37LnTu3tWvXzmt7hw4d7I477rASJUpY48aNbeHChU4oK1asmNdIGS549tlnLSQkxBYtWmRHjx610qVLW6lSpZyDHsuXL7eWLVta+fLlvRbP2bt3r7322musHHsJSYNF4uqlHTt2tFKlSjnXpFyyZInlyZPHnnrqqWRTGG/W9+V/kfS8nlmzZlmVKlWsc+fOtmDBAgsKCnLOK77cBevTSyi7eFrmoEGDLH/+/Pbjjz+a2YWD7126dLHq1avbq6++6vXaiouLS5OnUHz11Vd266232vbt251+6dOnjxUtWtS++OILa9CggTVq1Mg2bNhgJ06cMF9fX+vTp4/LVf93BLKbyD+d8H5xKPvss88sICDAVq9ebWYXLvj80EMPpbsT3hP77NixY17bT5w4YeXLl7e6des62+rVq2ehoaGXDGX4Z0m/UF999VXzeDxWt25dCw4O9pric/bsWWvSpIk1a9bspprbfb1dbtW2ihUrWr169SwwMNDeeustZ/vevXutTp06Xgt63Mz27NljlStXtlatWtmaNWvMzGzChAmWJUsWGzNmjL355pt2++23W9GiRW379u22d+9eq1y5ste119K78+fPW0REhFWvXt0++ugjM7tw4dSko6qJlixZYkOGDEn2HryZp/tcL5cKFnny5LGSJUsmW1r8rrvusi5durhQZep0cd9VrlzZPB6PTZ061czST+i6lMT33sWXl1izZo1VqVLFhg0b5lyKKDo62jp37mzVqlWz6dOnp/mVJ8eNG2e5cuXy2nbo0CFnVsS2bdusZs2aVrlyZUtISLBjx46liX02AtlN4kpOeE8aynbu3GmtWrWyW265xWrUqGHZsmVzjuSlN7t377acOXNay5YtLSwszE6dOmVmZj/99JNlzpzZxo4d67Rt0KCBFSpUyJYuXZom3uA3UtKduTfeeMM8Ho916dIl2QhY69atrV+/fuz8/b9/WrVt0aJFVrBgQatfv76z7dSpU9asWTOrW7dumnqNJl43plWrVtazZ08LDg52VkE1u3ANMo/H44wSpueduUQxMTHOdE6zC0G9SJEidu7cOVu2bJnXqOqpU6fs9ddfT3ZQjgMj/+7iYFGxYkVr0qSJ1/WNTpw4YdWqVXNmB+CCS4Wydu3aOa/b9Pw+3rVrlxUsWNDmzJljO3bscLaPGDHCsmfP7rVgRXR0tD300EN2++23ey1AlhYtXLjQsmTJ4qwKm1Ti59ULL7xgzZo18/o8u9m/DwlkN4GrOeE96dLQ69evt6lTp9qIESO83uzpzR9//GHZs2c3j8djjRo1ssmTJzvhdOjQoVa+fHmvef9VqlSxkiVLeu3o4MokDVkzZswwj8djY8eOdY4kP/3005YnT550/XpM6t9WbTt69KiNGzfO8uTJYzVr1rS2bdtarVq1rFy5cjfV9VWu1M6dO61hw4aWOXNmmzx5spldeE3FxsbawYMHrVy5cvbBBx+4XGXq8OGHHzqXj0g8qBQfH28VKlSw++67zwICAuzNN9902v/5559Wq1Yt5xIouDqXGilr27at8z5s1qyZlS9fPl0HjESXG3lN7LuqVatau3btnIOj6dX06dPN4/FYzZo1beDAgfbSSy85t911111WtWpVr/ZRUVHWu3fvND8zYPfu3RYYGGj33nvvJRcXio6OthYtWiS7NuzNjkCWyqXkhPfy5ct7XYsoPbr4+hOvvPKKPf744zZy5Ejr3bu3lS9f3pYsWWI//PCDlS5d2p555hmvaQCsMJZySUPZtGnTzOPx2JQpU2z48OHm7+/vzI1P7/5t1bbPPvvMOQd03bp11qVLFxswYIBNmjTJeV2nxZ2/P//80xo1amRNmza17777ztn+9NNPW+HChblgsV0I8oGBgfb444/bgAEDLGPGjM51wyZOnGjBwcHWpk0bp/2ZM2ecxTzSUoC/3q40WDRo0MCKFy+eJg+SXImki3O8/PLLyRaMMfPuu9mzZ1vhwoWd/Zn0rEOHDla5cmWbOXOmVahQwVq3bm27d++2jz/+2KpUqeIcdE/sv/QysyTxWrEPPvig1yJDe/futYYNG9odd9zhNUKdFhDIbgIpOeG9aNGizkhZWnmxXonE53rx9dVWr15tTZo0saVLl9rZs2dt2rRplj17dps0aZI1btzYsmfPniZW6bnRtm/fnuz8PDPv19xrr71mHo/HMmbMeNNcE+t6u5JV2wICAqxy5cr2ww8/XPIx0vJOX+L0xcaNG9vPP/9sL7zwgmXKlInXj124HqKvr6998sknzrYHHnjAXnnlFTt58qTt2bPHHn74YStTpow1bdrUHn74Yatdu7aVLVvWCQxMU7y0lASLggULevVtWjxI8k927NhhxYsXt8cee8wef/xxy5gx42UXwUrad1988UWa/gy7WOJ77uLn/O2339oDDzxgn332mUVERFi9evWsffv2NmDAAKtbt6516NAhXa4oe/78eeezLn/+/NakSRNr0KCBVa1a1apWrZomD34QyG4CnPB+dcLCwqxAgQL25JNPeo10jR071nLnzu0E1TVr1livXr2sefPm5vF4rFmzZmnqzX2tJZ5gnPjF8ssvv1j+/Pkv+zpLGsree++9dH09notd7aptSRfySS8HWP744w9r0aKFBQcHm6+vLyOrduGCuh6Px5599lmv7XfccYeVLVvWsmbNas2aNbNnn33WFi1aZK1atbKHHnrInnnmmTQ9qnotXItgkR77NioqymbMmGE5c+a0bNmyOec9XW7hiYs/v9LTd+5ff/1lderUsU8//dSOHj1qZheuF9izZ0/nMjznz5+36dOnW//+/c3X19c8Ho8zfTs9+uWXX6xv377WsGFD69Gjh7322mtp9v1GILtJcML7lYuMjLRnn33WsmfPbvXr1/eal921a1fr2rWrcyLo4cOH7dtvv7UWLVqk20VPrsScOXOsVatWXtPFtm/fbpUqVbLY2NjLhgSOxCfHqm1XbseOHdaqVSuvk9vTsz/++MNq165trVq1ckZz2rZta0WLFrWFCxfa0qVLrVSpUnbnnXde8pIA6Wnn92oRLK5eYh988sknliNHDitSpIj179/fuT099sk/2bt3r5UvX95KlChhbdu2dQ5S/vHHHxYUFGSvvPKK0zYyMtImT55s+fPn52DmJaTF11YG4aZQrFgxvfLKKzp79qzmz5+vYcOGqVGjRjIzxcXFKWPGjCpbtqxy584tSfLx8XG5Yvdkz55dzzzzjNauXascOXLotddeU926dbVz5041b95ckrRp0yZJUnBwsO666y599tlnKleunJtlp2pHjx5VRESERo4cqf3790uSwsPDFRsbqwwZMsjj8Vzyfhky8BFzMY/HIzOTn5+fOnbsqEcffVQFCxZUoUKFlC1bNkmSmSkqKkqxsbEqUaKEyxW7p0SJEvrwww9VunRpt0tJFYoVK6a3335bsbGxGj16tGrVqqW9e/dq+fLl6tChg5o2baq5c+fq119/dT7jksqYMaMLVad+ZqbAwECFhITIzJQ3b1698cYbkiRfX1/Fx8cnu8/Fn3npqW8TEhIk/a8PqlatqvXr12vQoEFauXKlHn30UUnefXKpPkxvChUqpJ9//ln9+vVTVFSUKlWqpMmTJytv3ryaO3euFi1apHXr1km6sB8zePBgbd++XWXKlHG5cneZWbJtafH9xt7STaR48eKaMWOGateurRUrVuj777+Xx+ORr6+vZs6cqZMnT6pq1apul5lqlCpVSjNnztRLL72kqKgoNWvWTD///LO2bt2qDz74wKvt5QIFLnj88cfVtWtX/fXXX3ryySd16NAhmZnOnDmjmJiYS97nUh+iuODiUPbYY4/p+PHj6tChg+Li4uTxeNSxY0fFxMRo2LBhbpfrKl9fX7dLSFWKFSumqVOnKiYmRlu3btUTTzyhW2+9VQkJCc57rmTJksqTJ4/LlaZ+BIurFxcX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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Top 10 colors in products (H&M)\n",
    "color_frequency = HM_df['color'].value_counts().nlargest(10)\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "color_frequency.plot(kind='bar', color='skyblue')\n",
    "plt.title('Top 10 Colors in H&M Products')\n",
    "plt.xlabel('Color')\n",
    "plt.ylabel('Frequency')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "34ae7c2b-4198-48e8-8511-b98fc1df5414",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2QAAAJBCAYAAAAp/nb5AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAByRElEQVR4nO3de3yP9f/H8efHTmZmDjMz5lSOOWY5H3OWJIRoDklEDgmRihRKOVQinRySQzmlYhG+cozMnImIyWYOszlubO/fH3678rEp1rhme9xvt8+tPtf1vj57XZfP6fl5v6/35TDGGAEAAAAA7rksdhcAAAAAAJkVgQwAAAAAbEIgAwAAAACbEMgAAAAAwCYEMgAAAACwCYEMAAAAAGxCIAMAAAAAmxDIAAAAAMAmBDIAAAAAsAmBDADuAofDcVu3//3vf3e9llmzZqlDhw4qWbKksmTJoiJFityy7YULFzRgwAAFBAQoa9asqlixoubNm3dHf2/dunVq166dChQoIHd3d/n4+KhGjRqaOnWqLl68eMf116tXT/Xq1bvj7e4Wh8OhkSNH3pXHHjhwoBwOh1q0aHHLNuHh4erdu7dKlCghT09P5c6dW+XKlVOPHj0UHh5+V+pKyYwZM5yey66uripYsKC6deumv/76657UcDf/LSRpypQpmjFjxl17fACQJFe7CwCAjGjTpk1O99966y2tWbNGq1evdlpepkyZu17LV199pcjISFWpUkWJiYm6evXqLdu2bt1aW7du1TvvvKMSJUpozpw5evrpp5WYmKiOHTv+698aMWKERo0apRo1auitt97SAw88oEuXLmnjxo0aOXKkfv/9d02cODEtd++e27RpkwoWLJjmj3v16lXNnj1bkhQSEqK//vpLBQoUcGpz/PhxPfzww8qZM6defvlllSxZUjExMdq7d6+++eYbHT58WIGBgWle2z+ZPn26SpUqpcuXL+uXX37R2LFjtXbtWu3atUteXl73tJa0NmXKFPn6+qpr1652lwIgAyOQAcBdUK1aNaf7efPmVZYsWZItvxd++uknZclyfUBEixYttHv37hTbLVu2TCtXrrRCmCTVr19fR48e1eDBg9W+fXu5uLjc8u98++23GjVqlLp3767PPvtMDofDWtesWTMNGTIkWVC914wxunLlijw9PVP9GHfr3/C7777TqVOn9Nhjj+nHH3/UzJkz9eqrrzq1+eyzz3T69Glt2bJFRYsWtZa3atVKr776qhITE+9Kbf+kbNmyCgoKknT9+ZKQkKC33npLS5YsUadOnVLc5tKlS8qWLdu9LBMA0i2GLAKATc6ePavevXtbQ/uKFSum4cOHKy4uzqmdw+HQiy++qGnTpqlEiRLy8PBQmTJlbnsoYVIY+zeLFy9W9uzZ9dRTTzkt79atm06cOKFff/31H7cfNWqUcuXKpQ8//NApjCXx9vZW48aNrftXrlzRsGHDVLRoUbm7u6tAgQLq06ePzp0796+13umx++STT1S6dGl5eHho5syZkqSpU6eqQoUKyp49u7y9vVWqVKlkASglNw+TSxq6t2bNGr3wwgvy9fVVnjx51Lp1a504ceJfHy/JF198IXd3d02fPl2BgYGaPn26jDFObc6cOaMsWbLIz88vxce4+d966dKlql69urJlyyZvb281atQoWSg+deqUnn/+eQUGBsrDw0N58+ZVzZo19fPPP9927TdKCqxHjx6VJHXt2lXZs2fXrl271LhxY3l7e6tBgwaSbv/fMTY2Vj169FCePHmUPXt2NW3aVL///nuyv921a9cUh+SOHDky2XMyMTFRH330kSpWrChPT0/lzJlT1apV09KlSyVJRYoU0Z49e7R27VprWGbSYycmJurtt99WyZIlrW3Lly+vDz74IFXHDEDmRg8ZANjgypUrql+/vv744w+9+eabKl++vNatW6exY8cqLCxMP/74o1P7pUuXas2aNRo1apS8vLw0ZcoUPf3003J1dVXbtm3TpKbdu3erdOnScnV1/mgoX768tb5GjRopbhsREaHdu3erffv2t9XzYYxRq1attGrVKg0bNky1a9fWzp07NWLECG3atEmbNm2Sh4dHitve6bFbsmSJ1q1bpzfeeEP+/v7y8/PTvHnz1Lt3b/Xt21fvv/++smTJokOHDmnv3r23c6hS9Nxzz+mxxx7TnDlzFB4ersGDB+uZZ55JNkw1JcePH9eKFSvUpk0b5c2bV126dNHbb7+tX375RXXr1rXaVa9eXR9//LFat26tgQMHqnr16sqRI0eKjzlnzhx16tRJjRs31ty5cxUXF6dx48apXr16WrVqlWrVqiVJCg4OVmhoqEaPHq0SJUro3LlzCg0N1ZkzZ1J1HA4dOiTpeq9wkvj4eLVs2VI9e/bU0KFDde3atdv+d0x6rmzcuFFvvPGGHnnkEW3YsEHNmjVLVX1JunbtqtmzZ6t79+4aNWqU3N3dFRoaqj///FPS9R8o2rZtKx8fH02ZMkWSrOfkuHHjNHLkSL322muqU6eOrl69qv3799/WjwkAkIwBANx1Xbp0MV5eXtb9Tz75xEgy33zzjVO7d99910gyK1assJZJMp6eniYyMtJadu3aNVOqVCnz4IMP3lEdjz32mClcuHCK64oXL26aNGmSbPmJEyeMJDNmzJhbPu7mzZuNJDN06NDbqiMkJMRIMuPGjXNaPn/+fCPJfPrpp9ayunXrmrp161r37/TY+fj4mLNnzzq1ffHFF03OnDlvq9abSTIjRoyw7k+fPt1IMr1793ZqN27cOCPJRERE/Otjjho1ykgyISEhxhhjDh8+bBwOhwkODnZql5iYaHr27GmyZMliJBmHw2FKly5tXnrpJXPkyBGrXUJCggkICDDlypUzCQkJ1vLz588bPz8/U6NGDWtZ9uzZzYABA+7kEDjt9+bNm83Vq1fN+fPnzQ8//GDy5s1rvL29redrly5djCTz5ZdfOm1/u/+Oy5cvN5LMBx984NRu9OjRyf4tunTpkuLze8SIEebGrzy//PKLkWSGDx/+j/v40EMPOT33krRo0cJUrFjxH7cFgNvFkEUAsMHq1avl5eWVrHcrafKAVatWOS1v0KCB8uXLZ913cXFR+/btdejQIR0/fjzN6kppqOHtrLtTSb1GN0+W8NRTT8nLyyvZ/t+87Z0cu0cffVS5cuVyWlalShWdO3dOTz/9tL777judPn06lXvyt5YtWzrdT+pZTBq6dyvGGGuYYqNGjSRJRYsWVb169bRw4ULFxsZabR0Ohz755BMdPnxYU6ZMUbdu3XT16lVNnDhRDz30kNauXStJOnDggE6cOKHg4GCnYYzZs2dXmzZttHnzZl26dMk6FjNmzNDbb7+tzZs3/+OkLympVq2a3Nzc5O3trRYtWsjf31/Lly93er5KUps2bZzu3+6/45o1ayQp2flotzPJzK0sX75cktSnT59UbV+lShXt2LFDvXv31k8//eT0bwQAd4pABgA2OHPmjPz9/ZOFHD8/P7m6uiYbLubv75/sMZKWpXZo2c3y5MmT4mOdPXtWkpQ7d+5bbluoUCFJ0pEjR27rb505c0aurq5Ow9qk64HD39//H/fpTo9d/vz5kz1GcHCwvvzySx09elRt2rSRn5+fqlatqpUrV95W/SnJkyeP0/2k4W2XL1/+x+1Wr16tI0eO6KmnnlJsbKzOnTunc+fOqV27drp06ZLmzp2bbJvChQvrhRde0BdffKGDBw9q/vz5unLligYPHizp7+dESvseEBCgxMRERUdHS5Lmz5+vLl266PPPP1f16tWVO3dude7cWZGRkbe137NmzdLWrVu1fft2nThxQjt37lTNmjWd2mTLli3Z0Mrb/XdMeq7cfHxTek3crlOnTsnFxSXVjzFs2DC9//772rx5s5o1a6Y8efKoQYMG+u2331JdE4DMi0AGADbIkyePTp48mWzShqioKF27dk2+vr5Oy1P6cpy07OYvqqlVrlw57du3T9euXXNavmvXLknXZ9O7lfz586tcuXJasWKF1fPyT/LkyaNr167p1KlTTsuNMYqMjEy2/zdveyfH7lY9e926ddPGjRsVExOjH3/8UcYYtWjR4l97tNLaF198IUmaMGGCcuXKZd1eeOEFp/X/pF27dipfvrw1g2bScyIiIiJZ2xMnTihLlixWr6Gvr68mTZqkP//8U0ePHtXYsWO1aNGi257qvXTp0goKClLFihVTDIBSyv8Gt/vvmPRcuTlop/SayJo1a7IJQSQl6wHNmzevEhISbjt03szV1VUDBw5UaGiozp49q7lz5yo8PFxNmjS5rec/ANyIQAYANmjQoIEuXLigJUuWOC2fNWuWtf5Gq1at0smTJ637CQkJmj9/vh544IE0uybWk08+qQsXLmjhwoVOy2fOnKmAgABVrVr1H7d//fXXFR0drX79+iX7ki1dv+j0ihUrJP29f0nX3UqycOFCXbx4Mdn+3+hOj92/8fLyUrNmzTR8+HDFx8drz549d7T9fxEdHa3FixerZs2aWrNmTbJbp06dtHXrVitopRSwpOvHNjw8XAEBAZKkkiVLqkCBApozZ47Tv8XFixe1cOFCa+bFmxUqVEgvvviiGjVqpNDQ0Luwx3+73X/H+vXrS5K+/vprp3Zz5sxJ9phFihRRVFSU02slPj5eP/30k1O7pAlBpk6d+o81enh4/GsPZ86cOdW2bVv16dNHZ8+etSYFAYDbxSyLAGCDzp076+OPP1aXLl30559/qly5clq/fr3GjBmj5s2bq2HDhk7tfX199eijj+r111+3Zlnc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AGATAhkAAAAA2IRABgAAAAA2IZABAAAAgE0IZAAAAABgEwIZAAAAANiEQAYAAAAANiGQAQAAAIBN0nUgu3btml577TUVLVpUnp6eKlasmEaNGqXExESrjTFGI0eOVEBAgDw9PVWvXj3t2bPH6XHi4uLUt29f+fr6ysvLSy1bttTx48ed2kRHRys4OFg+Pj7y8fFRcHCwzp07dy92EwAAAEAmla4D2bvvvqtPPvlEkydP1r59+zRu3Di99957+uijj6w248aN04QJEzR58mRt3bpV/v7+atSokc6fP2+1GTBggBYvXqx58+Zp/fr1unDhglq0aKGEhASrTceOHRUWFqaQkBCFhIQoLCxMwcHB93R/AQAAAGQuDmOMsbuIW2nRooXy5cunL774wlrWpk0bZcuWTV999ZWMMQoICNCAAQP0yiuvSLreG5YvXz69++676tmzp2JiYpQ3b1599dVXat++vSTpxIkTCgwM1LJly9SkSRPt27dPZcqU0ebNm1W1alVJ0ubNm1W9enXt379fJUuWvK16Y2Nj5ePjo5iYGOXIkeM/7/8720//58e4W4ZW8rW7BAAAACDdut1skK57yGrVqqVVq1bp999/lyTt2LFD69evV/PmzSVJR44cUWRkpBo3bmxt4+Hhobp162rjxo2SpG3btunq1atObQICAlS2bFmrzaZNm+Tj42OFMUmqVq2afHx8rDYAAAAAkNZc7S7gn7zyyiuKiYlRqVKl5OLiooSEBI0ePVpPP/20JCkyMlKSlC9fPqft8uXLp6NHj1pt3N3dlStXrmRtkraPjIyUn59fsr/v5+dntUlJXFyc4uLirPuxsbGp2EsAAAAAmVW67iGbP3++Zs+erTlz5ig0NFQzZ87U+++/r5kzZzq1czgcTveNMcmW3ezmNim1/7fHGTt2rDUJiI+PjwIDA29ntwAAAABAUjoPZIMHD9bQoUPVoUMHlStXTsHBwXrppZc0duxYSZK/v78kJevFioqKsnrN/P39FR8fr+jo6H9sc/LkyWR//9SpU8l63240bNgwxcTEWLfw8PDU7ywAAACATCddB7JLly4pSxbnEl1cXKxp74sWLSp/f3+tXLnSWh8fH6+1a9eqRo0akqTKlSvLzc3NqU1ERIR2795ttalevbpiYmK0ZcsWq82vv/6qmJgYq01KPDw8lCNHDqcbAAAAANyu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3WsFjBuPSe/evY3D4TAhISH3vNb04sYgFhUVZQ093LlzpylWrJhp27at0zllI0aMMG3btjWtWrUyO3futKXm9OqfZrv7+OOPjTF/D2e/OfSnpy9290JoaKgpXry4qVChgtm2bZsx5vr3hpkzZ5quXbuapk2bmpdeeonPz5t8/fXX1jX/+vTpY3x9fc0nn3xiLly48I/bZbbn1+364YcfTNmyZc2KFStMaGioadSokXnkkUesU3GOHz9uPv30U9O3b1/z1ltvWeH3+eefN61bt05XE8wQyDKYm39dvnLlijl//rz56aefTKNGjUyNGjWShbKbw1dGfuGndNL7li1bzMCBA821a9dMeHi4efDBB81zzz1n9u7da0qUKGFKliyZ6T9Url69alatWmWCgoJMUFCQWbp0qXVND2OM2bNnj6lTp47Jnz+/FcrCwsJM7969zZEjR2yqOn1J+gK3aNEiU65cOZMvXz5TsWJF06ZNG6vN8ePHTUhIiClTpow1eUVmceMX3FdeecWUKFHC5MmTx9SuXdssWbLE/PHHHymGsvfeey9D/4B0Kz/++KMJCwuz7i9cuNBUqVLFFC1a1Dz++ONm+fLl1jFr27at07mb165dS3GWsczudme7u/EzNDP2xibZsWOHKV++vHnuuecy1XXXUmv37t2mUqVKpkKFCtaIpS5dupiSJUuaWbNmWT39mXFCtdRYvHixGTx4sNO12M6fP2+efPJJExQUZGbPnp2s9zEyMtK89NJLJmfOnNb5ZekFgSwDufFFvHjxYjN37lzz/fffW8uSum9r165tfaB07NjRzJw5857XapeUTno35u+p2J999lnz1FNPWS/iVq1aGYfDYR588MFkL+zM4sYvHMuWLTNNmzY1bm5upm/fvk7tkkJZoUKFTHh4uDHGZNpjdiurVq0yWbNmNR9++KFZuXKlmTZtmilVqpQJCgpyanfu3DkzcuTITPNDwI3vXXPnzjX58+c3S5YsMTNmzDCDBg0yWbJkMTNnzjR//PGHeeCBB8zTTz9tXZstSWYKZZGRkaZo0aKmW7du5o8//jB79uwxOXLkMG+//bZ55513TK9evYyrq6uZMWOGFcqefvpps3HjRrtLT7dSM9sd/h6F89xzz6W7L7jpyaBBg0ybNm1MjRo1TK5cuUyxYsWs84aDg4NN6dKlrQtp499duHDBlChRwjgcDtO5c2endUmhrHr16k7X0T19+rQZNWqUqV27drq8Dh6BLIO48UvzoEGDTI4cOUypUqWMm5ubNcbbmOvdu02bNjV58+Y1NWvWNIGBgZnmi8zNJ7136NDBmt3ImOvDN2vVqmU+/PBDa1mvXr3MDz/8kKmvM5Zk586dpnv37mbBggXWOXY3f3js3bvXVKhQwZQqVcpcu3aNX/pu8sorr5hOnTpZ9xMTE83WrVtNyZIlrQ+VpGOWGX95X7NmjXnuuefMhAkTrGWxsbHmgw8+MFmzZjUbNmwwoaGhJlu2bOaNN96wsVL7bdu2zQQFBZk+ffqY4cOHW9eVNOb6OT4fffSRcXNzMz///LPZuXOnyZkzp+nevbt13UD8LbWz3eG60NBQU6VKFdOhQ4dM8yPSnZg+fbrJmTOn2bZtmzl79qyJiIgwjRs3NkFBQWbJkiXGmOs9Zbly5crUw6/vVFRUlKlfv7556KGHzA8//OD0fePChQumTp06pkePHk7bREREmNOnT9/rUm8LgSwDuPGL219//WWqVKliduzYYY4dO2YWLFhgsmXL5nSBxtDQUDNx4kTz6quvWmEsM3zApHTSe7t27Zx6ypo3b25KlSplVq9ebfr27WsCAwMzzWQK/ybpmmKbN282GzZsMA899JCpXLlysrHv+/fv55oz/y/ptblnzx5z7do18+yzz5pHHnkkWbvx48ebKlWqWBc1zowiIiLMAw88YLy9vc3bb7/ttO7s2bOmZcuWpk+fPsYYY7Zv354p3rP+zbZt20yVKlVM4cKFrWOT5Ny5c9ZU5MZc/yEqM05G9G/SYrY7XB/6X7duXX68TMHw4cNNrVq1TEJCghUajh8/bqpUqWKKFClihbK33nqLocR3KCIiwlSpUsXUrVs3WZi9dOmSdbzvhx+HCWT3saRhYUnGjBlj2rRpY5599lmnoWI//PCD8fLySvZLQZKM/sHybye9P/XUU9Yvo9u3bzfVq1c3gYGBpkyZMpl6dqikMHFjL1idOnXMo48+aowxZtOmTaZixYomKCiIYRb/YOnSpaZIkSJm06ZNZs6cOebhhx82P/74o1ObRYsWmSJFijhdbysz2rFjh3nggQfMww8/nOy1171792TXGMvo7123Y8eOHaZIkSKmVKlSyYbhDB8+3JQvXz7ZpQHwN2a7Szs8z5wlvVeNGjXKBAUFWccnKXStWbPGZMuWzdSuXdv88MMP1na8r6Xso48+Mj169DCNGjUyP/zwg/V5+ddff5lHHnnE1K1b1/z000/JRpfcD2HMGGOyCPel7t27q1+/ftb9xMREZcuWTcuWLdOOHTvk7u5urXvsscc0f/58zZ8/X+3bt0/2WC4uLvek5nst6Vg4HA65uLho0aJFatGihSpWrKiWLVvqr7/+0sqVK7Vt2zaNGzdOO3bsUMWKFbVhwwatWLFC69atU6VKlezeDds4HA6FhIToueee008//SRJmjNnjg4fPqyxY8eqWrVq+vDDD5UlSxZVqFBBly5dsrni9MMYI0mKjIzUrFmzNHjwYFWrVk01atRQtmzZ9Pnnn+uHH36w2m7YsEH58+eXl5eXnWXbrnz58lq0aJESEhL0wQcfKCwsTJJ0/vx57d+/X4UKFZLD4bDaZ9T3rjtRvnx5LV26VG5ubvrwww+tYyZJp0+fVt68eZWQkGBfgenUnDlz9NVXX2nRokXq3bu39u/fr+nTp+vixYtWm6efflrjxo3TJ598ooEDB8rV1VUJCQlydXW1sfL0K2vWrHaXkK4kvVe1atVK27dv17vvvitJcnNzkyTFxcWpWbNmcnNz06RJkxQXFyeJ97WUDB06VKNGjZKvr6/8/Pz08ssv68MPP9SRI0cUEBCg7777TvHx8XrppZe0ZcsWp22zZLlPoo7diRCpEx0dbf2alzTM6dKlS+aLL74wrq6uZsSIEcm2WbBggWnQoMF982vBf5Gak947dOjgdPHZzC4xMdH06NHDOBwOkytXLvPGG2+YP/74w4wePdo8+eSTZvv27SYxMdGEhISYevXqmcOHD9tdcrqydu1a8/TTT5t69eo5ney+a9cuU6dOHVO+fHlTqlQp06xZM+Pj45MuTzK2S2hoqClTpozJly+fadGihWndurWpVKmS9Z6XGc+v+zehoaGmbNmypmjRoqZr166mZ8+eJk+ePDyvUsBsd7jXpk+fbtzc3MyQIUPMb7/9Zv744w/z2GOPmdGjR5u9e/cah8NhVq5caXeZ6dKsWbNMkSJFrMsrrFu3zjgcDlOiRAkzcOBA6xSJ48ePm+eee+6+7WEkkN2HbnyyffXVV8bX19e6uGd8fLyZMmWKcXFxMaNGjbrlY2SGD5rUnvSemYdd3PxF99dffzVPP/20efvtt02VKlXMCy+8YJ577jlTunRp89577xljrj/nGLKY3Jo1a0zevHmNw+Ew33zzjdO6Y8eOmR9//NH079/fvP/++8kuRYHrwbVo0aKmdu3a1rTjxhjOsfgHO3fuNA8++KApVKiQGTt2LOdypoDZ7mCHxMRE8+233xo/Pz9TsGBBU6BAAVOpUiVz+fJl8+eff5rixYtz6YAUxMXFmfnz55t3333XGHN9BvGcOXOazz//3Lz55psmW7ZsZtCgQdZM2Unux1BGILvP3PiFefXq1SY8PNwEBQWZcuXKWSdsJ4UyV1fXZCfHZzac9H7nVq1aZU31nJCQYF588UXTtWtXExMTYz755BOr18zhcJj169fbXG36cON5iqdOnbLOUzx48KApVqyYadq0qdOMnrg927dvN1WrVjU9evTgtXmbfvvtN9OoUSMTFRVldynpDrPdwW7Hjx83mzZtMr/88ov1w/jQoUNNqVKlTEREhM3VpS+jR482y5cvN8eOHTMnT540J06cMEFBQWb8+PHGmOsjxfLnz28CAgKs2bHv59ETBLL7yI1PtDfeeMM89NBD5vDhw+bUqVMmKCjIlClTximUffLJJ8bhcJjp06fbVHH6wEnvt+/atWtm9OjR1rU91q9fbxITE02lSpWsYbCxsbGmb9++JiAgwOqZzaz+7eK8y5YtM4cPH7Ymj7lxRs/M0EudFphS+87xfpYyZrtDerJ7924THBzM0OIUzJ8/37i5uTlN7rRt2zbz4IMPWqeW7N6923Tt2tVMmTLlvuwRu9l9cqYbpL9PEN29e7fCwsL08ccfq2jRovL19dXy5cuVLVs2PfHEEzp06JDc3NzUrVs3LVy4UM8884zNlduLk95vn4uLi1599VWFhYUpMjJSr7zyil566SWNGTNGoaGhWr9+vby9vfXhhx9qz549Kl68uN0l2+bkyZN68cUX9cEHH+jw4cPau3evunXrppYtW6pnz54qUKCAWrZsqV9++cWaPGb8+PH69ddfJd1HJxrbrFKlSpo8ebIiIiLk4+Njdzn3BSZXcGb+f5IdDw8PXblyRfHx8cqSJYuuXr2qAgUK6N1331VUVJTGjx+vH3/8Ua+99prc3Nz4XMBdc+3aNcXHx8vPz09r165VxYoV7S4p3Vi4cKEuXbqkjz/+WJUqVbJev5cvX5aLi4s2bNigzZs3a+jQobpy5YpeeOEFubi43PevV4dJ2lPcF6ZMmaL58+crISFBixYtkp+fnxITE5UlSxadPn1azZs315UrV/TNN9+oVKlS1nbXrl3L9DNDbd++XZ07d9bFixdVt25deXh4aMGCBfr55595M0zByZMntXLlSo0fP16HDh1S3rx51b59e40dO9bu0tKN0NBQ9ezZU1WrVlXOnDkVFxen9957T5IUGxurWbNmaeDAgVq+fLn8/PxUp04dtWnTRh9//LE8PDxsrv7+cuXKFYIG/pNdu3apUqVKev311zVixAhr+U8//aTPPvtM0dHRypIli3744Qden7gnrl69as26COn48eMqXbq0Ll68qFGjRum1116TMcbqkOjbt69+/PFH68eUdevWyc3NzanN/YpAls4lha0kq1evVrdu3RQVFaWFCxeqefPmTu1Onz6toKAg1apVS7Nnz7ar7HRr165dat26teLj4/XCCy/o6aefVuHChe0uK11LSEjQkCFDNGXKFOXIkUOHDh2St7e33WWlG6GhoXrhhRd08uRJtWjRQpMnT7bWxcTEaMCAAbpy5Yrmzp2rjRs3ys/PTw8++KCNFQOZ14wZM/T888/rpZdeUrt27ZQrVy7169dPNWrU0JNPPqmHHnpIK1asUMOGDe0uFciU1q1bp379+snDw0P/+9//lDVrVqfgunPnTiUkJKh8+fJycXHJMB0OBLJ07MYwdvDgQWXNmlWBgYE6fPiwGjVqpDJlymjEiBEKCgpyah8TE6Ps2bNzLYtb2LZtm4YNG6avv/5aefPmtbucdO3GX51Wr16tBx54gACbgp07d+qJJ55Q1qxZNXfuXKce19dee03ff/+9fv31V3p4AJsZY7Rw4UL16dNH7u7uMsbIz89PGzdu1MmTJ9WoUSMtWLBA5cuXt7tUINP47rvvFBERITc3N9WuXVsnT55U9+7dVbRoUes6qCn1JiYkJGSY77oEsnTqxi/CQ4cO1eLFi3XmzBmVKVNGAwcOVIUKFdSwYUNVrlxZr7zyiipXrpxsu4z0RE1rDH+6fRlhKMC9sGvXLnXq1ElBQUHq16+fFcp69eqlQ4cO6bvvvsv0F34G0ou//vpL4eHhunr1qmrWrKksWbJo2LBhWrJkidasWSN/f3+7SwQyhUGDBmnmzJkqVaqUtm/frvLly6tt27Z65JFH1K1bNxUvXlzLly+XlLG/jxDI0qEbe8bmzZungQMHaurUqTp37px2796tCRMmaPr06apVq5YaN26sKlWqqF+/fqpWrZrNlQOZG+cpAvefPXv26N1339WyZct4rQL30IIFC9SvXz99//33evjhhxUTE6PBgwfr0KFDevrpp1WmTBk9/fTTCggIsCbEyqiY5isdSgpj//vf/7Rq1SoNHjxYTzzxhLp06aI33nhDEydOVM+ePRUZGalvv/1W3333nfXrAQD7VKpUSXPmzJGLi4tWr16tIkWKaNu2bXzBA9IpZrsD7HP48GEVKlRI5cuXlzFGOXPm1Ntvv61cuXJp0aJFqlWrlmbOnCl/f38lJibaXe5dRQ9ZOhUZGalatWopKipKr7zyioYPH26ti46OVteuXRUYGKjJkycrLCxM5cqVY3gikE5wniJwf2G2O+DeSRp6OGHCBM2aNUsbNmyQl5eXNUHHb7/9pipVqmjHjh0qV66ctd3NE91lJBlzrzIAf39/a1r7RYsWafv27da6XLlyKW/evDp48KCMMapYsWKGuAYDkFFUrlxZS5cuJYwB9wnCGHDvJJ0H1rRpU+3evVvvv/++JFmzJSYkJOihhx5StmzZnLbLqGFMIpCla+XLl9eiRYuUkJCgDz74wLqg8fnz57V//34VKlTI6eRGesiA9INJYwAAuLUyZcroiy++0OjRozVo0CBt3LhR+/bt05tvvqlcuXKpaNGidpd4zzBk8T6wfft2PfPMMzpz5oweeeQRubu768iRI9q8ebM1bW9GnXUGAAAAGdfChQvVt29fORwOZcuWTX5+fvrf//4nNze3DD1M8UYEsvvE7t271bJlSxUsWFAdO3ZUr169JDHuHQAAAPe3yMhInTx5UvHx8apcubKyZMmSYS76fDsyfuTMIMqWLatFixYpPj5eoaGhOnTokCTGvQMAAOD+5u/vrwoVKuiRRx5RlixZlJiYmGnCmEQP2X1n+/bt6tWrl4oVK6YRI0aoVKlSdpcEAAAAIJXoIbvPVKpUSZMnT1ZERIR8fHzsLgcAAADAf0AP2X3qypUrzOIGAAAA3OcIZAAAAABgE4YsAgAAAIBNCGQAAAAAYBMCGQAAAADYhEAGAAAAADYhkAEA7mv16tXTgAED7spj//nnn3I4HAoLC7srj38nRo4cqYoVK9pdBgAgjWWeS2ADAHCHAgMDFRERIV9fX7tLAQBkUPSQAQBwCy4uLvL395era8b4/fLq1at2lwAAuAmBDABw37t27ZpefPFF5cyZU3ny5NFrr72mpMtszp49W0FBQfL29pa/v786duyoqKgoa9vo6Gh16tRJefPmlaenp4oXL67p06dLSnnI4p49e/TYY48pR44c8vb2Vu3atfXHH3/cVp1ffvmlHnroIXl4eCh//vx68cUXrXXHjh3TE088oezZsytHjhxq166dTp48ecvHSkxM1KhRo1SwYEF5eHioYsWKCgkJsdYn1f7NN9+oXr16ypo1q2bPnn1bdQIA7h0CGQDgvjdz5ky5urrq119/1YcffqiJEyfq888/lyTFx8frrbfe0o4dO7RkyRIdOXJEXbt2tbZ9/fXXtXfvXi1fvlz79u3T1KlTbzlE8a+//lKdOnWUNWtWrV69Wtu2bdOzzz6ra9eu/WuNU6dOVZ8+ffT8889r165dWrp0qR588EFJkjFGrVq10tmzZ7V27VqtXLlSf/zxh9q3b3/Lx/vggw80fvx4vf/++9q5c6eaNGmili1b6uDBg07tXnnlFfXr10/79u1TkyZN/rVOAMC95TBJPyECAHAfqlevnqKiorRnzx45HA5J0tChQ7V06VLt3bs3WfutW7eqSpUqOn/+vLJnz66WLVvK19dXX375ZbK2f/75p4oWLart27erYsWKevXVVzVv3jwdOHBAbm5ud1RngQIF1K1bN7399tvJ1q1cuVLNmjXTkSNHFBgYKEnau3evHnroIW3ZskWPPPKIRo4cqSVLlli9dQUKFFCfPn306quvWo9TpUoVPfLII/r444+t2idNmqT+/fvfUa0AgHuHHjIAwH2vWrVqVhiTpOrVq+vgwYNKSEjQ9u3b9cQTT6hw4cLy9vZWvXr1JF0fIihJL7zwgubNm6eKFStqyJAh2rhx4y3/TlhYmGrXrn3HYSwqKkonTpxQgwYNUly/b98+BQYGWmFMksqUKaOcOXNq3759ydrHxsbqxIkTqlmzptPymjVrJmsfFBR0R7UCAO4tAhkAIMO6cuWKGjdurOzZs2v27NnaunWrFi9eLOn6UEZJatasmY4ePaoBAwZYoWnQoEEpPp6np2eq6vi37YwxToHy35YnuXldSu29vLzuoFIAwL1GIAMA3Pc2b96c7H7x4sW1f/9+nT59Wu+8845q166tUqVKOU3okSRv3rzq2rWrZs+erUmTJunTTz9N8e+UL19e69atu+PZCr29vVWkSBGtWrUqxfVlypTRsWPHFB4ebi3bu3evYmJiVLp06WTtc+TIoYCAAK1fv95p+caNG1NsDwBIvwhkAID7Xnh4uAYOHKgDBw5o7ty5+uijj9S/f38VKlRI7u7u+uijj3T48GEtXbpUb731ltO2b7zxhr777jsdOnRIe/bs0Q8//HDLUPPiiy8qNjZWHTp00G+//aaDBw/qq6++0oEDB/61xpEjR2r8+PH68MMPdfDgQYWGhuqjjz6SJDVs2FDly5dXp06dFBoaqi1btqhz586qW7fuLYccDh48WO+++67mz5+vAwcOaOjQoQoLC+N8MQC4z2SMC6sAADK1zp076/Lly6pSpYpcXFzUt29fPf/883I4HJoxY4ZeffVVffjhh3r44Yf1/vvvq2XLlta27u7uGjZsmP788095enqqdu3amjdvXop/J0+ePFq9erUGDx6sunXrysXFRRUrVkx2LldKunTpoitXrmjixIkaNGiQfH191bZtW0nXhx4uWbJEffv2VZ06dZQlSxY1bdrUCmwp6devn2JjY/Xyyy8rKipKZcqU0dKlS1W8ePE7PHoAADsxyyIAAAAA2IQhiwAAAABgEwIZAABpIHv27Le8rVu3zu7yAADpFEMWAQBIA4cOHbrlugIFCqR6ynwAQMZGIAMAAAAAmzBkEQAAAABsQiADAAAAAJsQyAAAAADAJgQyAAAAALAJgQwAAAAAbEIgAwAAAACbEMgAAAAAwCYEMgAAAACwyf8BJiZzpPM/VX4AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Top 10 colors in products (Asos)\n",
    "color_frequency = asos_df['basic_color'].value_counts().nlargest(10)\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "color_frequency.plot(kind='bar', color='skyblue')\n",
    "plt.title('Top 10 Colors in ASos Products')\n",
    "plt.xlabel('basic_color')\n",
    "plt.ylabel('Frequency')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "80e4d12b-489c-4fdc-90e7-feca0e50846a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 1000x600 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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epWhB/9+rvv378PDwwPnzp3T2dWW3MfWv7R+f/OYHSIiIso0cXFxePz4MUaMGIEKFSp8NOh8KdyNRURERJnm//7v/+Du7o7z589j4cKFmTJP9uwQERGplL4udPoxfn5+6Tr3z5fAnh0iIiJSNYYdIiJKE45nIX34Eusdww4REX2U9my5b9++1XMl9F+kXe+Sn7U5PXjMDhERfZSxsTGyZ8+unCfFysoqwy7YSKQlInj79i2ePn2K7Nmz65z8ML0YdoiI6JOcnJwA4JMXtyT60rJnz66sf5+LYYeIiD5Jo9HA2dkZDg4OOheOJMpIpqam/6pHR4thh4iI0szY2PiLfPkQZSYeoExERESqxrBDREREqsawQ0RERKrGsENERESqxrBDREREqsawQ0RERKrGsENERESqxrBDREREqsawQ0RERKrGsENERESqxrBDREREqsawQ0RERKrGsENERESqxrBDREREqsawQ0RERKrGsENERESqxrBDREREqsawQ0RERKrGsENERESqxrBDREREqsawQ0RERKqm17AzZcoUlCtXDra2tnBwcEDTpk1x/fp1nTadOnWCRqPRuVWoUEGnTUxMDAIDA5ErVy5YW1ujcePGePDgQWYuChERERkovYadY8eOoU+fPjhz5gxCQkIQHx+POnXq4M2bNzrt6tWrh8ePHyu3vXv36tw/YMAAbNu2DevXr8fJkycRFRUFf39/JCQkZObiEBERkQEy0efM9+3bp/P3smXL4ODggPPnz6Nq1arKdHNzczg5OaX6HBEREViyZAlWrVqFWrVqAQBWr14NNzc3HDx4EHXr1s24BSAiIiKDZ1DH7ERERAAAcubMqTP96NGjcHBwQKFChdC9e3c8ffpUue/8+fOIi4tDnTp1lGkuLi4oXrw4Tp06lep8YmJiEBkZqXMjIiIidTKYsCMiGDRoECpXrozixYsr0+vXr481a9bg8OHDmDFjBs6dO4caNWogJiYGABAWFgYzMzPkyJFD5/kcHR0RFhaW6rymTJkCOzs75ebm5pZxC0ZERER6pdfdWEn17dsXly5dwsmTJ3Wmt2zZUvl/8eLFUbZsWbi7u2PPnj0ICAj44POJCDQaTar3jRw5EoMGDVL+joyMZOAhIiJSKYPo2QkMDMTOnTtx5MgR5MmT56NtnZ2d4e7ujhs3bgAAnJycEBsbi5cvX+q0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ax5krX5pDjtHjhwBAHTu3Bk//vgjsmXL9q9nHhUVhZs3byp/37lzBxcuXEDOnDmRM2dOBAcHo3nz5nB2dkZoaChGjRqFXLlyKUPc7ezs0LVrVwwePBj29vbImTMnhgwZAm9vb2V0FhEREf23pfuYnWXLlin/f/DgATQaDVxdXT9r5r///juqV6+u/K3dVdaxY0csWLAAly9fxsqVK/Hq1Ss4OzujevXq2LBhA2xtbZXHzJo1CyYmJmjRogWio6NRs2ZNLF++XGfEGBEREf13pTvsJCYmYuLEiZgxYwaioqIAALa2thg8eDBGjx4NI6O0D/Dy8/P76FmX9+/f/8nnsLCwwJw5czBnzpw0z5eIiIj+O9IddkaPHo0lS5bg+++/x1dffQURwf/93/8hODgY7969w6RJkzKiTiIiIqLPku6ws2LFCixevBiNGzdWppUsWRKurq7o3bs3ww4REREZlHSfVPDFixcoUqRIiulFihTBixcvvkhRRERERF9KusPOhy7cOXfuXJQsWfKLFEVERET0paR7N9a0adPQsGFDHDx4EBUrVoRGo8GpU6dw//79FFckJyIiItK3z7o21j///INmzZrh1atXePHiBQICAnD9+nW4u7tnRI1EREREny3dPTuenp54/PhxigORw8PD4ebmhoSEhC9WHBEREdG/le6enQ+dFycjLgRKRERE9G991oVAx44dq5cLgRIRERGlV5a6ECgRERFReun1QqBEREREGe1fXQiUiIiIyNCl+wBlIiIioqyEYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVI1hh4iIiFSNYYeIiIhUjWGHiIiIVM1E3wUQERGp3fd/Ps/weYwonSvD55FVl4M9O0RERKRqDDtERESkagw7REREpGoMO0RERKRqDDtERESkagw7REREpGoMO0RERKRqDDtERESkagw7REREpGoMO0RERKRqeg07x48fR6NGjeDi4gKNRoPt27fr3C8iCA4OhouLCywtLeHn54erV6/q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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Term Frequency</th>\n",
       "      <th>Percentage of Total Products</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>terms</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>pants</th>\n",
       "      <td>284</td>\n",
       "      <td>14.0%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sweaters</th>\n",
       "      <td>242</td>\n",
       "      <td>11.93%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>shorts</th>\n",
       "      <td>213</td>\n",
       "      <td>10.5%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>shoes</th>\n",
       "      <td>192</td>\n",
       "      <td>9.47%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>jeans</th>\n",
       "      <td>176</td>\n",
       "      <td>8.68%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>jackets</th>\n",
       "      <td>160</td>\n",
       "      <td>7.89%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dresses</th>\n",
       "      <td>151</td>\n",
       "      <td>7.45%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>t-shirts</th>\n",
       "      <td>147</td>\n",
       "      <td>7.25%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>suits</th>\n",
       "      <td>113</td>\n",
       "      <td>5.57%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>bags</th>\n",
       "      <td>113</td>\n",
       "      <td>5.57%</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Term Frequency Percentage of Total Products\n",
       "terms                                                \n",
       "pants                284                        14.0%\n",
       "sweaters             242                       11.93%\n",
       "shorts               213                        10.5%\n",
       "shoes                192                        9.47%\n",
       "jeans                176                        8.68%\n",
       "jackets              160                        7.89%\n",
       "dresses              151                        7.45%\n",
       "t-shirts             147                        7.25%\n",
       "suits                113                        5.57%\n",
       "bags                 113                        5.57%"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Top 10 categories by product count (Mango)\n",
    "\n",
    "frequency = mango_df['terms'].value_counts().nlargest(10)\n",
    "total_products = len(mango_df)\n",
    "percentage = ((frequency / total_products) * 100).round(2).astype(str) + '%'\n",
    "term_product_relationship = pd.DataFrame({\n",
    "    'Term Frequency': frequency,\n",
    "    'Percentage of Total Products': percentage\n",
    "})\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "term_product_relationship.plot(kind='bar', color=\"skyblue\")\n",
    "plt.title('Top 10 categories by product count in Mango Data')\n",
    "plt.xlabel('Brand')\n",
    "plt.ylabel('total')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()\n",
    "term_product_relationship"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "1b6f4c13-6d8c-421d-8e69-a0ea6fe2de43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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586dZfPmzfLXX3/Jt99+K/Pnz5f79++n2W7Ou3fvlqCgIJsxmw0aNJC//vpL7O3tRUTku+++Ez8/P/n+++8lU6ZM0r9/f2nUqJFER0dnyH2lUKFCUrp0aRGJ77bt6Ogo77zzjoSEhEjz5s2lW7duMn78eLl48aKMHj1aihcvLp988onExcXJzZs3pW7dunL27NkMfZXlwoULcubMGRGJP8aoXr26VK9eXX766SfJmTOnlC9fXrJnzy6urq4SFxcnbdu2lZCQEFmwYEEKV5529O/fXz744APJmTOniIjkzp1bihQpIqtXrxZ7e3u5ePGi/PLLL9K7d28ZNWqU/PDDDxIaGiozZsxI2cKfkb1790q3bt3kypUrqf8497nGNvxnkZGReu7cOb1586bR1qZNG82WLZtu375dVdU4exEdHa3379/X5s2b6wcffKCqXJE6evSoDhw4ULt3764rVqww2rp3766ZMmXSsWPHquq/Zx+tVwhUVU+dOvX8C07lDh48qO3atdOgoCBt1aqV/vHHHzbL+/btqxaLRf39/XXfvn1GO2d344WHh2uePHl0wYIFibZJx44dtVu3btqmTRv18fHRHTt2GMv279+foa8y3L9/X8PCwtTZ2Vl/+OEHm2UbNmzQwoULa/ny5TVv3rz6119/2SxPq9+Be/fuVWdnZx02bJiq/vs5bt26pYGBgfrZZ5/pG2+8ob6+vrpt2zbjdevXr9eTJ0+mRMmpQlRUlB49elTPnz+vX3zxhd65c0dV47dL9erVtUmTJjZ/O7/55hsdOnSo5s6dWx0dHdVisRhXpTKi8PBw9fDwMHptWL377rtatGhRVVXt2rWr+vj46O7du1VVddmyZdq3b1/dv3//c683Lerfv79my5ZN9+zZo6r//m7/73//03z58um6devUx8dHX331VWP/PXHihK5cuTLFan6Wdu3apXZ2djpixAijLTUf5xKk0pBDhw5p69attUaNGjp16lSjfeXKlVqkSBH19fW1OZC9f/++jhgxQr29vfXo0aMpUXKqsmfPHvX399eePXvqlClT9N69e8ayQ4cO6WuvvabZs2c3vpysB7Z050varl27NFu2bPr6669r9+7dtUyZMlq4cGGbfe3MmTMaFBSkEydOVNW0exD7LLVu3VqzZ8+uS5cutQlT33//vWbPnl2LFSume/fuVVW2X0L7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BolmnUO8qKgojYuL0ytXrthM0jF+/Hj19/fXVq1a6aVLl4x26wHNtWvXbGaYzOjOnTunH374ofr4+Oj777+v586d088++0wrVqyohQsXVi8vL+3Xr59aLBbNli1bhh+zcenSJT1z5ozx/y1atNCGDRvq119/raqqW7du1REjRmjt2rXV29tbPT091WKxaGBgoM2VvrTk2rVreuTIEV21alWiGQeTClNJjZnKiB7szlesWDHNkiVLorD54JWpqlWr6nvvvcf97NR2LOGQIUP0xRdf1GrVqqnFYtHChQurr6+v5s2bV3Pnzq2+vr7q5+enNWrU0IMHD6Zg1WlH//791WKxPHLyIGuYqlGjRpLdKVNDcHhakhq7av2Ou3379mPDVGpBkEqFwsPDbb6Y2rdvrwEBATYzkiS8+em9e/e0TZs2+tlnnz33WlOjyMhI9ff3N27CqBo/s2FAQIDWqlUryTOOI0aM0KCgoEQBDPFTnLdv317LlCmjbm5uGhwcbMzCpxp/E+OyZctqWFiY0fXgwaCa0SU8AL5w4YKOGTNGXV1d9YsvvjDaDx8+rN98842+9tprGhgYqJkyZcrQs21evXpVQ0JC9I033jB+Zy9evKgtW7bUypUr64wZM4zteuPGDT179qx++eWX2rt3b2Ma4bRm7969+sILL2ipUqXUYrGonZ2d1qlTR3/77TfjKkDC36uwsDC1WCy6dOnSlCo5VXlwTJk1bC5cuNBmPesB3J07d7RVq1Zau3ZtY0xQRnTnzh29e/duolnhhg0bpv7+/lq+fHkdP368zpkzR+fOnatz5szR//3vfzpnzhx6GyRT3759NVu2bDbd+awenHXv+PHjmj9/fi1WrNhDx9Smdfv379eePXvqtGnTbNoTHjskDFMJj+dSG4JUKnPz5k2tWbOmtm7d2jgYOHTokHp6empoaKj+888/xi+d9b9DhgzRggUL0kc5gXnz5qmbm5v26tXLaBs9erT6+/trmTJldP369XrmzBnduHGj9ujRQ93d3XXXrl0pWHHqtGfPHs2WLZt2795dJ0+erF999ZXWqFFDLRaLduzY0VhvzJgxWrZsWR04cCBdYxK4e/eucQYt4dm3f/75R0ePHq1ubm76/vvv27wmLi5Ob9++neTZyIzmnXfe0YoVK2pYWJixX4WHh2urVq20atWq+uWXX6abwL5v3z7NmjWr9u/fX7du3ap79+7VmTNnar58+TQgIEAXLFiQ5BncoUOHZvgrAtZZ5Nq1a5doTNnDukEmDFMZ+XftwIED2qRJE61cubKWKVNGd+7cabN82LBhWrFiRR09ejTd957QgAED1NPT0yZExcTEaLVq1fTYsWNJvubw4cM6YMCA51XicxUVFaUtW7bUggULavPmzbV48eL63XffJTlpRGRkpM6dO1ednJz0jTfeSIFqH48glQp98cUXWqlSJe3atasRpmbMmKFZs2bV4OBgXbRokV67dk1XrlypvXv31ixZstjcrBPxFi9erE5OTvrmm28abZ988okxTbybm5sWK1ZMq1SpkuRZoowuPDxcS5YsqUOGDLFpP3PmjI4ZM0bt7Oy0Z8+eRvuECRM0b968Onz48DQ93fTTcvDgQa1WrZq+/vrreurUqUTj7i5evKhjxozRrFmz6qRJk4z2jDxZjDUUJdxWY8eONa54JhWm/ve//6X5MBUREaH169fXPn36JFp24cIFLVy4sBYrVsw4WZae7hvzXzz47252TFlG/57auXOnZs2aVXv06KHDhw/XypUrq7u7e6KTYYMHD9ayZcvqiBEj0vy4w+ftjz/+UIvFouPHjzfaYmNjtXLlylqlShVjWvOEHtyv0/r3W1I+/fRTzZs3r0ZEROjYsWO1efPm6u/vrx999JHNDcVV43scLFy4MMVn53sYglQqkvCLf/r06VquXDnt2rWrMXj4p59+0kKFCqm9vb1aLBbNnz+/VqtWLc12Y3maLl++nOQv2ffff6+Ojo7ao0cPo+3atWv666+/6rx583THjh2cZXuIjRs3aunSpfXo0aPG5XbrF/o///yjAwYMUDc3N5u7q3/88cfGtOcZWWxsrE6YMEELFy6s3bp109y5c+tbb72V6EDu/PnzOnr0aPXw8NCxY8emULWph3X/unnzps1B7ujRo5MMU23bttUSJUrozJkzU6Tep+XixYtaqFAhXbx4sar+ux2sfxMOHjyoWbJk0UGDBqVYjalNwnGYjCkzb9++ferk5KTvvfee0fbNN9+oxWLRb7/9NtH6Q4YM0cDAQH3vvfcI8ib1799fXV1djUlwypcvr/Xr1zfGD6fHoPQw1t/bmJgYbdKkifHdHRERocuXL1eLxaIFChTQV155Rffs2WPcvyw1byOCVCpw8+ZNvXz5cqI7qE+f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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>Average Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ABRIGO</td>\n",
       "      <td>199.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>TRENCH</td>\n",
       "      <td>179.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>CAZADORA</td>\n",
       "      <td>172.90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AMERICANA</td>\n",
       "      <td>171.61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GABARDINA</td>\n",
       "      <td>171.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>BOTA</td>\n",
       "      <td>151.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>BOTÍN</td>\n",
       "      <td>150.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>PARKA</td>\n",
       "      <td>149.32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>CHAQUETA</td>\n",
       "      <td>144.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ZAPATO</td>\n",
       "      <td>137.28</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    category  Average Price\n",
       "0     ABRIGO         199.00\n",
       "1     TRENCH         179.00\n",
       "2   CAZADORA         172.90\n",
       "3  AMERICANA         171.61\n",
       "4  GABARDINA         171.00\n",
       "5       BOTA         151.00\n",
       "6      BOTÍN         150.25\n",
       "7      PARKA         149.32\n",
       "8   CHAQUETA         144.10\n",
       "9     ZAPATO         137.28"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Top 10 categories most valuable (Massimo Dutti) \n",
    "top_10_category_price_relationship = massimo_dutti_df.groupby('category')['price'].mean().sort_values(ascending=False).nlargest(10)\n",
    "top_10_category_price_df = top_10_category_price_relationship.reset_index().rename(columns={'price': 'Average Price'}).round(2)\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "top_10_category_price_relationship.plot(kind='bar', color = \"skyblue\")\n",
    "plt.title('Top 10 Categories by Average Price in Massimo Dutti Data')\n",
    "plt.xlabel('Category')\n",
    "plt.ylabel('Average Price')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()\n",
    "\n",
    "top_10_category_price_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "fb7a8fce-f99a-4785-bc66-64433312ab46",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Distribution of price values')"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAHFCAYAAADv8c1wAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABg7klEQVR4nO3de1xUdf4/8NdhblyEkUswkuItIglvYYtorZqKlejuum1bFOlmWGteSF3L3FbqW9hmXirLykwtK9pWbdssArMsfuINo0TNbDVBA/ECw0WcgZnP7w+YA8N1gIHh4Ov5eMxDOec9cz4fsOW1n8/nfI4khBAgIiIioma5uboBRERERErA0ERERETkAIYmIiIiIgcwNBERERE5gKGJiIiIyAEMTUREREQOYGgiIiIicgBDExEREZEDGJqIiIiIHMDQRNSJNm3aBEmS5Je7uzsMBgPGjRuH5cuXo7CwsMF7kpKSIElSq65z+fJlJCUl4euvv27V+xq7Vr9+/RAbG9uqz2nJ+++/jzVr1jR6TpIkJCUlOfV6zvbll19ixIgR8PLygiRJ+Pjjjzv0ejNmzEC/fv069Bod7ZdffoEkSdi0aZOrm0LUZgxNRC6wceNGZGZmIj09Ha+++iqGDRuGf/7znxg0aBB27txpV/vQQw8hMzOzVZ9/+fJlPP30060OTW25Vls0F5oyMzPx0EMPdXgb2koIgbvvvhsajQaffPIJMjMzMWbMmA695lNPPYXt27d36DWIqGVqVzeA6GoUERGBESNGyF//8Y9/xGOPPYZbbrkF06ZNw4kTJxAUFAQA6N27N3r37t2h7bl8+TI8PT075VotGTlypEuv35Jff/0Vly5dwh/+8AeMHz++Q69l+7kMHDiwQ69DRI7hSBNRFxESEoKVK1eitLQUb7zxhny8sSmzXbt2YezYsfD394eHhwdCQkLwxz/+EZcvX8Yvv/yCa665BgDw9NNPy1OBM2bMsPu8Q4cO4a677oKvr6/8S7m5qcDt27djyJAhcHd3x4ABA/Dyyy/bnbdNPf7yyy92x7/++mtIkiSPeo0dOxY7duzA6dOn7aYqbRqbnsvJycHvfvc7+Pr6wt3dHcOGDcPmzZsbvc4HH3yApUuXIjg4GD4+PpgwYQKOHz/e9De+joyMDIwfPx7e3t7w9PTEqFGjsGPHDvl8UlKSHCoff/xxSJLU7LSZrU1btmzBggULYDAY4OHhgTFjxuC7776zq50xYwZ69OiBw4cPIyYmBt7e3nIoa2x6zmq14pVXXsGwYcPg4eGBnj17YuTIkfjkk0/s6j788ENER0fDy8sLPXr0wKRJkxpcu77vv/8ekiRhw4YNDc59/vnnkCRJvs7PP/+Mv/zlLwgNDYWnpyeuvfZaTJkyBYcPH272Gk31C2j836EQAq+99prcX19fX9x11104efKkXd13332H2NhYBAYGQqfTITg4GJMnT8aZM2dabA9RSxiaiLqQO++8EyqVCt98802TNb/88gsmT54MrVaLt99+G6mpqXj++efh5eUFs9mMXr16ITU1FQAwc+ZMZGZmIjMzE0899ZTd50ybNg3XXXcdPvroI7z++uvNtis7OxuJiYl47LHHsH37dowaNQrz58/Hiy++2Oo+vvbaaxg9ejQMBoPctuamBI8fP45Ro0bhyJEjePnll7Ft2zaEh4djxowZeOGFFxrUP/nkkzh9+jTeeustvPnmmzhx4gSmTJkCi8XSbLt2796N2267DUajERs2bMAHH3wAb29vTJkyBR9++CGA6unLbdu2AQDmzp2LzMxMh6bNnnzySZw8eRJvvfUW3nrrLfz6668YO3Zsg1/4ZrMZU6dOxW233Yb//Oc/ePrpp5v8zBkzZmD+/Pm4+eab8eGHHyIlJQVTp061C63Jycm49957ER4ejn/961949913UVpailtvvRVHjx5t8rOHDh2K4cOHY+PGjQ3Obdq0CYGBgbjzzjsBVI+8+fv74/nnn0dqaipeffVVqNVqREVFORxWHfHwww8jMTEREyZMwMcff4zXXnsNR44cwahRo3Du3DkAQHl5OSZOnIhz587h1VdfRXp6OtasWYOQkBCUlpY6rS10FRNE1Gk2btwoAIgDBw40WRMUFCQGDRokf71s2TJR9z/Vf//73wKAyM7ObvIzzp8/LwCIZcuWNThn+7x//OMfTZ6rq2/fvkKSpAbXmzhxovDx8RHl5eV2fTt16pRd3VdffSUAiK+++ko+NnnyZNG3b99G216/3ffcc4/Q6XQiNzfXru6OO+4Qnp6eori42O46d955p13dv/71LwFAZGZmNno9m5EjR4rAwEBRWloqH6uqqhIRERGid+/ewmq1CiGEOHXqlAAgVqxY0ezn1W3TTTfdJL9fCCF++eUXodFo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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(df_cleaned['price'], kde=True, bins=30, color=\"skyblue\")\n",
    "plt.title('Distribution of price values')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5edc3c02-55a2-4957-abeb-ec03b74cb487",
   "metadata": {},
   "source": [
    "## HYPOTHESIS TESTING"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b931705-ac14-4d37-b0c1-b118d6a46938",
   "metadata": {},
   "source": [
    "## ONE SAMPLE T-TEST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "5436a429-be2e-44fe-b3f8-debfacbe5c1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the hypothesis\n",
    "\n",
    "#H0: avg prices for Man == 55\n",
    "#H1: avg prices for Man != 55\n",
    "\n",
    "#Significance Level = 0,05"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "2707bc79-6a8e-4817-ad9b-6f9fbc977a30",
   "metadata": {},
   "outputs": [],
   "source": [
    "men_section_mu_price = df_cleaned[df_cleaned['section']== 'Man']['price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "ad9c6589-abc5-441f-9b4a-2e9dfbf37846",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t-stat: -3.7563677029072364, p_value: 0.0001732849197274086\n"
     ]
    }
   ],
   "source": [
    "alpha = 0.05\n",
    "t_stat, p_value = st.ttest_1samp(men_section_mu_price, 55)\n",
    "print(f\"t-stat: {t_stat}, p_value: {p_value}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "c7e2cf3a-abe1-4ab0-9581-2cb0bde19ce4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We reject the null hypotesis\n"
     ]
    }
   ],
   "source": [
    "if p_value > alpha:\n",
    "    print(\"We are not able to reject the null hypothesis\")\n",
    "else:\n",
    "    print(\"We reject the null hypotesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "e657b8bb-d34c-44dd-81fc-af4e3774f55a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean price for man: 53.374136880486034\n"
     ]
    }
   ],
   "source": [
    "mu_man = men_section_mu_price.mean()\n",
    "print(f\"Mean price for man: {mu_man}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8176fe47-a214-45a7-abec-da037f1ecbf5",
   "metadata": {},
   "source": [
    "## TWO SAMPLE T-TEST (indep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "8b2c7f2b-0550-464e-8653-f6dc42827165",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set the hypothesis\n",
    "\n",
    "#H0: mu price male >= mu price female\n",
    "#H1: mu price male < mu price female\n",
    "\n",
    "#significance level = 0.05"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "06cdf104-0c55-46e6-bd28-d4d91648b963",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_woman = df_cleaned[df_cleaned['section']== 'Woman']['price']\n",
    "df_man = df_cleaned[df_cleaned['section']== 'Man']['price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "632c3b65-d15c-479c-be80-1483704b1d5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t-stat: 55.15809761933002, p_value: 1.0\n"
     ]
    }
   ],
   "source": [
    "alpha = 0.05\n",
    "t_stat, p_value = st.ttest_ind(df_man,df_woman, equal_var=False, alternative = \"less\")\n",
    "print(f\"t-stat: {t_stat}, p_value: {p_value}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "11ddb38c-6ead-4011-bdce-643333e5763c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We are not able to reject the null hypothesis\n"
     ]
    }
   ],
   "source": [
    "if p_value > alpha:\n",
    "    print(\"We are not able to reject the null hypothesis\")\n",
    "else:\n",
    "    print(\"We reject the null hypotesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "1b5bd070-cd1d-4eca-a73b-0a3a46ab2629",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean price for woman: 28.87592054711818, Mean price for Man: 53.374136880486034\n"
     ]
    }
   ],
   "source": [
    "mu_woman = df_woman.mean()\n",
    "mu_man = df_man.mean()\n",
    "print(f\"Mean price for woman: {mu_woman}, Mean price for Man: {mu_man}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5100ed26-307e-4f70-9f95-cd432de09e48",
   "metadata": {},
   "source": [
    "## TWO SAMPLE T-TEST (indep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "0fc0dfb2-5fa2-4cae-bbe4-6eeb54f0fc5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set the hypothesis\n",
    "\n",
    "#H0: mu price Zara >= mu price Massimo Duti\n",
    "#H1: mu price Zara < mu price Massimo Duti\n",
    "\n",
    "#significance level = 0.05"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "bedb361d-113f-46f8-bf57-bd32bc549262",
   "metadata": {},
   "outputs": [],
   "source": [
    "zara = zara_df['price€']\n",
    "massimo_dutti = massimo_dutti_df['price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "a6bef399-af02-45b6-8891-7f199c3eebb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t-stat: -8.083103344524007, p_value: 4.203232325061037e-15\n"
     ]
    }
   ],
   "source": [
    "alpha = 0.05\n",
    "t_stat, p_value = st.ttest_ind(zara, massimo_dutti, equal_var=False, alternative = \"less\")\n",
    "print(f\"t-stat: {t_stat}, p_value: {p_value}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "1959e35e-78c0-49c7-b80a-93da813c1433",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We reject the null hypotesis\n"
     ]
    }
   ],
   "source": [
    "if p_value > alpha:\n",
    "    print(\"We are not able to reject the null hypothesis\")\n",
    "else:\n",
    "    print(\"We reject the null hypotesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "7d86e00f-1b2d-427b-9f75-081bfb91f94c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean price for Zara: 72.445976, Mean price for Massimo Dutti: 96.88293135435994\n"
     ]
    }
   ],
   "source": [
    "mu_zara=zara.mean()\n",
    "mu_md =massimo_dutti.mean()\n",
    "print (f\"Mean price for Zara: {mu_zara}, Mean price for Massimo Dutti: {mu_md}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e4ed83b-3c44-4f77-814a-7eb7f9d7c203",
   "metadata": {},
   "source": [
    "## PROPORTION Z-TEST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "b38bf43b-c57c-4764-ba31-a82cef4b9209",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set the hypothesis\n",
    "\n",
    "#H0:  proportion of 'shoes' in the dataset = 0.3 \n",
    "#H1:  proportion of 'shoes' in the dataset!= 0.3\n",
    "\n",
    "#significance level = 0.05"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "591cb263-fbb7-470e-a723-c23fcd4d1c89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Z-statistic: -507.5623448718427, P-value: 0.0\n",
      "Reject the null hypothesis. The proportion of 'Shoes' is significantly different from 0.3.\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from statsmodels.stats.proportion import proportions_ztest\n",
    "\n",
    "n = len(df_cleaned['category'])\n",
    "count_shoes = (df_cleaned['category'] == 'Shoes').sum()\n",
    "\n",
    "p0 = 0.3\n",
    "stat, p_value = proportions_ztest(count_shoes, n, p0)\n",
    "\n",
    "print(f\"Z-statistic: {stat}, P-value: {p_value}\")\n",
    "\n",
    "alpha = 0.05\n",
    "\n",
    "if p_value < alpha:\n",
    "    print(\"Reject the null hypothesis. The proportion of 'Shoes' is significantly different from 0.3.\")\n",
    "else:\n",
    "    print(\"Fail to reject the null hypothesis. The proportion of 'Shoes' is not significantly different from 0.3.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "4066da79-4ab0-4582-9c9f-fb682391b1d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Actual proportion of 'Shoes': 0.0297\n"
     ]
    }
   ],
   "source": [
    "# Actual proportion of \"Shoes\"\n",
    "proportion_shoes = count_shoes / n\n",
    "\n",
    "print(f\"Actual proportion of 'Shoes': {proportion_shoes:.4f}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import pandas as pd

def load_data():
    file_path = 'brands.csv' 
    data = pd.read_csv(file_path)
    return data

    return data
