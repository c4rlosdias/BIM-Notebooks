BIM Notebooks
============
Coletânea de notebooks do jupyter para análise e manipulação de modelos BIM no formato IFC.

IFC_Query
----------
Este notebook permite analisar destacar elementos pesquisados numa visualização do modelo BIM, em formato SPF (padrão IFC) no Jupyter Notebook. 


![IfcQuery](https://user-images.githubusercontent.com/57261862/114325355-0f13d880-9b06-11eb-8a92-60c376dffb8b.PNG)


Pré-requisitos
--------------
* k3d [https://anaconda.org/conda-forge/k3d]
* Ifcopenshell [http://ifcopenshell.org/]
* PythonOCC [https://anaconda.org/conda-forge/pythonocc-core]
* lark-parser [https://anaconda.org/conda-forge/lark-parser]
* Ipywidgets [https://anaconda.org/anaconda/ipywidgets]


### Dependências
Para instalar todas as depedencias use:

    > !pip install -r requirements.txt

**Nota:** As consultas seguem a sintaxe definida no módulo select do ifcopenshell. Para mais informações, veja:
* [https://wiki.osarch.org/index.php?title=IfcOpenShell_code_examples](https://wiki.osarch.org/index.php?title=IfcOpenShell_code_examples)  
