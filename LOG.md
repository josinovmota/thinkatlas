## 2026/11/01 - Domingo

### Learning-log

- O que aprendi: Aprendi a inicializar um repositório com `uv` ( criador de virtual environments muito rápido ) e configurar um `pre-commit` com alguns hooks importantes, como `huff` e as próprias checagens do `uv`
- Onde travei: Eu tentei instalar o `pre-commit` com `uv add` e não funcionou. Só foi bem depois que eu entendi que ele é um `uv tool`
- Próximo passo: Começar o dia 2

## 2026/11/02 - Segunda-Feira

### Pytest

- Why i'm studying this: As I saw while I was studying `Java`, unit-tests are a very important part of the development since they ensure you that the code is running the way it was created to run. We are humans ( this is kind a joke right now, since we're living the AI's era ) and we can commit errors and don't look properly at them. I found out in my last projects that some errors just don't appear immediately and if you don't catch them, they'll problably become a snowball later. Quoting the book The `Pragmatic Programmer`, "One broken window, left unrepaired for any substantial length of time, instills in the inhabitants of the building a sense of abandonment — a sense that the powers that be don’t care about the building". 

- What it solves: It's one more layer to protect you against your code doing something that it's not supposed to do

- Write a code that use it: [link to the code](C:\Users\josinovmota\Desktop\Workspace\thinkatlas\tests\test_pytest.py)

## 2026/11/03 - Terça-Feira

### Ci

- Why i'm studying this: Helps you to more secure about everything that you're pushing to your main branch.
- What does it do: CI helps us to add another layer of security to our version control system. It will assure that whenever it finds an error, it'll break the `git push`, forcing you to fix it or flag it as a controlled error
- Write a code that use it: [link to the ci](C:\Users\josinovmota\Desktop\Workspace\thinkatlas\.github\workflows\ci.yml)

## 2026/11/10 - Terça-Feira

### Git essentials

- Why i'm studying this: A version control system is an essential part of the development, even in my studies. It can help me to save my files in the cloud, undo problems that I created in the my repository thinkatlas and upload everything to github, so I can visualize it a little better
- What does it do: It creates the bridge between my computer and the github and also helps me to work with snapshots of my files, so when I commit an error, I can easily revert it
- Write a code that use it: I've typed a lot of commands in my terminal, so I can't point it here, but I got used to `git add`, `git commit`, `git push`, `git branch`, `git switch`, `git checkout`, `git log`, `git revert`, `git merge`, `git diff`.

## 2026/11/17 - Terça-Feira

### Python occult methods

- Why am I studying this: In Python you can use some tricks to access info about a object. We're able to use len(object) to discover the object size and we can use object[position] to discover the value that have the position index. This is normal in python so we learn it from the beggining, but when we learn about Classes and create them, our classes don't have the capability to invoke this special methods. That's why we use the occult methods __len__ and __getitem__. Whenever we do a `len(object)` we're invoking __len__(object), so if we create methods to do this inside our Class, we can able it to work in a more "Pythonic" way
- What does it do: First of all we can use it to make your code clear, so the user don't have to think "What should I do to access the len of this object?". Instead, he'll just use the good old python
- Write a code that use it: [special_methods](exercises\fluent-python-chapter-1\main.ipynb)
