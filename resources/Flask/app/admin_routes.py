try:
    from flask import render_template
except ImportError as eImp:
    print(f"The following import error occurred in file {__file__}: {eImp}")

# ------------------Admin routes------------------
# Below define your admin routes