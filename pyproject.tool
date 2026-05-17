[tool.ruff]
# Diz ao Ruff que essas variáveis globais do Databricks são nativas e não devem gerar erro F821
builtins = ["dbutils", "spark", "display"]

[tool.ruff.lint]
# Mantém as regras padrões, mas você pode customizar/ignorar regras específicas aqui se precisar no futuro
ignore = []