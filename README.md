**<h2>API with FastAPI</h2>**  

###

A brief description of FastAPI and how to use it.

---

An API developed with `FastAPI` that returns information based on names via the `/name` route.

###

**<h2>Dependency Installation</h2>**

###

- Enter the cloned repository:

###
```powershell
cd Projects
```

- Create and activate the Virtual Environment `env`:

###

Windows

###

```powershell
python -m venv env  ### Creates the env
```

###
```powershell
.\env\Scripts\activate ### Activates the env
```

MacOS/Linux

###

```powershell
python3 -m venv env
```

###

```powershell
source env/bin/activate
```

- Install the dependencies:

###
```powershell
pip install fastapi uvicorn ### install FastAPI and Uvicorn directly (if you don't have requirements.txt)
```

**<h2>Running the Application</h2>**

###

After following the steps above, type:

###

```powershell
uvicorn main:app --reload
```

The application will be available at:

###

```powershell
http://127.0.0.1:8000/name
```

---

**<h2>Cloning for Tests</h2>**

###
```powershell
cd https://github.com/kauanvinicius9/Bootcamp.Py
```

###
```powershell
python -m venv env
```

###
```poweshell
.\env\Scripts\activate  # or source env/bin/activate
```

###
```powershell
pip install -r requirements.txt
```

###
```powershell
uvicorn main:app --reload
```
