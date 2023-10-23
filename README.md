# cnpjinfo

**cnpjinfo** is a library for obtaining cnpj information via scraping from the receitaws website.

## Features

- CNPJ information via receitaws website.

## Installation

- Run `pip install cnpjinfo`

## Exxemple

```python
from cnpjinfo import cnpjinfo, cnpjinfo_list

# For one CNPJ
info = cnpjinfo('12345678901234')
nome = info.get('nome')
tel = info.get('telefone')
email = info.get('email')
print (f'Nome: {nome}, Tel: {tel}, e-Mail: {email}'))

# For CNPJ list
cnpj_list = [ "05720854000166", "00623904000173", "15436940000103" ]
result = cnpjinfo_list(cnpj_list)
for cnpj in result:
    info = cnpjinfo(cnpj)
    nome = info.get('nome')
    tel = info.get('telefone')
    email = info.get('email')
    print (f'Nome: {nome}, Tel: {tel}, e-Mail: {email}'))
```

### console output

```bash
foo@bar:~$ python myscript.py
Nome: COMPANY NAME., Tel: (11) 1111-1111
foo@bar:~$ 
```

## Upgrade

```bash
foo@bar:~$ Run `pip install cnpjinfo --upgrade`
```
