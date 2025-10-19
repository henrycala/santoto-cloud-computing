# 🧠 Santoto Cloud Computing

Este repositorio contiene los ejercicios, proyectos y recursos desarrollados durante el curso **Computación en la Nube**.  
Cada carpeta corresponde a una actividad o aplicación independiente relacionada con los temas del módulo.

---

## 📂 Proyecto: `app-st-ai-agent`

Esta aplicación utiliza **Streamlit** y la API de **OpenAI** para construir un agente conversacional inteligente.  
A continuación, se describen los pasos necesarios para ejecutarla en tu entorno local.

---

### ⚙️ Requisitos previos

- Tener **Python 3.10+** instalado.  
- Contar con **Poetry** como manejador de dependencias.  
- Disponer de una clave válida de la **API de OpenAI**.

---

### 🚀 Ejecución local

1. **Accede al directorio de la aplicación**

   ```bash
   cd app-st-ai-agent
    ```

2. **Crea el archivo .env**

En la carpeta **app-st-ai-agent**, crea un archivo llamado .env con tu clave de OpenAI.
Puedes guiarte del archivo sample.env.

3. **Instala las dependencias del proyecto**

   ```bash
    poetry install --no-root
     ```

4. **Ejecuta la aplicación**

   ```bash
    poetry run streamlit run app.py
     ```