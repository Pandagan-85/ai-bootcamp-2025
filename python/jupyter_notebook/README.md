# Jupyter Notebook
Troverai un file env.yml con cui potrai replicare il mio ambiente, dentro la cartella env_backup

## Setup dell'Ambiente con Conda

1. **Creazione dell'ambiente Conda:**

   Per ricreare l'ambiente virtuale con tutte le dipendenze, puoi usare il file `env.yml`. Questo file contiene le configurazioni necessarie per installare i pacchetti richiesti dal progetto.

   Esegui il comando seguente per creare un ambiente Conda a partire dal file `env.yml`:

   ```shell
   conda env create -f env.yml
   ```
   
2. **Una volta che l'ambiente è stato creato, puoi attivarlo con:**

    ```shell
    conda activate nome-ambiente
    ```

3. **Avviare Jupyter Notebook:**
Con l'ambiente attivato, puoi avviare Jupyter Notebook con il comando:
    ```shell
    jupyter notebook
    ```
   

---

## Setup in PyCharm
Se desideri usare PyCharm per lavorare sul progetto, segui questi passaggi:

Aprire il progetto in PyCharm:

Apri PyCharm e seleziona Open per aprire la cartella del progetto.
Configurare l'ambiente Conda in PyCharm:

Vai su `File > Settings` (su Windows/Linux) o `PyCharm > Settings` (su macOS).

Nella barra laterale sinistra, seleziona `Project: <nome del progetto> > Python Interpreter`.

Clicca `Add interpreter > Add Local Interpreter`, `Type: > Conda`.

Seleziona `Existing environment`.

Adesso potrai selezionare e usare l'ambiente creato dal file yml con Conda.