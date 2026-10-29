# Kurs: AI Ops

Välkommen till utbildningsrepositoryt för **AI Ops**. Detta repo innehåller kursmaterial, Jupyter-notebooks och nödvändiga konfigurationsfiler för att du ska komma igång med praktiska AI- och LLM-tillämpningar.

## Struktur och Innehåll

Repositoryt är uppdelat i följande moduler:

*   **`01_setup/`**
    Innehåller guider och notebooks för att konfigurera din arbetsmiljö. 
    *Nyckelfil:* `pydantic_with_nvidia_build.ipynb`
*   **`02_llm_intro/`**
    Introduktion till Large Language Models (LLMs) och hur man interagerar med dem.
    *Nyckelfil:* `llm_intro.ipynb`

## Systemkrav och Verktyg

Projektet är konfigurerat med moderna verktyg för Python-utveckling. För att köra koden behöver du:

1.  **Python**: Se filen `.python-version` (Python 3.13) för exakt version.
2.  **uv**: Projektet använder `uv` (via `pyproject.toml` och `uv.lock`) för extremt snabb beroendehantering.
3.  **Jupyter Notebook**: För att exekvera `.ipynb`-filerna (rekommenderas via VS Code eller webbläsare).

## Kom igång

Följ dessa steg för att sätta upp miljön på din lokala maskin:

**1. Klona repositoryt**
```bash
git clone <din-repo-url>
cd AI_01_DE25_Rikard_Oledal
```

**2. Installera beroenden med `uv`**
Säkerställ att du har installerat `uv` (t.ex. `pip install uv` eller via deras officiella installationsskript). Kör sedan:
```bash
uv sync
```
Detta skapar automatiskt en virtuell miljö och installerar alla paket som definieras i `pyproject.toml` och låses i `uv.lock`.

**3. Kör Notebooks**
När installationen är klar kan du starta Jupyter och navigera till modulerna:
```bash
uv run jupyter notebook
```
*(Om du använder VS Code, se till att välja den virtuella miljö som `uv` skapade som din Python-kernel).*

## Om Kursen
Denna del av utbildningen fokuserar på AI Operations, från initial setup av miljön (inklusive pydantic och NVIDIA-verktyg) till grundläggande integration och arbete med språkmodeller (LLMs). Gå igenom mapparna i nummerordning för bästa inlärningskurva.