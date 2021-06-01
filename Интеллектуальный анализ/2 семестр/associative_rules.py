import numpy as np
import pandas as pd

file = open('./pluginfile.txt', 'r', encoding='utf-8')
numbers, product = list(), list()
for line in file:
    numbers.append(line[0:6])
    product.append(line[7:].replace('\t', '').replace('\n', ''))

df = pd.DataFrame({'trans': numbers, 'item': product}).drop(0)

"""
Класс инициируется 3мя параметрами:
- min_supp - минимальный support который мы рассматриваем для ItemSet
. Рассчитывается как % от количества транзакций
- max_items - максимальное количество елементов в нашем ItemSet
- min_items - минимальное количество элементов ItemSet
"""
class Eclat:
    def __init__(self, min_support = 0.01, max_items = 5, min_items =2):
        self.min_support = min_support
        self.max_items = max_items
        self.min_items = min_items
        self.item_lst = []
        self.item_len = 0
        self.item_dict = {}
        self.final_dict = dict()
        self.data_size = 0

#создание словаря из ненулевых объектов из всех транзакций (вертикальный датасет)
    def read_data(self, dataset):
        for index, row in dataset.iterrows():
            row_wo_na = set(row[0])
            for item in row_wo_na:
                item = item.strip()
                if item in self.item_dict:
                    self.item_dict[item][0] += 1
                else:
                    self.item_dict.setdefault(item, []).append(1)
                self.item_dict[item].append(index)
        #задаем переменные экземпляра (instance variables)
        self.data_size = dataset.shape[0]
        self.item_lst = list(self.item_dict.keys())
        self.item_len = len(self.item_lst)
        self.min_support = self.min_support * self.data_size
        #print ("min_supp", self.min_support)
    
    #рекурсивный метод для поиска всех ItemSet по алгоритму Eclat
    #структура данных: {Item: [Supp number, tid1, tid2, tid3, ...]}
    def recur_eclat(self, item_name, tids_array, minsupp, num_items, k_start):
        if tids_array[0] >= minsupp and num_items <= self.max_items:
            for k in range(k_start+1, self.item_len):
                if self.item_dict[self.item_lst[k]][0] >= minsupp:
                    new_item = item_name + " | " + self.item_lst[k]
                    new_tids = np.intersect1d(tids_array[1:], self.item_dict[self.item_lst[k]][1:])
                    new_tids_size = new_tids.size
                    new_tids = np.insert(new_tids, 0, new_tids_size)
                    if new_tids_size >= minsupp:
                        if num_items >= self.min_items: 
                            self.final_dict.update({new_item: new_tids})
                        self.recur_eclat(new_item, new_tids, minsupp,num_items+1, k)
    
    #последовательный вызов функций определенных выше
    def fit(self, dataset):
        self.read_data(dataset)
        for i, w in enumerate(self.item_lst):
            self.recur_eclat(w, self.item_dict[w], self.min_support, 2, i)
        return self
    #вывод в форме словаря {ItemSet: support(ItemSet)}
    def transform(self):
        return {k: (v[0]+0.0)/self.data_size*100 for k, v in self.final_dict.items()}
    
    df.trans = pd.to_numeric(df.trans, errors='coerce')df.dropna(axis = 0, how = 'all', inplace = True)
    df.trans = df.trans.astype(int)
    df = df.groupby('trans').agg(lambda x: x.tolist())
    model = Eclat(min_support = 0.0001, max_items = 5, min_items = 1)
    model.fit(df)
    answer = model.transform()
    
    def search_apriori_rules(product=None, top=True):
        list_d = list(answer.items())
        list_d.sort(key=lambda i: i[1], reverse=top)
        print('SUPPORT RULES')
        for i in list_d:
            if product is None:
                print("{0:.4f}%".format(i[1]), ':', i[0])
            else:
                flag = all(j in i[0] for j in product)
                if flag:
                    print("{0:.4f}%".format(i[1]), ':', i[0])
