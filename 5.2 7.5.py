docs = ['//doc/5041434?query=data%20science','//doc/5041567?query=data%20science', '//doc/4283670?query=data%20science','//doc/3712659?query=data%20science', '//doc/4997267?query=data%20science'  
]  
## links = ['https://www.kommersant.ru//doc/5041434?query=data%20science', 'https://www.kommersant.ru//doc/5041567?query=data%20science', 'https://www.kommersant.ru//doc/4283670?query=data%20science', 'https://www.kommersant.ru//doc/3712659?query=data%20science', 'https://www.kommersant.ru//doc/4997267?query=data%20science']  

docs = ['//doc/5041434?query=data%20science','//doc/5041567?query=data%20science','//doc/4283670?query=data%20science','//doc/3712659?query=data%20science','//doc/4997267?query=data%20science','//doc/4372673?query=data%20science','//doc/3779060?query=data%20science','//doc/3495410?query=data%20science','//doc/4308832?query=data%20science','//doc/4079881?query=data%20science'  
]  
## links = ['https://www.kommersant.ru//doc/5041434?query=data%20science', 'https://www.kommersant.ru//doc/5041567?query=data%20science', 'https://www.kommersant.ru//doc/4283670?query=data%20science', 'https://www.kommersant.ru//doc/3712659?query=data%20science', 'https://www.kommersant.ru//doc/4997267?query=data%20science', 'https://www.kommersant.ru//doc/4372673?query=data%20science', 'https://www.kommersant.ru//doc/3779060?query=data%20science', 'https://www.kommersant.ru//doc/3495410?query=data%20science', 'https://www.kommersant.ru//doc/4308832?query=data%20science', 'https://www.kommersant.ru//doc/4079881?query=data%20science']

links =list(map(lambda name: "https://www.kommersant.ru" + name, docs))
print(links)