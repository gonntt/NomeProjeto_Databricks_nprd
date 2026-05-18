# Databricks notebook source
# MAGIC %md
# MAGIC # PoC DataOps - Teste de Deploy
# MAGIC Este notebook foi implantado via esteira OIDC + Key Vault.

# COMMAND ----------

# CORREÇÃO: O 'import os' foi removido porque não estava sendo usado no código
# Capturando parâmetro passado pelo manifesto bundle


client_id_param = dbutils.widgets.get("env_client_id")

# CORREÇÃO: Removido o prefixo 'f' desta primeira string porque ela não possui placeholders {}
print("✅ Notebook executado com sucesso!")
print(f"🚀 Projeto: {spark.conf.get('spark.databricks.bundle.name', 'N/A')}")
print(f"📍 Ambiente: {spark.conf.get('spark.databricks.bundle.target', 'N/A')}")

# Validação de segurança: o valor real da secret nunca deve ser impresso, 
# mas confirmamos que o parâmetro chegou.
if client_id_param:
    print("🔒 Credenciais injetadas via Key Vault foram reconhecidas pelo Job.")
else:
    print("⚠️ Atenção: Parâmetro de credencial não encontrado.")

# COMMAND ----------

# Exemplo de listagem de arquivos no DBFS para testar permissão
display(dbutils.fs.ls("/"))